class House():
    def __init__(self,name ,num):
        self.name  = name
        self.num = num
    def __gt__(self, other):
        return self.num > other.num
    def __lt__(self, other):
        return self.num < other.num
    def __ge__(self, other):
        return self.num >= other.num
    def __le__(self, other):
        return self.num <= other.num
    def __eq__(self, other):
        return self.num == other.num
    def __ne__(self, other):
        return self.num != other.num
    def __add__(self, other):
        return self.num + other
    def __iadd__(self, other):
        return self.num + other
    def __radd__(self, other):
        return self.num + other

hs1 = House("DOOSAN", 20)
hs2 = House("DOOSAN", 10)
hs3 = House("DOOSAN", 5)
print(hs3 < hs1 > hs2)
print(hs1 < hs2)
print(hs1 >= hs2)
print(hs1 <= hs2 < hs3)
print(hs1 == hs2)

hs1 = hs1 + 50
hs2 += 30
hs3 = 5 + hs3
print(hs1)
print(hs2)
print(hs3)