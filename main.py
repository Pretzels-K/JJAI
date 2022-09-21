import turtle as t
import time
import random
import tkinter
from tkinter import Tk, Canvas

def clicked1():
    t.clear()
    scr.clear()
    modeOption()

def clicked2():
    t.bye()

def reStop():
    t.clear()
    scr.clear()
    scr.bgcolor('black')
    t.ht()
    t.up()
    t.goto(0,50)
    t.pencolor('white')
    t.write('Press R to regame', False, 'center', ('Consolas', 50))
    t.goto(0,-50)
    t.write('Press Q to quit', False, 'center', ('Consolas', 50))

    scr.onkey(clicked1, 'r')
    scr.onkey(clicked2, 'q')
    scr.listen()

def comPare():
    user_input_str = []
    user_input = t.textinput('숫자 기억 게임', f'기억한 숫자 {num_times}개를 입력하세요.\nex)1 2 3')
    user_input_str = user_input.split(' ')
    user_input_str.sort()
    user_input_int = list(map(int, user_input_str))  # 문자열 리스트 정수형 리스트로 변환

    image1 = 'C:\worng3.jfif'

    if user_input_int == num:
        scr.bgpic('correct.gif')  # 이미지 파일 배경화면으로 설정
        scr.update()
        time.sleep(2)
    else:
        scr.bgpic('wrong.gif')
        t.goto(0, -200)
        t.write(f'정답은 {num}입니다', False, 'center', ('Consolas', 30))
        t.goto(0, -250)
        t.write(f'입력하신 수는 {user_input}입니다', False, 'center', ('', 30))
        time.sleep(3)

    reStop()

def onClick(x,y):
    t.clear()
    modeOption()

def easyMode():
    global num_times
    num_times = int(t.textinput('숫자 기억 게임', '몇 개의 숫자로 진행하시겠습니까?'))
    t.clear()
    scr.bgpic('effect.gif')
    scr.bgcolor('black')

    global num
    num = []
    for x in range(num_times):
        rand_num = random.randint(1, 100)
        t.pencolor('white')
        t.goto(0, -40)
        t.write(rand_num, False, 'center', ('Consolas', 70))
        # print(rand_num)
        num.append(rand_num)
        time.sleep(3)
        t.clear()
    num.sort()

    comPare()

def normalMode():
    global num_times
    num_times = int(t.textinput('숫자 기억 게임', '몇 개의 숫자로 진행하시겠습니까?'))

    t.clear()
    scr.bgpic('effect.gif')
    scr.bgcolor('black')

    global num
    num = []
    for x in range(num_times):
        rand_num = random.randint(1, 100)
        t.pencolor('white')
        t.goto(0, -40)
        t.write(rand_num, False, 'center', ('Consolas', 70))
        # print(rand_num)
        num.append(rand_num)
        time.sleep(1)
        t.clear()
    num.sort()

    comPare()

def hardMode():
    global num_times
    num_times = int(t.textinput('숫자 기억 게임', '몇 개의 숫자로 진행하시겠습니까?'))

    t.clear()
    scr.bgpic('effect.gif')
    scr.bgcolor('black')

    global num
    num = []
    for x in range(num_times):
        rand_num = random.randint(1, 100)
        t.pencolor('white')
        xRand = random.randint(-300, 300)
        yRand = random.randint(-300, 300)
        print(xRand, yRand)
        t.goto(xRand, yRand)
        t.write(rand_num, False, 'center', ('Consolas', 70))
        num.append(rand_num)
        time.sleep(0.5)
        t.clear()
    num.sort()

    comPare()

def modeOption():
    t.clear()
    scr.clear()
    scr.bgcolor('black')
    t.ht()
    t.up()
    t.pencolor('white')

    t.goto(0,100)
    t.write('Easy - Press E', False, 'center', ('Consolas', 30))
    t.goto(0,0)
    t.write('Normal - Press N', False, 'center', ('Consolas', 30))
    t.goto(0,-100)
    t.write('Hard - Press H', False, 'center', ('Consolas', 30))

    scr.onkey(easyMode, 'e')
    scr.onkey(normalMode, 'n')
    scr.onkey(hardMode, 'h')
    scr.listen()

def main():
    t.title('Number Game')
    t.ht()  # hide turtle : turtle 숨기기
    t.up()  # pen up : 이동할 때 그림 안 그려지게끔

    global scr
    scr = t.Screen()
    scr.bgpic('effect.gif')
    scr.bgcolor('black')

    t.pencolor('white')
    t.write('Game Start', False, 'center', ('Consolas', 50))
    t.goto(0, -100)
    t.write('Click to Start', False, 'center', ('Consolas', 20))
    t.goto(0, 0)
    for i in range(2):
        t.clear()
        t.write('Game Start', False, 'center', ('Consolas', 50))
        time.sleep(1)
        t.goto(0,-100)
        t.write('Click to Start', False, 'center', ('Consolas', 20))
        t.goto(0, 0)
        time.sleep(1)

    scr.onclick(onClick)
    scr.mainloop()

if __name__ == '__main__':
    main()