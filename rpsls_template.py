#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ����
���ڣ�2021��11��25��
"""
import random
comp_number=random.randrange(0,5)
# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����
def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
        player_choice_number=int(0)
        return player_choice_number
    if name=="ʷ����":
        player_choice_number=int(1)
        return player_choice_number
    if name=="ֽ":
        player_choice_number=int(2)
        return player_choice_number
    if name=="����":
        player_choice_number=int(3)
        return player_choice_number
    if name=="����":
        player_choice_number=int(4)
        return player_choice_number
def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        comp_name="ʯͷ"
        return comp_name
    if number==1:
        comp_name="ʷ����"
        return comp_name
    if number==2:
        comp_name="ֽ"
        return comp_name
    if number==3:
        comp_name="����"
        return comp_name
    if number==4:
        comp_name="����"
        return comp_name
def rpsls(player_choice_number):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    if player_choice_number!=comp_number:
        if (player_choice_number==0 and (comp_number==4 or comp_number==3)) or (player_choice_number==1 and (comp_number==0 or comp_number==4)) or (player_choice_number==2 and (comp_number==1 or comp_number==0)) or (player_choice_number==3 and (comp_number==1 or comp_number==2)) or (player_choice_number==4 and (comp_number==2 or comp_number==3)):
            result="��Ӯ�ˣ�"
            return result
        else:
            result="����Ӯ��"
            return result
    else:
        result="���ͼ��������һ����"
        return result
    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
    # ����Ļ����ʾ�����ѡ����������
    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
# �Գ�����в���
print("����������ѡ��:")
choice_name=input()
if choice_name=="ʯͷ" or choice_name=="����" or choice_name=="ֽ" or choice_name=="ʷ����" or choice_name=="����":
    print("----------")
    print("����ѡ��Ϊ��%s"%choice_name)
    comp_name=number_to_name(comp_number)
    print("�����˵�ѡ��Ϊ��%s"%comp_name)
    player_choice_number=name_to_number(choice_name)
    print(rpsls(player_choice_number))
else:
    print("Error: No Correct Name")


