# F_2 ^nの基底クラス
class F2n:
    # LISTを受け取ってbasisを生成する.(掃き出し法)
    def __init__(self,LIST):
        self.basis = []
        for ele in LIST:
            for vec in self.basis:
                ele = min(ele, vec^ele)
            if ele:
                self.basis.append(ele)
    # basisに要素eleを追加できるなら追加しTrueを返す. 追加できないなら何もせず,Falseを返す.
    def ADD(self, ele):
        for vec in self.basis:
            ele = min(ele, ele^vec)
        if ele:
            self.basis.append(ele)
            return True
        else:
            return False

# h=F2n([3,12,15,7])
# print(h.basis)
# print(h.ADD(4))
# h.ADD(1)
# print(h.basis)