import tkinter
from tkinter import *
import tkinter.font

window = Tk()
window.geometry("320x470")
window.title("Tic Tac Toe")
window.config(bg="#EAEEF6")

startclicked = False
count = 0
var = ''


def start():
    global startclicked
    button7['text'] = 'X'
    startclicked = True


def reset():
    global startclicked, count
    button1['text'] = ""
    button2['text'] = ""
    button3['text'] = ""
    button4['text'] = ""
    button5['text'] = ""
    button6['text'] = ""
    button7['text'] = ""
    button8['text'] = ""
    button9['text'] = ""
    result['text'] = ""
    startclicked = False
    count = 0


def unbeatable(button, value):
    global startclicked, count, var
    if button['text'] == "" and startclicked == True:
        button['text'] = 'O'
        count = count + 1
        if count == 1:
            if value == 8:
                middleadjacent8()
                var = '8'
            elif value == 4:
                middleadjacent4()
                var = '4'
            elif value == 1:
                corner1()
                var = '1'
            elif value == 9:
                corner9()
                var = '9'
            elif value == 2:
                middleaway2()
                var = '2'
            elif value == 6:
                middleaway6()
                var = '6'
            elif value == 5:
                button3['text'] = 'X'
                var = '5'
            elif value == 3:
                oppocorner()
                var = '3'

        elif count == 2:
            if var == '5':
                if value == 1:
                    center_corner()
                    var = '5_1'
                elif value == 9:
                    center_corner()
                    var = '5_9'
                elif value == 2:
                    center_middle2()
                    var = '5_2'
                elif value == 6:
                    center_middle6()
                    var = '5_6'
                elif value == 8:
                    center_middle8()
                    var = '5_8'
                elif value == 4:
                    center_middle4()
                    var = '5_4'
            else:
                if var == '8':
                    middleadjacent8()
                elif var == '4':
                    middleadjacent4()
                elif var == '1':
                    corner1()
                elif var == '9':
                    corner9()
                elif var == '2':
                    middleaway2()
                elif var == '6':
                    middleaway6()
                elif var == '3':
                    oppocorner()


        else:
            if var == '8':
                middleadjacent8()
            elif var == '4':
                middleadjacent4()
            elif var == '1':
                corner1()
            elif var == '9':
                corner9()
            elif var == '2':
                middleaway2()
            elif var == '6':
                middleaway6()
            elif var == '5_1':
                center_corner()
            elif var == '5_9':
                center_corner()
            elif var == '5_2':
                center_middle2()
            elif var == '5_4':
                center_middle4()
            elif var == '5_6':
                center_middle6()
            elif var == '5_8':
                center_middle8()
            elif var == '3':
                oppocorner()


def middleadjacent8():
    if button8['text'] == 'O':
        button1['text'] = 'X'
        if button4['text'] == 'O':
            button3['text'] = 'X'
            if button2['text'] == 'O':
                button5['text'] = 'X'
                result.config(text='Better Luck Next Time')
            elif button5['text'] == 'O' or button6['text'] == 'O' or button9['text'] == 'O':
                button2['text'] = 'X'
                result.config(text='Better Luck Next Time')
        else:
            x = [button2, button3, button5, button6, button9]
            for i in range(5):
                if x[i]['text'] == 'O':
                    button4['text'] = 'X'
                    result.config(text='Better Luck Next Time')


def middleadjacent4():
    if button4['text'] == 'O':
        button9['text'] = 'X'
        if button8['text'] == 'O':
            button3['text'] = 'X'
            if button6['text'] == 'O':
                button5['text'] = 'X'
                result.config(text='Better Luck Next Time')
            elif button5['text'] == 'O' or button1['text'] == 'O' or button2['text'] == 'O':
                button6['text'] = 'X'
                result.config(text='Better Luck Next Time')
        else:
            x = [button2, button3, button5, button6, button1]
            for i in range(5):
                if x[i]['text'] == 'O':
                    button8['text'] = 'X'
                    result.config(text='Better Luck Next Time')


