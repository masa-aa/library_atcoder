from random import randint

dic = {"数字":"number", "数字":"number", "論理":"logic"} # ここに追加する
num = 5 # 問題数

#ここより下は触らない.
#-------------------------------------------------------------------------------

key = list(dic.keys())
n = len(key)
correct = 0
i = 0
use = set()
miss=[]
print()

while i < n and i < num: 
    a = key[randint(0,n-1)]
    if not(a in use):
        answer = input(a+"    ")
        use.add(a)
        i += 1
        if answer == dic[a]:
            print("正解")
            print()
            correct+=1
        else:
            print("x 正解は " + dic[a])
            print()
            miss.append(a)
print("正解数は",correct,"問です。")
print()
if i - correct > 0:
    print("間違えた単語は")
    print()
    for x in miss:
        print(x,":",dic[x])
        print()
    print("の",i - correct,"問です。")
else:
    print("全問正解おめでとう！！")
print()