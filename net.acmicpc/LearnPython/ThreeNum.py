# 세 수
# https://www.acmicpc.net/problem/10817
def solution():
    test = PriorityList()

    for i in map(int, input().split()):
        test.put(i)

    print(test.get(1))

class PriorityList :

    def __init__(self):
        self.list = []
        self.count = 0
    
    def put(self, newOne):
        if self.count == 0 :
            self.list.append(newOne)
        else:
            for i in range(self.count):
                if newOne < self.list[i] :
                    self.list.insert(i, newOne)
                    break
                if i == self.count-1 :
                    self.list.append(newOne)
        self.count += 1          
    
    def get(self, index):
        return self.list[index]

solution()