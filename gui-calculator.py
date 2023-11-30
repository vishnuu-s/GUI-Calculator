from tkinter import *
import pickle 
import tkinter.messagebox
import random
import math
import numpy as np
import re
import datetime

try:
    f = open("log.dat")
    f.close()
except:
    f = open("log.dat",mode="wb")
    pickle.dump("Date\t\t\t\tTime\t\t\tExpression\n",f)
    f.close()


master = Tk()
master.title("Calculator")
master.resizable(False,False)
equation = StringVar()
expression = ""

root = Frame(master)
root.pack()

displaytextbox = Entry(root, textvariable=equation, bd=3)
displaytextbox.grid(row=0, column=1, columnspan=4, ipadx=30)

equation.set("")
displaytextbox.config(state="disabled")


def root_calculation():
    global expression, equation
    screen1 = Toplevel(root)
    screen1.title("Roots")
    screen1.geometry("250x150")
    screen1.grab_set()
    screen1.config(bg="#313975")
    screen1.resizable(0,0)

    def clear():
        screen1.grab_release()
        screen1.destroy()

    def answer1():
        global answer, expression, equation
        expression += str(answer)
        equation.set(expression)
        clear()

    def answer2():
        global answer, expression, equation
        answer = "-" + str(answer)
        expression += str(answer)
        equation.set(expression)
        clear()

    def answer_method():
        global expression, equation, answer
        value_of_n = eval(ntext.get())
        value_of_x = eval(xtext.get())
        answer = value_of_n ** (1 / value_of_x)
        with open("log.dat","ab") as f:
            pickle.dump("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+ntext.get()+" root "+xtext.get()),f)
        if value_of_x % 2 == 1:
            expression += str(answer)
            equation.set(expression)
            clear()
        elif value_of_x % 2 == 0:
            choice1.pack()
            choice2.pack()

    topiclabel = Label(screen1, text="Roots x√n", font="Roboto 16 bold",bg="#313975",fg='white')
    topiclabel.pack(pady=5)

    label1 = Label(screen1, text="Enter the value for x",bg="#535A92",fg='white')
    label1.place(x=15,y=40) 

    xtext = StringVar()
    xtextbox = Entry(screen1, textvariable=xtext, bd=5, width=14)
    xtextbox.place(x=135,y=38)

    label2 = Label(screen1, text="Enter the value for n",bg="#535A92",fg='white')
    label2.place(x=15,y=70)
    ntext = StringVar()
    ntextbox = Entry(screen1, textvariable=ntext, bd=5, width=14)
    ntextbox.place(x=135,y=68)

    calculate_root = Button(screen1, text='=',fg='white', bg="#181F58", command=answer_method, height=2, width=26)
    calculate_root.place(x=33,y=100)
    screen1.bind("<Return>",answer_method)

    choice1 = Button(screen1, text='+', fg='black', bg="#33cc00", command=answer1, height=1, width=7)
    choice2 = Button(screen1, text='-', fg='black', bg="#33cc00", command=answer2, height=1, width=7)


def randint():
    screen2 = Toplevel(root)
    screen2.title("RandInt")
    screen2.geometry('%dx%d+%d+%d' % (250,150,70,180))
    screen2.grab_set()
    screen2.config(bg="#313975")
    screen2.resizable(width=0,height=0)

    def clear():
        screen2.grab_release()
        screen2.destroy()

    def answer_method(event=None):
        global expression, equation
        try:
            value_of_n = eval(ntext.get())
            value_of_x = eval(xtext.get())
            value = random.randint(value_of_x, value_of_n)
            expression += str(value)
            with open("log.dat","ab") as f:
                pickle.dump("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+"randint("+ntext.get()+","+xtext.get()+")"),f)
            equation.set(expression)
            clear()
        except:
            tkinter.messagebox.showerror("RandInt", "Please enter correct values")

    topiclabel = Label(screen2, text="Random number generator", font="Roboto 12 bold",bg="#313975",fg='white')
    topiclabel.pack(pady=5)

    label1 = Label(screen2, text="Enter the start value",bg="#535A92",fg='white')
    label1.place(x=15,y=40) 

    xtext = StringVar()
    xtextbox = Entry(screen2, textvariable=xtext, bd=5, width=14)
    xtextbox.place(x=135,y=38)

    label2 = Label(screen2, text="Enter the stop value",bg="#535A92",fg='white')
    label2.place(x=15,y=70)
    ntext = StringVar()
    ntextbox = Entry(screen2, textvariable=ntext, bd=5,width=14)
    ntextbox.place(x=135,y=68)

    calculate_root = Button(screen2, text='GENERATE', fg='white', bg="#181F58", command=answer_method, height=2, width=26,)
    screen2.bind("<Return>",answer_method)
    calculate_root.place(x=33,y=100)


def hcf_method():
    screen3 = Toplevel(root)
    screen3.title("HCF")
    screen3.geometry("250x150")
    screen3.config(bg="#313975")
    screen3.grab_set()

    def method(event = None):
        global expression, equation
        try:
            value1 = int(xtext.get())
            value2 = int(ntext.get())
            answer = math.gcd(value1, value2)
            expression += str(answer)
            equation.set(expression)
            with open("log.dat","ab") as f:
                pickle.dump("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+"HCF("+ntext.get()+","+xtext.get()+")"),f)
            screen3.grab_release()
            screen3.destroy()
        except:
            tkinter.messagebox.showerror("HCF", "Please enter correct values")

    topiclabel = Label(screen3, text="HCF", font="Roboto 16 bold",bg="#313975",fg='white')
    topiclabel.pack(pady=5)

    label1 = Label(screen3, text="Enter num1: ",bg="#535A92",fg='white')
    label1.place(x=15,y=40)

    xtext = StringVar()
    xtextbox = Entry(screen3, textvariable=xtext, bd=5, width=14)
    xtextbox.place(x=135,y=38)

    label2 = Label(screen3, text="Enter num2: ",bg="#535A92",fg='white')
    label2.place(x=15,y=70)
    ntext = StringVar()
    ntextbox = Entry(screen3, textvariable=ntext, bd=5, width=14)
    ntextbox.place(x=135,y=68)

    calculate_root = Button(screen3, text='=',fg='white', bg="#181F58", command=method, height=2, width=26)
    screen3.bind('<Return>',method)
    calculate_root.place(x=33,y=100)


def lcm_method():
    screen4 = Toplevel(root)
    screen4.title("LCM")
    screen4.geometry("250x150")
    screen4.config(bg="#313975")
    screen4.grab_set()

    def method(event = None):
        global expression, equation
        try:
            value1 = int(xtext.get())
            value2 = int(ntext.get())
            answer = np.lcm(value1, value2)
            expression += str(answer)
            equation.set(expression)
            screen4.grab_release()
            screen4.destroy()
        except:
            tkinter.messagebox.showerror("LCM", "Both values need to be an integer")

    topiclabel = Label(screen4, text="LCM(x, n)", font="Roboto 16 bold",bg="#313975",fg='white')
    topiclabel.pack(pady=5)

    label1 = Label(screen4, text="Enter num1: ",bg="#535A92",fg='white')
    label1.place(x=15,y=40)

    xtext = StringVar()
    xtextbox = Entry(screen4, textvariable=xtext,bd=5, width=14)
    xtextbox.place(x=135,y=38)

    label2 = Label(screen4, text="Enter num2: ",bg="#535A92",fg='white')
    label2.place(x=15,y=70)

    ntext = StringVar()
    ntextbox = Entry(screen4, textvariable=ntext,bd=5, width=14)
    ntextbox.place(x=135,y=68)

    calculate_root = Button(screen4, text='=',fg='white', bg="#181F58", command=method, height=2, width=26)
    screen4.bind('<Return>',method)
    calculate_root.place(x=33,y=100)


def backspace(event=None):
    global expression, equation
    try:
        if expression[-1] != "D" and expression[-1] != "V":
            expression = expression[:-1]
            equation.set(expression)
        elif expression[-1] == "D":
            expression = expression.replace("MOD", "")
            equation.set(expression)
        else:
            expression = expression.replace("DIV", "")
            equation.set(expression)
    except:
        pass


def exponential_calculation():
    global expression
    expression = expression.replace("^", "**")
    with open("log.dat","ab") as f:
        pickle.dump("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+expression),f)


def modulus_calculation():
    global expression
    expression = expression.replace("MOD", "%")
    with open("log.dat","ab") as f:
            pickle.dump("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+expression),f)


def div_calculation():
    global expression
    expression = expression.replace("DIV", "//")
    with open("log.dat","ab") as f:
            pickle.dump("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+expression),f)


def pi():
    global expression
    expression = expression.replace("π", str(math.pi))
    with open("log.dat","ab") as f:
        pickle.dump("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+expression),f)


def sin():
    sin_window = Toplevel(root)
    sin_window.title("")
    sin_window.resizable(False, False)
    sin_window.grab_set()

    def sin_calculate_method():
        global expression, equation
        if str(deg_rad.get()) == "deg":
            try:
                sin_answer = math.sin(math.radians(eval(sin_expression.get())))
                sin_answer = round(sin_answer, 11)
                expression += str(sin_answer)
                equation.set(expression)
                with open("log.dat","ab") as f:
                    pickle.dump("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+"sin("+sin_expression.get()+")"),f)
                sin_window.grab_release()
                sin_window.destroy()
            except:
                tkinter.messagebox.showerror("sin()", "Invalid expression")
        else:
            try:
                sin_answer = math.sin(eval(sin_expression.get()))
                expression += str(sin_answer)
                equation.set(expression)
                with open("log.dat","ab") as f:
                    pickle.dump("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+"sin("+sin_expression.get()+")"),f)
                sin_window.grab_release()
                sin_window.destroy()
            except:
                tkinter.messagebox.showerror("sin()", "Invalid expression")

    options = ["deg", "rad"]
    deg_rad = StringVar()
    deg_rad.set("deg")

    sin_expression = StringVar()

    sin_format = Frame(sin_window)
    sin_format.pack()

    sin_label = Label(sin_format, text="sin(", font="Roboto 10 bold")
    sin_label.pack(side="left")
    sin_entry = Entry(sin_format, textvariable=sin_expression, bd=5)
    sin_entry.pack(side="left")
    sin_options = OptionMenu(sin_format, deg_rad, *options)
    sin_options.pack(side="left")
    sin_label = Label(sin_format, text=")", font="Roboto 10 bold")
    sin_label.pack(side="left")

    sin_calculate = Button(sin_window, text="=", fg='black', bg="#33cc00", command=sin_calculate_method, height=1,
                           width=8)
    sin_calculate.pack()
    sin_window.bind("<Return>",sin_calculate_method)


def cos():
    cos_window = Toplevel(root)
    cos_window.title("")
    cos_window.resizable(False, False)
    cos_window.grab_set()

    def cos_calculate_method():
        global expression, equation
        if str(deg_rad.get()) == "deg":
            try:
                cos_answer = math.cos(math.radians(eval(cos_expression.get())))
                cos_answer = round(cos_answer, 11)
                expression += str(cos_answer)
                equation.set(expression)
                with open("log.dat","ab") as f:
                    pickle.dump("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+"cos("+cos_expression.get()+")"),f)
                cos_window.grab_release()
                cos_window.destroy()
            except:
                tkinter.messagebox.showerror("cos()", "Invalid expression")
        else:
            try:
                cos_answer = math.cos(eval(cos_expression.get()))
                expression += str(cos_answer)
                equation.set(expression)
                with open("log.dat","ab") as f:
                    pickle.dump("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+"cos("+cos_expression.get()+")"),f)
                cos_window.grab_release()
                cos_window.destroy()
            except:
                tkinter.messagebox.showerror("cos()", "Invalid expression")

    options = ["deg", "rad"]
    deg_rad = StringVar()
    deg_rad.set("deg")

    cos_expression = StringVar()

    cos_format = Frame(cos_window)
    cos_format.pack()

    cos_label = Label(cos_format, text="cos(", font="Roboto 10 bold")
    cos_label.pack(side="left")
    cos_entry = Entry(cos_format, textvariable=cos_expression, bd=5)
    cos_entry.pack(side="left")
    cos_options = OptionMenu(cos_format, deg_rad, *options)
    cos_options.pack(side="left")
    cos_label = Label(cos_format, text=")", font="Roboto 10 bold")
    cos_label.pack(side="left")

    cos_calculate = Button(cos_window, text="=", fg='black', bg="#33cc00", command=cos_calculate_method, height=1,
                           width=8)
    cos_calculate.pack()
    cos_window.bind("<Return>",cos_calculate_method)


def tan():
    tan_window = Toplevel(root)
    tan_window.title("")
    tan_window.resizable(False, False)
    tan_window.grab_set()

    def tan_calculate_method():
        global expression, equation
        if str(deg_rad.get()) == "deg":
            try:
                tan_answer = math.tan(math.radians(eval(tan_expression.get())))
                tan_answer = round(tan_answer, 11)
                expression += str(tan_answer)
                equation.set(expression)
                with open("log.dat","ab") as f:
                    pickle.dump("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+"tan("+tan_expression.get()+")"),f)
                tan_window.grab_release()
                tan_window.destroy()
            except:
                tkinter.messagebox.showerror("tan()", "Invalid expression")
        else:
            try:
                tan_answer = math.tan(eval(tan_expression.get()))
                expression += str(tan_answer)
                equation.set(expression)
                with open("log.dat","ab") as f:
                    pickle.dump("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+"tan("+tan_expression.get()+")"),f)
                tan_window.grab_release()
                tan_window.destroy()
            except:
                tkinter.messagebox.showerror("tan()", "Invalid expression")

    options = ["deg", "rad"]
    deg_rad = StringVar()
    deg_rad.set("deg")

    tan_expression = StringVar()

    tan_format = Frame(tan_window)
    tan_format.pack()

    tan_label = Label(tan_format, text="tan(", font="Roboto 10 bold")
    tan_label.pack(side="left")
    tan_entry = Entry(tan_format, textvariable=tan_expression, bd=5)
    tan_entry.pack(side="left")
    tan_options = OptionMenu(tan_format, deg_rad, *options)
    tan_options.pack(side="left")
    tan_label = Label(tan_format, text=")", font="Roboto 10 bold")
    tan_label.pack(side="left")

    tan_calculate = Button(tan_window, text="=", fg='black', bg="#33cc00", command=tan_calculate_method, height=1,
                           width=8)
    tan_calculate.pack()
    tan_window.bind("<Return>",tan_calculate_method)


def log():
    log_window = Toplevel(root)
    log_window.title("log()")
    log_window.resizable(False, False)
    log_window.grab_set()

    def log_calculate_method():
        global expression, equation
        try:
            log_answer = math.log(eval(log_expression.get()), eval(log_base.get()))
            expression += str(log_answer)
            equation.set(expression)
            with open("log.dat","ab") as f:
                    pickle.dump("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+log_expression.get()+"log"+log_base.get()),f)
            log_window.grab_release()
            log_window.destroy()
        except:
            tkinter.messagebox.showerror("log()", "Invalid values")

    log_expression = StringVar()
    log_base = StringVar()

    log_label = Label(log_window, text="log(x, base)", font="Roboto 10 bold")
    log_label.pack()

    log_format = Frame(log_window)
    log_format.pack()

    log_label = Label(log_format, text="log(", font="Roboto 10 bold")
    log_label.pack(side="left")
    log_entry = Entry(log_format, textvariable=log_expression, bd=5)
    log_entry.pack(side="left")
    log_entry = Entry(log_format, textvariable=log_base, bd=5)
    log_entry.pack(side="left")
    log_label = Label(log_format, text=")", font="Roboto 10 bold")
    log_label.pack(side="left")

    log_calculate = Button(log_window, text="=", fg='black', bg="#33cc00", command=log_calculate_method, height=1,
                           width=8)
    log_calculate.pack()
    log_window.bind("<Return>",log_calculate_method)


def press(num):
    global expression

    if expression == "Please enter a value":
        expression = ""

    expression = expression + str(num)
    equation.set(expression)


def validate_leading_zeros(expression):
    x = re.split("+|-|*|/", expression)

    operators = []
    signs = "+-/*"

    for operator in expression:
        if operator in signs:
            operators.append(operator)

    print(x)
    print(operators)

    def getNumbers(str):
        array = re.findall(r'[0-9]+', str)
        return array

    for mini_exp in x:
        array = getNumbers(mini_exp)

        signs_2 = "%^/()"
        operators_2 = []

        for operator_2 in mini_exp:
            if operator_2 in signs_2:
                operators_2.append(operator_2)

        print(array)
        print(operators_2)

        new_array = []

        for number in array:
            new_array.append(number.lstrip("0"))

        print(new_array)

        sub_exp = []

        for item in operators_2:
            for item2 in new_array:
                sub_exp.append()


def equals(event=None):
    global expression, equation,historyvar

    try:
        global equation
        if "^" in expression:
            exponential_calculation()
        elif "MOD" in expression:
            modulus_calculation()
        elif "DIV" in expression:
            div_calculation()
        elif "π" in expression:
            pi()

        # if "0" in expression:
            # validate_leading_zeros(expression)

        with open("log.dat","ab") as f:
            pickle.dump("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+expression),f)

        answer = str(round(eval(expression), 10))
        equation.set(answer)
        expression = ""
    except:
        if expression == "":
            equation.set("Please enter a value")
        else:
            equation.set("Error")
            expression = ""


def clear(event=None):
    global expression
    expression = ""
    equation.set("")


# Buttons and labels

button1 = Button(root, text='1', fg='black', bg="#8A7BAF", command=lambda: press(1), width=8, height=2)
button1.grid(row=1, column=1)
master.bind('1',lambda event: press(1))
button2 = Button(root, text='2', fg='black', bg="#8A7BAF", command=lambda: press(2), width=8, height=2)
button2.grid(row=1, column=2)
master.bind('2',lambda event: press(2))

button3 = Button(root, text='3', fg='black', bg="#8A7BAF", command=lambda: press(3), width=8, height=2)
button3.grid(row=1, column=3)
master.bind('3',lambda event: press(3))

plus = Button(root, text='+', fg='black', bg="#6F5796", command=lambda: press("+"), height=2, width=8)
plus.grid(row=1, column=4)
master.bind('+',lambda event: press("+"))

####NewRow######

button4 = Button(root, text='4', fg='black', bg="#8A7BAF", command=lambda: press(4), width=8, height=2)
button4.grid(row=2, column=1)
master.bind('4',lambda event: press(4))

button5 = Button(root, text='5', fg='black', bg="#8A7BAF", command=lambda: press(5), width=8, height=2)
button5.grid(row=2, column=2)
master.bind('5',lambda event: press(5))

button6 = Button(root, text='6', fg='black', bg="#8A7BAF", command=lambda: press(6), width=8, height=2)
button6.grid(row=2, column=3)
master.bind('6',lambda event: press(6))

minus = Button(root, text='-', fg='black', bg="#6F5796", command=lambda: press("-"), height=2, width=8)
minus.grid(row=2, column=4)
master.bind('-',lambda event: press("-"))

####NewRow######

button7 = Button(root, text='7', fg='black', bg="#8A7BAF", command=lambda: press(7), width=8, height=2)
button7.grid(row=3, column=1)
master.bind('7',lambda event: press(7))

button8 = Button(root, text='8', fg='black', bg="#8A7BAF", command=lambda: press(8), width=8, height=2)
button8.grid(row=3, column=2)
master.bind('8',lambda event: press(8))

button9 = Button(root, text='9', fg='black', bg="#8A7BAF", command=lambda: press(9), width=8, height=2)
button9.grid(row=3, column=3)
master.bind('9',lambda event: press(9))

multiply = Button(root, text='X', fg='black', bg="#6F5796", command=lambda: press("*"), height=2, width=8)
multiply.grid(row=3, column=4)
master.bind('*',lambda event: press("*"))

####NewRow######

exponential = Button(root, text="^", fg='black', bg='#8A7BAF', command=lambda: press("^"), height=2, width=8)
exponential.grid(row=4, column=3)
master.bind('^',lambda event: press("^"))

button0 = Button(root, text='0', fg='black', bg="#8A7BAF", command=lambda: press(0), width=8, height=2)
button0.grid(row=4, column=2)
master.bind('0',lambda event: press(0))

decimal = Button(root, text='.', fg='black', bg="#8A7BAF", command=lambda: press('.'), width=8, height=2)
decimal.grid(row=4, column=1)
master.bind('.',lambda event: press("."))

divide = Button(root, text='/', fg='black', bg="#6F5796", command=lambda: press("/"), height=2, width=8)
divide.grid(row=4, column=4)
master.bind('/',lambda event: press("/"))

####NewRow######

hcf = Button(root, text="HCF", fg='black', bg='#6F5796', height=2, width=8, command=hcf_method)
hcf.grid(row=5, column=1)

modulus = Button(root, text="MOD", fg='black', bg='#6F5796', command=lambda: press("MOD"), height=2, width=8)
modulus.grid(row=5, column=2)

div = Button(root, text="DIV", fg='black', bg='#6F5796', command=lambda: press("DIV"), height=2, width=8)
div.grid(row=5, column=3)

mathroots = Button(root, text="√", fg='black', bg='#6F5796', command=root_calculation, height=2, width=8)
mathroots.grid(row=5, column=4)

####NewRow######

lcm = Button(root, text="LCM", fg='black', bg='#6F5796', height=2, width=8, command=lcm_method)
lcm.grid(row=6, column=1)

leftbracket = Button(root, text="(", fg='black', bg='#6F5796', command=lambda: press("("), height=2, width=8)
leftbracket.grid(row=6, column=3)
master.bind("(",lambda event: press("("))

rightbracket = Button(root, text=")", fg='black', bg='#6F5796', command=lambda: press(")"), height=2, width=8)
rightbracket.grid(row=6, column=4)
master.bind(")",lambda event: press(")"))

rand_int = Button(root, text="RandInt", fg='black', bg='#6F5796', height=2, width=8, command=randint)
rand_int.grid(row=6, column=2)

# New Row

sin_button = Button(root, text="sin()", fg='black', bg='#F7CAC9', height=2, width=8, command=sin)
sin_button.grid(row=7, column=1)

cos_button = Button(root, text="cos()", fg='black', bg='#F7CAC9', height=2, width=8, command=cos)
cos_button.grid(row=7, column=2)

tan_button = Button(root, text="tan()", fg='black', bg='#F7CAC9', height=2, width=8, command=tan)
tan_button.grid(row=7, column=3)

log_button = Button(root, text="log()", fg='black', bg='#F7CAC9', height=2, width=8, command=log)
log_button.grid(row=7, column=4)

####NewRow######

delete = Button(root, text='AC', fg='black', bg="#e03a3a", command=clear, width=8, height=2)
delete.grid(row=8, column=1)
master.bind("<Escape>",clear)

backspace_button = Button(root, text='DEL', fg='black', bg="#e03a3a", command=backspace, width=8, height=2)
backspace_button.grid(row=8, column=2)
master.bind('<BackSpace>',backspace)

pi_button = Button(root, text="π", fg='black', bg='#ebb734', command=lambda: press("π"), height=2, width=8)
pi_button.grid(row=8, column=3)

equal = Button(root, text='=', fg='black', bg="#33cc00", command=equals, height=2, width=8)
equal.grid(row=8, column=4)
master.bind("<Return>",equals)

print("Calculator is up and running. Enjoy.")
master.mainloop()
print("Calculator closed.")