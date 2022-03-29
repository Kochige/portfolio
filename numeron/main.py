import sys
import random


# 回答できる回数の設定
print("numer0nを始めます。20以下の答える回数を入力してください。(推奨:10)")
while True:
    try:
        reply = int(input())
        while True:
            if(reply > 20):
                print("20以下の数字を入力してください。(推奨:10)")
                reply = int(input())
            else:
                print("***************************************")
                break
        break
    except ValueError as e:
        print("数字を入力してください。")

# 答えの桁数の設定
print("続いて、解答の桁数(5桁以下)を入力してください。(推奨:4)")
while True:
    try:
        digit = int(input())
        while True:
            if(digit > 5):
                print("5以下の数字を入力してください。")
                digit = int(input())
            else:
                print("***************************************")
                break
        break
    except ValueError as e:
        print("数字を入力してください。")

# 正解の数字の生成
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(num)
ans = num[0:digit]

# 正誤判定
res = []


def isCollect(num):
    eat = 0
    bite = 0
    varDigit = "{:0"+str(digit)+"}"
    num = varDigit.format(num)
    numList = [int(a) for a in num]

    for i in range(len(ans)):
        if(numList[i] == ans[i]):
            eat += 1
        elif(numList[i] in ans):
            bite += 1
    if(int(eat) == int(digit)):
        print("正解は"+num + "でした。おめでとうございます！")
        print("回答した回数は"+str(int(len(res)+1))+"回！")
        sys.exit()
    print(num+"は、 eat: " + str(eat)+", bite: " + str(bite)+"です")
    res.append([str(num), "eat: " + str(eat), "bite: " + str(bite)])
    for i in res:
        print(i)
    print("***************************************")


print("それではゲームを始めます。")
# 回答のループ
i = 0
while i < reply:
    print(str(digit)+"桁の数字を入力してください")
    while True:
        try:
            challenge = str(input())
            while True:
                if(str(len(challenge)) != str(digit)):
                    print("入力に誤りがあります。"+str(digit)+"桁の数字を入力してください。")
                    challenge = str(input())
                else:
                    isCollect(int(challenge))
                    break
            break
        except ValueError as e:
            print("予期せぬエラー発生")
    i += 1


# 指定の回数以内に正解できなかった場合、答えを表示
map = map(str, ans)
print("残念！正解は"+str(''.join(map))+"でした！")