def corner9():
    if button9['text'] == 'O':
        button1['text'] = 'X'
        if button4['text'] == 'O':
            button3['text'] = 'X'
            if button2['text'] == 'O':
                button5['text'] = 'X'
                result.config(text='Better Luck Next Time')
            elif button5['text'] == 'O' or button6['text'] == 'O' or button8['text'] == 'O':
                button2['text'] = 'X'
                result.config(text='Better Luck Next Time')
        else:
            x = [button2, button3, button5, button6, button8]
            for i in range(5):
                if x[i]['text'] == 'O':
                    button4['text'] = 'X'
                    result.config(text='Better Luck Next Time')


def corner1():
    if button1['text'] == 'O':
        button9['text'] = 'X'
        if button8['text'] == 'O':
            button3['text'] = 'X'
            if button6['text'] == 'O':
                button5['text'] = 'X'
                result.config(text='Better Luck Next Time')
            elif button5['text'] == 'O' or button4['text'] == 'O' or button2['text'] == 'O':
                button6['text'] = 'X'
                result.config(text='Better Luck Next Time')
        else:
            x = [button2, button3, button5, button6, button4]
            for i in range(5):
                if x[i]['text'] == 'O':
                    button8['text'] = 'X'
                    result.config(text='Better Luck Next Time')


def middleaway6():
    if button6['text'] == 'O':
        button9['text'] = 'X'
        if button8['text'] == 'O':
            button1['text'] = 'X'
            if button4['text'] == 'O':
                button5['text'] = 'X'
                result.config(text='Better Luck Next Time')
            elif button5['text'] == 'O' or button2['text'] == 'O' or button3['text'] == 'O':
                button4['text'] = 'X'
                result.config(text='Better Luck Next Time')
        else:
            x = [button1, button2, button3, button4, button5]
            for i in range(5):
                if x[i]['text'] == 'O':
                    button8['text'] = 'X'
                    result.config(text='Better Luck Next Time')


def middleaway2():
    if button2['text'] == 'O':
        button1['text'] = 'X'
        if button4['text'] == 'O':
            button9['text'] = 'X'
            if button8['text'] == 'O':
                button5['text'] = 'X'
                result.config(text='Better Luck Next Time')
            elif button5['text'] == 'O' or button3['text'] == 'O' or button6['text'] == 'O':
                button8['text'] = 'X'
                result.config(text='Better Luck Next Time')
        else:
            x = [button3, button5, button6, button8, button9]
            for i in range(5):
                if x[i]['text'] == 'O':
                    button4['text'] = 'X'
                    result.config(text='Better Luck Next Time')


def center_corner():
    if button5['text'] == 'O':
        button3['text'] = 'X'
        if button1['text'] == 'O':
            button9['text'] = 'X'
            if button6['text'] == 'O':
                button8['text'] = 'X'
                result.config(text='Better Luck Next Time!')
            elif button8['text'] == 'O' or button2['text'] == 'O' or button4['text'] == 'O':
                button6['text'] = 'X'
                result.config(text='Better Luck Next Time!')
        else:
            if button9['text'] == 'O':
                button1['text'] = 'X'
                if button2['text'] == 'O':
                    button4['text'] = 'X'
                    result.config(text='Better Luck Next Time!')
                elif button4['text'] == 'O' or button6['text'] == 'O' or button8['text'] == 'O':
                    button2['text'] = 'X'
                    result.config(text='Better Luck Next Time!')


def center_middle4():
    if button5['text'] == 'O':
        button3['text'] = 'X'
        if button4['text'] == 'O':
            button6['text'] = 'X'
            if button9['text'] == 'O':
                button1['text'] = 'X'
                if button2['text'] == 'O':
                    button8['text'] = 'X'
                    result.config(text="           Draw")
                elif button8['text'] == 'O':
                    button2['text'] = 'X'
                    result.config(text='Better Luck Next Time!')
            elif button1['text'] == 'O' or button2['text'] == 'O' or button8['text'] == 'O':
                button9['text'] = 'X'
                result.config(text='Better Luck Next Time!')


def center_middle2():
    if button5['text'] == 'O':
        button3['text'] = 'X'
        if button2['text'] == 'O':
            button8['text'] = 'X'
            if button9['text'] == 'O':
                button1['text'] = 'X'
                if button4['text'] == 'O':
                    button6['text'] = 'X'
                    result.config(text='           Draw')
                elif button6['text'] == 'O':
                    button4['text'] = 'X'
                    result.config(text='Better Luck Next Time!')
            elif button1['text'] == 'O' or button4['text'] == 'O' or button6['text'] == 'O':
                button9['text'] = 'X'
                result.config(text='Better Luck Next Time!')


