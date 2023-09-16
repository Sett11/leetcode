class MyCalendar:

    def __init__(self):
        self.a = []

    def book(self, s, e):
        for i in self.a:
            if (s >= i[0] and e <= i[1]) or (s < i[1] and s >= i[0]) or (e > i[0] and s < i[0]):
                return False
        return bool(self.a.append([s, e]) or 1)


m = MyCalendar()

arr = [47, 50], [33, 41], [39, 45], [33, 42], [25, 32], [
    26, 35], [19, 25], [3, 8], [8, 13], [18, 27]

for i in arr:
    print(m.book(i[0], i[1]))
    #print(m.a)
