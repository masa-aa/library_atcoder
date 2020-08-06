# k文字ずらす
c = input()
k = int(input())
chr(ord(c) + k)

# アルファベット生成
al = [chr(ord('a') + i) for i in range(26)]
