#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：张轩齐
日期：2020/4/8
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
	"""
	将游戏对象对应到不同的整数
	"""
	if name == str('石头'):
		number = 0
		return number
	elif name == str('史波克'):
		number = 1
		return number
	elif name == str("纸"):
		number=2
		return number
	elif name == str("蜥蜴"):
		number=3
		return number
	elif name == str("剪刀"):
		number=4
		return number	
	else:
		number=520
		return number



def number_to_name(number):
	"""
	将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
	"""
	if number==0:
		name=str("石头")
		return name
	elif number==1:
		name=str("史波克")
		return name
	elif number==2:
		name=str("纸")
		return name
	elif number==3:
		name=str("蜥蜴")
		return name
	else:
		name=str("剪刀")
		return name
    


def rpsls(player_choice):
	"""
	用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

	"""
	print("-------- ")
	print("您的选择为：",choice_name)
	player_choice=choice_name        #将自己的游戏选择对象存入变量player_choice
	player_choice_number=name_to_number(player_choice)   #将用户的游戏选择对象转换为相应的整数
	comp_number=random.randrange(0,4)     #利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
	print("计算机的选择为：",number_to_name(comp_number))
	if comp_number == player_choice_number :  #判断用户选择是否和计算机一样
		print("您和计算机出的一样呢")
	elif abs(comp_number - player_choice_number) <= 2:   #如果用户与计算机选择之差绝对值小于2，那么大的赢
		if min(comp_number,player_choice_number)== comp_number:
			print("您赢了")
		else:
			print("机器赢了")
	elif abs(comp_number - player_choice_number) <= 4:   #如果用户与计算机选择之差绝对值大于2小于4，那么小的赢
		if max(comp_number,player_choice_number)== comp_number:
			print("您赢了")
		else:
			print("机器赢了")
	else:
		print("Error: No Correct Name")       #如果用户输入错误则报错
	    

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)


