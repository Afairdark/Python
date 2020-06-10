#coding:gbk
"""
����Ŀ�ģ���������GDP��ʷ���ݻ������༰����ӻ��Ĺ��ܱ�д
���ߣ�������
"""

import csv
import math
import pygal
import pygal_maps_world #������Ҫʹ�õĿ�


def read_csv_as_nested_dict(filename, keyfield, separator, quote): #��ȡԭʼcsv�ļ������ݣ���ʽΪǶ���ֵ�
	"""
	�������:
	filename:csv�ļ���
	keyfield:����
	separator:�ָ���
	quote:���÷�
	���:
	��ȡcsv�ļ����ݣ�����Ƕ���ֵ��ʽ����������ֵ�ļ���Ӧ����keyfiled���ڲ��ֵ��Ӧÿ���ڸ�������Ӧ�ľ���ֵ
	"""
	result={}
	with open(filename,newline="") as csvfile:
		csvreader = csv.DictReader(csvfile,delimiter=separator,quotechar=quote)
		for row in csvreader:
			rowid = row[keyfield]
			result[rowid] = row
			
	return result
	
pygal_countries = pygal.maps.world.COUNTRIES #��ȡpygal.maps.world�й��Ҵ�����Ϣ��Ϊ�ֵ��ʽ�������м�Ϊpygal�и������룬ֵΪ��Ӧ�ľ������(���齫����ʾ����Ļ���˽�����ʽ���������ݣ�


def reconcile_countries_by_name(plot_countries,gdp_countries): #������������GDP���ݵĻ�ͼ����Ҵ����ֵ䣬�Լ�û������GDP���ݵĹ��Ҵ��뼯��
	"""
	�������:
	plot_countries: ��ͼ����Ҵ������ݣ��ֵ��ʽ�����м�Ϊ��ͼ����Ҵ��룬ֵΪ��Ӧ�ľ������
	gdp_countries:���и������ݣ�Ƕ���ֵ��ʽ�������ⲿ�ֵ�ļ�Ϊ���й��Ҵ��룬ֵΪ�ù��������ļ��е������ݣ��ֵ��ʽ)
	�����
	����Ԫ���ʽ������һ���ֵ��һ�����ϡ������ֵ�����Ϊ��������GDP���ݵĻ�ͼ�������Ϣ����Ϊ��ͼ������Ҵ��룬ֵΪ��Ӧ�ľ������),
	��������Ϊ��������GDP���ݵĻ�ͼ����Ҵ���
	"""
	dil = {}
	jihe = set()
	Tup = (dil,jihe)
	for xx in plot_countries:
		for i in gdp_countries.values():
			if plot_countries[xx] == i["Country Name"]:
				for year in range(1960,2016):
					if i[str(year)] == "": #�����һ��GDP��Ϊ�գ�������ֵ�
						continue
					else:
						dil[xx] = i
	for xq in plot_countries: #���й��Ҵ����ȥ�ֵ��е�Ϊ��GDP��¼�Ĺ���
		if xq not in dil:
			jihe.add(xq)
			
	return Tup
	
	
	