def center_middle6():
    if button5['text'] == 'O':
        button3['text'] = 'X'
        if button6['text'] == 'O':
            button4['text'] = 'X'
            if button1['text'] == 'O':
                button9['text'] = 'X'
                if button8['text'] == 'O':
                    button2['text'] = 'X'
                    result.config(text='           Draw')
                elif button2['text'] == 'O':
                    button8['text'] = 'X'
                    result.config(text='Better Luck Next Time!')
            elif button2['text'] == 'O' or button8['text'] == 'O' or button9['text'] == 'O':
                button1['text'] = 'X'
                result.config(text='           Draw')


def center_middle8():
    if button5['text'] == 'O':
        button3['text'] = 'X'
        if button8['text'] == 'O':
            button2['text'] = 'X'
            if button1['text'] == 'O':
                button9['text'] = 'X'
                if button6['text'] == 'O':
                    button4['text'] = 'X'
                    result.config(text='           Draw')
                elif button4['text'] == 'O':
                    button6['text'] = 'X'
                    result.config(text='Better Luck Next Time!')
            elif button4['text'] == 'O' or button6['text'] == 'O' or button9['text'] == 'O':
                button1['text'] = 'X'
                result.config(text='Better Luck Next Time!')


def oppocorner():
    if button3['text'] == 'O':
        button1['text'] = 'X'
        if button4['text'] == 'O':
            button9['text'] = 'X'
            if button5['text'] == 'O':
                button8['text'] = 'X'
                result.config(text='Better Luck Next Time')
            elif button8['text'] == 'O' or button2['text'] == 'O' or button6['text'] == 'O':
                button5['text'] = 'X'
                result.config(text='Better Luck Next Time')
        else:
            x = [button2, button8, button5, button6, button9]
            for i in range(5):
                if x[i]['text'] == 'O':
                    button4['text'] = 'X'
                    result.config(text='Better Luck Next Time')


titlefont = tkinter.font.Font(family="Times", size=20)
resultfont = tkinter.font.Font(family="Times", size=18)

label1 = Label(window, bg="#EAEEF6", text='Tic Tac Toe', font=titlefont, fg='#1C3870')
label1.place(x=90, y=15)

button1 = Button(window, bg="#7696E5", width=6, height=3, command=lambda: unbeatable(button1, 1))
button1.place(x=70, y=70)

button2 = Button(window, bg="#7696E5", width=6, height=3, command=lambda: unbeatable(button2, 2))
button2.place(x=130, y=70)

button3 = Button(window, bg="#7696E5", width=6, height=3, command=lambda: unbeatable(button3, 3))
button3.place(x=190, y=70)

button4 = Button(window, bg="#7696E5", width=6, height=3, command=lambda: unbeatable(button4, 4))
button4.place(x=70, y=135)

button5 = Button(window, bg="#7696E5", width=6, height=3, command=lambda: unbeatable(button5, 5))
button5.place(x=130, y=135)

button6 = Button(window, bg="#7696E5", width=6, height=3, command=lambda: unbeatable(button6, 6))
button6.place(x=190, y=135)

button7 = Button(window, bg="#7696E5", width=6, height=3, command=lambda: unbeatable(button7, 7))
button7.place(x=70, y=200)

button8 = Button(window, bg="#7696E5", width=6, height=3, command=lambda: unbeatable(button8, 8))
button8.place(x=130, y=200)

button9 = Button(window, bg="#7696E5", width=6, height=3, command=lambda: unbeatable(button9, 9))
button9.place(x=190, y=200)

buttonstart = Button(window, bg="#7696E5", width=7, height=2, text="Start", fg='#072052', command=start, font=12)
buttonstart.place(x=60, y=300)

buttonreset = Button(window, bg="#7696E5", width=7, height=2, text="Reset", fg='#072052', command=reset, font=12)
buttonreset.place(x=160, y=300)

result = Label(window, bg="#EAEEF6", font=resultfont, fg='#1C3870', )
result.place(x=50, y=410)

window.mainloop()