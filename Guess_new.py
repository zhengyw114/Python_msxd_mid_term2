# -*- coding: utf-8 -*-
# 【项目二】高级猜数字
#
# 制作交互性强、容错率高的猜数字游戏程序。
#
# 要求：
#
# 为猜数字游戏增加记录玩家成绩的功能，包括玩家用户名、玩的次数和平均猜中的轮数等；
# 如果记录里没有玩家输入的用户名，就新建一条记录，否则在原有记录上更新数据；
# 对玩家输入做检测，判定输入的有效性，并保证程序不会因异常输入而出错；
# 将游戏打包为 exe 文件。
import random
gr = []
game_record = {}
#打开记录
def create_gamer():
    with open("record.txt") as f:
        l = f.readlines()
        for i in l:
            i.strip()
            gr = i.split()
            game_record[gr[0]] = gr[1:]  # 建立字典，第一列为键，其余为值

    exist_names = ";".join(game_record.keys())
    #输入玩家记录：
    global name
    name = input("请输入你的游戏名称，或选择已经存在的玩家名称（%s）" %exist_names)
    user = []
    try:
        if name in exist_names:
            user = [name,game_record[name]]
            print("你好%s，你已经玩了%d次游戏，共猜了%d轮，平均%.1f轮猜对，最少%d轮猜对"% (name,eval(user[1][0]),eval(user[1][1]),eval(user[1][1])/eval(user[1][0]),eval(user[1][2])))
        elif name not in exist_names:
            game_record[name] = [0,0,0]
            print("你好%s，这是你第一次玩游戏哦，加油吧！"% (name))
        global total_time,guess_time
        total_time = 0
        guess_time = 0
    except:
        print("请输入个名称试试")
        create_gamer()

#定义猜数字规则
def compare(num1,num2):
    print("你的第%d个答案是%d，结果" %(guess_time,ans))
    if num1 < num2:
        print("太小了")
        return False
    elif num1 > num2:
        print("太大了")
        return False
    else:
        print("你猜对啦!")
        return True

#定义游戏,本想用 while not True, return True or False的值来控制循环的，但是感觉很难控制两个的值的真假，所以还是改用笨办法，写的多了点
def guess_game():
    que = random.randint(1,100)
    global ans
    ans = 9999
    while ans != que:
        try:
            ans = int(input("请输入一个1-100的整数："))
            if ans <= 100 and ans >=1:
                global guess_time
                guess_time+=1
                compare(ans,que)
            else:
                print("你很调皮哦，这样不好，再来一次吧")
        except:
            print("你很调皮哦，这样不好，再来一次吧")

#记录游戏
def record_game():
    print("%s,你用了%d次猜出了答案" %(name,guess_time))
    global guess_time
    if guess_time < int(game_record[name][2]):
        min_time = guess_time
    elif int(game_record[name][2]) == 0:
        min_time = guess_time
    else:
        min_time = int(game_record[name][2])
    total_time = int(game_record[name][0])+1
    guess_time = guess_time + int(game_record[name][1])
    game_record[name]=[str(total_time),str(guess_time),str(min_time)]
    for i in game_record.keys():
        result = ""
        line = i + ' ' + ' '.join(game_record[i]) + '\n'
        result += line

    with open("record.txt","w") as f2:
        f2.write(result)

while True:
    select = input("这是一个猜数字的游戏，请选择：s.开始，e.退出")
    if select == "s":
        create_gamer()
        guess_game()
        record_game()

    elif select == "e":
        exit()