def build_map_dict_by_name(gdpinfo,plot_countries, year):
	"""
	�������:
	gdpinfo:
	plot_countries: ��ͼ����Ҵ������ݣ��ֵ��ʽ�����м�Ϊ��ͼ����Ҵ��룬ֵΪ��Ӧ�ľ������
	year: �������ֵ
	�����
	�������һ���ֵ�Ͷ������ϵ�Ԫ�����ݡ������ֵ�����Ϊ��ͼ������Ҵ��뼰��Ӧ����ĳ�������GDP��ֵ����Ϊ��ͼ���и����Ҵ��룬ֵΪ�ھ�����ݣ���year����ȷ��������Ӧ������GDP����ֵ��Ϊ
	������ʾ���㣬GDP�����ת��Ϊ��10Ϊ�����Ķ�����ʽ����GDPԭʼֵΪ2500����ӦΪlog2500��ps:����math.log()���)
	2������һ��Ϊ������GDP��������ȫû�м�¼�Ļ�ͼ����Ҵ��룬��һ������Ϊֻ��û��ĳ�ض��꣨��year����ȷ��������GDP���ݵĻ�ͼ����Ҵ���
	"""
	Tup1=reconcile_countries_by_name(plot_countries,read_csv_as_nested_dict("isp_gdp.csv","Country Code",",",'"'))
	Dict = {}
	A1 = set()
	A2 = set()
	A3 = set()
	with open(gdpinfo["gdpfile"],"rt") as csvfile:
		reader = csv.DictReader(csvfile,delimiter=gdpinfo["separator"],quotechar=gdpinfo["quote"])
		for cow in reader:
			for xx in plot_countries:
				country = plot_countries[xx]
				if country == cow[gdpinfo["country_name"]] and cow[year] != "":
					Dict[xx] = math.log10(float(cow[year])) #�����м�¼�ľͼ����ֵ�
				elif country == cow[gdpinfo["country_name"]] and cow[year] == "":
					A2.add(xx) #������GDP��¼�Ĺ���
				else:
					continue
	A1 = Tup1[1] #��ȫû��GDP��¼�Ĺ��Ҵ���
	A3 = A2-A1 #��û��ĳ�ض����¼�Ĺ���
	Tup = (Dict,A1,A3)
	
	return Tup
	
	
	
def render_world_map(gdpinfo, plot_countries, year, map_file): #������ĳ�����������GDP����(����ȱ��GDP�����Լ�ֻ���ڸ���ȱ��GDP���ݵĹ���)�Ե�ͼ��ʽ���ӻ�
	"""
	Inputs:
	gdpinfo:gdp��Ϣ�ֵ�
	plot_countires:��ͼ����Ҵ������ݣ��ֵ��ʽ�����м�Ϊ��ͼ����Ҵ��룬ֵΪ��Ӧ�ľ������
	year:����������ݣ����ַ�����ʽ������"1970"
	map_file:�����ͼƬ�ļ���
	Ŀ�꣺��ָ��ĳ����������GDP�����������ͼ����ʾ������������Ϊ����ĵ�ͼƬ�ļ�
	��ʾ�����������ӻ���Ҫ����pygal.maps.world.World()����
	"""
	worldmap_chart = pygal.maps.world.World()
	worldmap_chart.title = "ȫ��GDP�ֲ�ͼ" #����
	worldmap_chart.add(year,build_map_dict_by_name(gdpinfo,plot_countries, year)[0]) #��GDP�Ĺ��һ�ͼ
	worldmap_chart.add("missing from world bank",build_map_dict_by_name(gdpinfo,plot_countries, year)[1]) #��ȫû��GDP��¼�Ĺ���ͼ
	worldmap_chart.add("no data at this year",build_map_dict_by_name(gdpinfo,plot_countries, year)[2]) #��û��ĳ�ض����¼�Ĺ���ͼ
	worldmap_chart.render_to_file(map_file) #����ļ�
	
	
	
def test_render_world_map(year): #���Ժ���
	"""
	�Ը����ܺ������в���
	"""
	gdpinfo = {
	"gdpfile": "isp_gdp.csv",
	"separator": ",",
	"quote": '"',
	"min_year": 1960,
	"max_year": 2015,
	"country_name": "Country Name",
	"country_code": "Country Code"
	} #���������ֵ�
	pygal_countries = pygal.maps.world.COUNTRIES # ��û�ͼ��pygal���Ҵ����ֵ�
	render_world_map(gdpinfo, pygal_countries, year, "isp_gdp_world_name_%s.svg"%year) #���ú���
	print("���ӻ����")
	# ����ʱ����1970��Ϊ�����Ժ����������ԣ������н�����ṩ��svg���жԱȣ�������ݿɽ��ļ���������
	
	
	
	#������Ժ�����
print("��ӭʹ������GDP���ݿ��ӻ���ѯ")
print("----------------------")
year=input("���������ѯ�ľ������:")
test_render_world_map(year)