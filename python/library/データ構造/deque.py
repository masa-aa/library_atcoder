from collections import deque

# 後ろから取り除く stack
s = deque([])
s.append(1)  # [1]
s.append(2)  # [1, 2]
s.append(3)  # [1, 2, 3]
s.pop()      # 一番上から取り除く [1, 2, 3] -> [1, 2]
s.pop()      # [1, 2] -> [1]
s.pop()      # [1] -> []

# 前から取り除くque
q = deque([])
q.append(1)  # [1]
q.append(2)  # [1, 2]
q.append(3)  # [1, 2, 3]
q.popleft()  # 一番下から取り除く [1, 2, 3] -> [2, 3]
q.popleft()  # [2, 3] -> [3]
q.popleft()  # [3] -> []
q.appendleft(12)
