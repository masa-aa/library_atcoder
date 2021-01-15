# dequeを使いましょう

"""
"stack" putとgetができる
"""
import queue

# LIFOキューの作成
q = queue.LifoQueue()

# キューにデータを挿入する。挿入するデータは「0, 1, 2, 3, 4」
for i in range(5):
    q.put(i)

# キューからデータがなくなるまで取り出しを行う
while not q.empty():
    print(q.get())
    # 4 3 2 1 0


"""
"Que" putとgetができる
"""
import queue

# FIFOキューの作成
q = queue.Queue()

# キューにデータを挿入する。挿入するデータは「0, 1, 2, 3, 4」
for i in range(5):
    q.put(i)

# キューからデータがなくなるまで取り出しを行う
while not q.empty():
    print(q.get())
    # 0 1 2 3 4
