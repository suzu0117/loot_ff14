playername = []
loot = {}
import random

people = int(input("人数を入力してください\n"))

# n人目のプレイヤーの名前を入れる
number =1
while number <= people:
    name = input(str(number)+"人目の名前\n")
    playername.append(name)
    number =number + 1


# ダイスを振る
number =1
while number <= people:
    dice = random.randint(1, 99)
    loot[playername[number-1]] = dice
    number =number + 1


# ダイスで出した目を出力    
number =1
while number <= people:
 print(playername[number-1]+"はダイスで"+str(loot[playername[number-1]])+"を出した。\n")
 number =number + 1


# 誰が一番大きい数字を出したか判定
number =1
get = 0
while number <= people:
 if get<loot[playername[number-1]]:
    get = loot[playername[number-1]]
    number=number+1
 else:
    number=number+1
	
getplayer =  [k for k, v in loot.items() if v == get]
print(str(getplayer)+"はアイテムを手に入れた。")

