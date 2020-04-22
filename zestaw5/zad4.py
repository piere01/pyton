class Point:
    counter = []

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
p2 = Point(3,1)
p3 = Point(2,4)
p4 = Point(2,1)

print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
print("")
p1.update(1)
print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
print("")
p2.update(5)
print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
print("")
p3.update(10)
print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
print("")
p4.update(454)
print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
print("")
print("")
p4.counter=[3,5,8,1]
print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
print("")
