from random import randrange


class RollingHash:
    def __init__(self, s):
        self.base = [37, 368789449308, 1852846309939, 2102001800968, 3135613673210,
                     3573032120887, 5162739766272, 5981870488812, 6752369793223, 7700519273161,
                     9299907180755, 11220764879935, 13661711890983, 15631445301958, 16191225434172,
                     17992903178549, 18444241224682, 19542925735378, 19904897765689, 21026451511176,
                     22352021740951, 24614951263776, 27926655860868, 28668013049122, 30731186880431,
                     31200962432156, 32525487701018, 33195339867934, 34424470708402, 35347625139334,
                     35538747926358, 35582135363245, 38299872411055, 39611488430368, 39640191188389,
                     39687840340713, 39836964525889, 40494045054405, 41823714436906, 42464338718658,
                     45187222874290, 46814471362845, 46843887310593, 47056835891494, 47120526022187,
                     47245858682046, 48060903655667, 49148836433744, 50740362522447, 52092287614654,
                     52963661986595, 53909010970445, 54034266176372, 56610716098501, 57249192258849,
                     58159353606107, 58265735653900, 59020252957603, 60035782095813, 60299921283817,
                     61190794855394, 64063255668212, 66214433217808, 66216096723703, 67780144096898,
                     67999945148190, 68256362212749, 70499107424943, 70862334850448, 72011752626580,
                     73649428254369, 75449903238572, 76548613569443, 78278540023804, 79009260751099,
                     80099977091766, 80465655308476, 83855206194524, 92017907719628, 92059595206125,
                     92062781387242, 92471692941349, 92498823585506, 93431743820951, 94923662069170,
                     95089788205304, 96760468270869, 97437512252944, 98969648473851, 101584354600387,
                     103992426667469, 104570401503026, 105149646660817, 106163858477891, 106970744616241,
                     107019066406563, 107140499986715, 108680210682305, 109288626609043, 110027486424350][randrange(0, 100)]
        self.mod = 2305843009213693951  # 2**61 - 1
        self.size = len(s)
        self.string = s

        self.hash = self.__make_hashtable(s)
        self.pow = self.__make_powtable()

    def __make_hashtable(self, _s):
        hashtable = [0] * (self.size + 1)
        for i in range(self.size):
            hashtable[i + 1] = (hashtable[i] * self.base + ord(_s[i])) % self.mod
        return hashtable

    def __make_powtable(self):
        power = [1] * (self.size + 1)
        for i in range(self.size):
            power[i + 1] = (self.base * power[i]) % self.mod
        return power

    def __get_hash(self, left, right):
        """get hash of s[left:right]"""
        return (self.hash[right] - self.hash[left] * self.pow[right - left]) % self.mod

    def contain(self, a):
        """return all s.index(a)"""
        m = len(a)
        hasha = 0
        index = []
        if m > self.size:
            return index
        for i in range(m):
            hasha = (hasha * self.base + ord(a[i])) % self.mod
        for i in range(self.size - m + 1):
            hashs = self.__get_hash(i, m + i)
            if hasha == hashs:
                index.append(i)
        return index

    def is_contain(self, a):
        """return a in s"""
        m = len(a)
        if m > self.size:
            return False
        hasha = 0
        for i in range(m):
            hasha = (hasha * self.base + ord(a[i])) % self.mod
        for i in range(self.size - m + 1):
            hashs = self.__get_hash(i, m + i)
            if hasha == hashs:
                return True
        return hasha == hashs

# verify contain
# https://onlinejudge.u-aizu.ac.jp/solutions/problem/ALDS1_14_B/review/5211162/masa_aa/Python3


def main():
    t = input()
    p = input()
    rh = RollingHash(t)
    res = rh.contain(p)
    if res:
        print(*res, sep="\n")


if __name__ == "__main__":
    main()
