#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：李健峰
日期：2021年11月25日
"""
import random
comp_number=random.randrange(0,5)
# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀
def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="石头":
        player_choice_number=int(0)
        return player_choice_number
    if name=="史波克":
        player_choice_number=int(1)
        return player_choice_number
    if name=="纸":
        player_choice_number=int(2)
        return player_choice_number
    if name=="蜥蜴":
        player_choice_number=int(3)
        return player_choice_number
    if name=="剪刀":
        player_choice_number=int(4)
        return player_choice_number
def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        comp_name="石头"
        return comp_name
    if number==1:
        comp_name="史波克"
        return comp_name
    if number==2:
        comp_name="纸"
        return comp_name
    if number==3:
        comp_name="蜥蜴"
        return comp_name
    if number==4:
        comp_name="剪刀"
        return comp_name
def rpsls(player_choice_number):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    if player_choice_number!=comp_number:
        if (player_choice_number==0 and (comp_number==4 or comp_number==3)) or (player_choice_number==1 and (comp_number==0 or comp_number==4)) or (player_choice_number==2 and (comp_number==1 or comp_number==0)) or (player_choice_number==3 and (comp_number==1 or comp_number==2)) or (player_choice_number==4 and (comp_number==2 or comp_number==3)):
            result="您赢了！"
            return result
        else:
            result="机器赢了"
            return result
    else:
        result="您和计算机出得一样呢"
        return result
    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
    # 在屏幕上显示计算机选择的随机对象
    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”
# 对程序进行测试
print("请输入您的选择:")
choice_name=input()
if choice_name=="石头" or choice_name=="剪刀" or choice_name=="纸" or choice_name=="史波克" or choice_name=="蜥蜴":
    print("----------")
    print("您的选择为：%s"%choice_name)
    comp_name=number_to_name(comp_number)
    print("机器人的选择为：%s"%comp_name)
    player_choice_number=name_to_number(choice_name)
    print(rpsls(player_choice_number))
else:
    print("Error: No Correct Name")


