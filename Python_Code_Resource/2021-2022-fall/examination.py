# 此文件为模拟考试系统，一题10分，共10题，100分满分，90分及格，低于90取消资格
from time import sleep  # 引入睡眠模块，用于倒计时，1s/次
import openpyxl  # 引入openpyxl模块，可以控制excel文件

book = openpyxl.load_workbook('test.xlsx')  # 给book定一个标签，让他的背后功能是"读取工作簿"
sheet = book.active  # 激活这个工作簿

FullScore = 100  # 满分是100

print('欢迎使用模拟考试系统')


def authentication():  # 身份验证功能
    for i in range(3):
        name = str(input("请输入用户名："))
        password = str(input("请输入密码："))
        if name == "hangzhou" and password == "123456":
            print("登录成功")
            break
        else:
            print("登录失败")
            print("你还有%d次机会登录" % (2-i))
    else:
        print("登录失败，请于120S后再次登录")


def score():  # 扣分功能
    global FullScore
    if Answer != CorrectAnswer:
        print('答案错误，正确答案是%s' % (CorrectAnswer))
        FullScore -= 10
    else:
        print('恭喜您，答对了！')
        pass
    print('当前分数为%d' % (FullScore))
    if FullScore < 90:  # 当成绩低于90的时候，就显示成绩不合格
        print('成绩不合格')


def Topic():
    for cell in sheet:
        print(cell)


authentication()
print('第一道题')
sleep(1)
Topic()
print('1+1=？')
Answer = input('请输入你的答案')
CorrectAnswer = '2'
score()
