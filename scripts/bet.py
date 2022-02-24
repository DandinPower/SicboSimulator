import random


def bet(input):
    check = random.randrange(1, 10000, 1)
    if(1 <= check and check <= 4900):
        return 2*input
    else:
        return 0


def artificial():
    while(1):
        principal = int(input("請輸入本金"))
        while(principal != 0):
            stake = int(input("請輸入下注額"))
            if (principal < stake):
                print("本金不夠了")
                bool = input("是否增加本金?(Y/N)")
                if(bool == "Y"):
                    add = int(input("輸入增加的本金"))
                    principal += add
                elif(bool == "N"):
                    print("繼續遊玩")
                else:
                    print("輸入錯誤")
                continue
            principal -= stake
            profit = bet(stake)
            principal += profit
            print("賺了%d,本金還有%d" % (profit, principal))
        print("沒本金囉")
        bool = input("是否繼續玩(Y/N)")
        if(bool == "Y"):
            continue
        elif(bool == "N"):
            break
        else:
            print("輸入錯誤")
            break


def autorun(principal, stake):
    #    principal=int(input("請輸入本金"))
    beginprincipal = principal
#    stake=int(input("請輸入基礎下注額"))
    beginstake = stake
    while(principal > 0.5*beginprincipal and principal < 1.1*beginprincipal):
        if principal < stake:
            # print("本金不夠")
            break
        principal -= stake
        profit = bet(stake)
        if(profit == 0):
            stake *= 2
        else:
            stake = beginstake
        principal += profit
        #print("賺了%d,本金還有%d" % (profit, principal))
    return principal


'''def autorun():
    principal = int(input("請輸入本金"))
    beginprincipal = principal
    stake = int(input("請輸入基礎下注額"))
    beginstake = stake
    while(principal > 0.61*beginprincipal and principal < 1.1*beginprincipal):
        if principal < stake:
            print("本金不夠")
            break
        principal -= stake
        profit = bet(stake)
        if(profit == 0):
            stake *= 2
        else:
            stake = beginstake
        principal += profit
        print("賺了%d,本金還有%d" % (profit, principal))
    return principal'''


def autoruntest():
    countwin = 0
    countlose = 0
    boolcheck = 0
    for i in range(10000):
        boolcheck = autorun(10000, 50)
        if(boolcheck == 0):
            countwin += 1
        elif(boolcheck == 1):
            countlose += 1
    winrate = (countwin/(countwin+countlose))*100
    print("贏了%d次,輸了%d次,勝率為%.2f" % (countwin, countlose, winrate))
    return winrate


def main():
    minrate = 0.0
    maxrate = 0.0
    minrate = autoruntest()
    maxrate = minrate
    for i in range(99):
        temp = autoruntest()
        if(temp < minrate):
            minrate = temp
        elif(temp > maxrate):
            maxrate = temp
    print("最低勝率為%.2f,最高勝率為%.2f" % (minrate, maxrate))


def main2():
    totalprincipal = 10000
    win = 0
    lose = 0
    for i in range(15):
        check = autorun(10000, 10)
        if check < 10000:
            lose += (10000-check)
        else:
            win += (check-10000)
    dif = abs(lose-win)
    if win > lose:
        print("賺了%d,輸了%d,贏了差距%d" % (win, lose, dif))
        return 1
    else:
        print("賺了%d,輸了%d,輸了差距%d" % (win, lose, dif))
        return 0


def main3():
    countwin = 0
    countlose = 0
    for i in range(100):
        boolc = main2()
        if(boolc == 1):
            countwin += 1
        else:
            countlose += 1
    winrate = (countwin/(countwin+countlose))*100
    print("贏了%d次,輸了%d次,勝率為%.2f" % (countwin, countlose, winrate))


def win():
    principal = 1500
    total = 0
    for i in range(100):
        check = autorun(principal, 1)
        total += check-principal
    print(total)


win()
# artificial()
