#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2020/4/8
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
	"""
	����Ϸ�����Ӧ����ͬ������
	"""
	if name == str('ʯͷ'):
		number = 0
		return number
	elif name == str('ʷ����'):
		number = 1
		return number
	elif name == str("ֽ"):
		number=2
		return number
	elif name == str("����"):
		number=3
		return number
	elif name == str("����"):
		number=4
		return number	
	else:
		number=520
		return number



def number_to_name(number):
	"""
	������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
	"""
	if number==0:
		name=str("ʯͷ")
		return name
	elif number==1:
		name=str("ʷ����")
		return name
	elif number==2:
		name=str("ֽ")
		return name
	elif number==3:
		name=str("����")
		return name
	else:
		name=str("����")
		return name
    


def rpsls(player_choice):
	"""
	�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

	"""
	print("-------- ")
	print("����ѡ��Ϊ��",choice_name)
	player_choice=choice_name        #���Լ�����Ϸѡ�����������player_choice
	player_choice_number=name_to_number(player_choice)   #���û�����Ϸѡ�����ת��Ϊ��Ӧ������
	comp_number=random.randrange(0,4)     #����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
	print("�������ѡ��Ϊ��",number_to_name(comp_number))
	if comp_number == player_choice_number :  #�ж��û�ѡ���Ƿ�ͼ����һ��
		print("���ͼ��������һ����")
	elif abs(comp_number - player_choice_number) <= 2:   #����û�������ѡ��֮�����ֵС��2����ô���Ӯ
		if min(comp_number,player_choice_number)== comp_number:
			print("��Ӯ��")
		else:
			print("����Ӯ��")
	elif abs(comp_number - player_choice_number) <= 4:   #����û�������ѡ��֮�����ֵ����2С��4����ôС��Ӯ
		if max(comp_number,player_choice_number)== comp_number:
			print("��Ӯ��")
		else:
			print("����Ӯ��")
	else:
		print("Error: No Correct Name")       #����û���������򱨴�
	    

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


