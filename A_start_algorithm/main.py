from queue import PriorityQueue

from data import data


class Node:
    def __init__(self, name, par=None, g=0, h=0):
        self.name = name
        self.par = par
        self.g = g
        self.h = h

    def display(self):
        print(self.name, self.par, self.g, self.h)

    def __lt__(self, other):
        if other is None:
            return False
        return self.g + self.h < other.g + other.h

    def __eq__(self, other):
        if other is None:
            return False
        return self.name == other.name


def equal(O, G):
    if O.name == G.name:
        return True
    return False


def checkInPriority(tmp, c):
    # Sử dụng một tập hợp để kiểm tra xem có trong hàng đợi không
    if tmp == None:
        return False
    return tmp in c.queue


def getPath(O):
    print(O.name)
    if O.par != None:
        getPath(O.par)
    else:
        return

def AStart(S=Node('A'), G=Node('N')):
    Open = PriorityQueue()  # Sử dụng queue.PriorityQueue
    Closed = PriorityQueue()

    S.h = data[S.name][-1]
    Open.put(S)
    j = 1

    while True:
        if Open.empty():
            print("Tìm kiếm thất bại")
            return
        O = Open.get()
        Closed.put(O)
        print(f'Duyệt lần {j}: ', O.name, O.g, O.h)
        j += 1
        if equal(O, G):
            print("Tìm kiếm thành công")
            getPath(O)
            print("\ndistance: ", O.g + O.h)
            return

        i = 0
        while i < len(data[O.name]) - 1:
            name = data[O.name][i]
            g = O.g + data[O.name][i + 1]
            h = data[name][-1]  # Heuristic
            tmp = Node(name=name, g=g, h=h)
            tmp.par = O  # Đặt O là cha của tmp

            ok1 = checkInPriority(tmp, Open)
            ok2 = checkInPriority(tmp, Closed)

            if not ok1 and not ok2:
                Open.put(tmp)

            i += 2

# Test
AStart(Node('A'), Node('J'))