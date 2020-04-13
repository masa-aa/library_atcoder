"""
listの要素の数を数える
返り値は「Python 辞書」で検索
"""

def list_count(my_list):
    dic={} #辞書型の宣言
    for num in my_list:
        if num in dic: #もしnumがkeyとして辞書にあれば
            dic[num]+=1 #valueに+1
        else: #なければ
            dic[num]=1 #dicにnumというkeyを追加し、対応するvalueを1とする
    return dic
    
n=int(input())
l=list(map(int,input().split()))
print(list_count(l))
#--------------------
#使用例
#--------------------
"""

a=[5, 6, 9, 6, 4, 6, 10, 9, 10, 1]

dic=list_count(a)

print(dic)
{5: 1, 6: 3, 9: 2, 4: 1, 10: 2, 1: 1}

print(dic.keys())
dict_keys([5, 6, 9, 4, 10, 1])
list型として使用可能

print(dic.values())
dict_values([1, 3, 2, 1, 2, 1])
list型として使用可能
"""


from collections import Counter