import random

# トランプカードの生成
spade = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
heart = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
club = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
diamond = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
trump = spade + heart + club + diamond
random.shuffle(trump)


class Player():
    def __init__(self, name):
        self.name = name
        self.l = []
        self.sum = 0
        self.lnum = []
        self.lcourt = []
        self.lace = []
        self.lsort = []

    def addSum(self):

        card = trump.pop(0)
        self.l.append(card)

        if(card == "J" or card == "Q" or card == "K"):
            self.lcourt.append(card)
        elif(card == "A"):
            self.lace.append(card)
        else:
            self.lnum.append(card)

        self.lsort = self.lnum + self.lcourt + self.lace

        self.sum = 0

        for i in range(len(self.lsort)):
            if(self.lsort[i] == "J" or self.lsort[i] == "Q" or self.lsort[i] == "K"):
                self.sum = self.sum + 10
            elif(self.lsort[i] == "A" and self.sum <= 11):
                self.sum = self.sum + 10
            elif(self.lsort[i] == "A" and self.sum > 11):
                self.sum = self.sum + 1
            else:
                self.sum = self.sum + int(self.lsort[i])
        return card


# プレイヤー数の設定
print("何人で遊びますか?  1~4")
playerNum = input()

while(int(playerNum) > 4):
    print("4人以下で設定してください")
    playerNum = input()

lplayer = []

for i in range(1, int(playerNum)+1):

    print(str(i)+"番目のプレイヤーの名前を入力してください。")
    name = input()
    lplayer.append(name)

print("***********************************************")
print(lplayer)
print("上記"+playerNum+"人のプレイヤーでゲームを始めます。")
print("***********************************************")
input()

players = []
for i in range(len(lplayer)):
    players.append(Player(lplayer[i]))

# 各プレイヤーは最初に2枚のカードを引く
isStop = []
score = []
for i in range(len(lplayer)):
    players[i].addSum()
    players[i].addSum()
    print(lplayer[i]+"さんの手札は" + str(players[i].l) +
          "で、合計は" + str(players[i].sum) + "です。")
    isStop.append("Y")
    score.append(players[i].sum)
input()
print("***********************************************")

# 判定がYのプレイヤーだけ、カードを追加で引くかどうか決める
while "Y" in isStop:

    for i in range(len(isStop)):
        if(isStop[i] == "Y"):
            print(lplayer[i]+"さんのターンです。")
            print(lplayer[i]+"さんの手札は" + str(players[i].l) +
                  "で、合計は" + str(players[i].sum) + "です。")
            print("追加でカードを引きますか?  y/n")
            draw = input()
            if(draw == "y"):
                addCard = players[i].addSum()
                print("追加で" + str(addCard) + "を引きました。現在の手札は" +
                      str(players[i].l) + "です。")
                print("合計は" + str(players[i].sum)+"です。")
                score[i] = players[i].sum
                if(players[i].sum > 21):
                    print("21を超えてしまいました。ドボンです。")
                    print("***********************************************")
                    isStop[i] = "N"
                    score[i] = 0
                    input()
                    break
                print("***********************************************")
                input()
            if(draw == "n"):
                print(lplayer[i]+"さんのスコアは" + str(players[i].sum)+"です。")
                print("***********************************************")
                isStop[i] = "N"
                score[i] = players[i].sum
                input()

# 勝敗を決める
winner = [lplayer[i] for i, v in enumerate(score) if v == max(score)]

print("優勝は...!!")
input()
print(winner)
print("")
scoreBoard = [[lplayer[i], score[i]] for i in range(len(lplayer))]
print(scoreBoard)
print("***********************************************")
