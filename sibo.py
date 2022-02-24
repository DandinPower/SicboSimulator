import tkinter as tk
import random


def be():
    global total
    global result
    totalnum = 0
    newresult = []
    for i in range(3):
        newresult.append(random.randrange(1, 7, 1))  # 骰3個骰子
    total = 0
    for i in range(3):
        total += newresult[i]
    result = newresult
    check = 0
    if result[0] == result[1] == result[2]:
        check = 1
    if(check == 1):
        return 0  # 莊家通吃
    elif(total >= 4 and total <= 10):
        return 1  # 開小
    elif(total <= 17 and total >= 11):
        return 2  # 開大


def adding():
    global principal
    stakein = staketofloat(add_entry.get())
    principal += stakein
    principal_label.config(text="本金還剩:%.2f" % (principal))


def staketofloat(inputin):
    if inputin == '':
        return 0
    else:
        return float(inputin)


def beting():
    global principal
    global result
    global total
    stake_little = staketofloat(stake_little_en.get())
    stake_big = staketofloat(stake_big_en.get())
    if principal < stake_big:
        result_label.config(text="請增加籌碼")
        return 0
    principal -= stake_big
    if principal < stake_little:
        result_label.config(text="請增加籌碼")
        return 0
    principal -= stake_little
    profit_check = 0
    profit_check = be()
    if profit_check == 0:
        result_label.config(text="莊家通殺,開%d-%d-%d" %
                            (result[0], result[1], result[2]))
    elif profit_check == 1:
        principal += 2*stake_little
        result_label.config(text="開小,開%d,開%d-%d-%d" %
                            (total, result[0], result[1], result[2]))
    elif profit_check == 2:
        principal += 2*stake_big
        result_label.config(text="開大,開%d,開%d-%d-%d" %
                            (total, result[0], result[1], result[2]))
    principal_label.config(text="本金還剩:%.2f" % (principal))


result = [3]
total = 0
principal = 0
window = tk.Tk()
window.title("SIBO APP")
window.geometry('800x600')
window.minsize(width=800, height=600)
window.maxsize(width=1024, height=768)
window.configure(background='white')
window.iconbitmap('image/icon.ico')
window.config(bg="#323232")
header_label = tk.Label(text="骰寶模擬")
header_label.config(fg="skyblue")
header_label.config(bg="#323232")
header_label.config(font="微軟正黑體 15")
header_label.pack(side=tk.TOP)

little_label = tk.Label(text="SMALL 4~10", fg="white",
                        bg="#323232", font="微軟正黑體 12")
little_label.pack(anchor=tk.NW, side=tk.LEFT)
stake_little_en = tk.Entry(font="微軟正黑體 12")
stake_little_en.pack(anchor=tk.NW, side=tk.LEFT)

big_label = tk.Label(text="BIG 11~17", fg="white",
                     bg="#323232", font="微軟正黑體 12")
big_label.pack(anchor=tk.NE, side=tk.RIGHT)
stake_big_en = tk.Entry(font="微軟正黑體 12")
stake_big_en.pack(anchor=tk.NE, side=tk.RIGHT)


principal_label = tk.Label(text="本金還剩:", fg="white", bg="#323232")
principal_label.pack(side=tk.TOP)
result_label = tk.Label(text="開出:", fg="white", bg="#323232")
result_label.pack(side=tk.TOP)


add_entry = tk.Entry()
add_entry.pack(side=tk.TOP)
add = tk.Button(text="增加籌碼")

add.config(command=adding)
add.pack(side=tk.TOP)

bet = tk.Button(text="開骰")
bet.config(width=10, height=5)
bet.config(command=beting)
bet.pack(side=tk.TOP)

window.mainloop()
