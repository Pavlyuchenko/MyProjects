class Current:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.face_pos = 1
        self.counter = 0

    def move_right(self, city):

        if self.face_pos == 1:
            self.x += 1
            self.face_pos = 2

        elif self.face_pos == 2:
            self.y += 1
            self.face_pos = 3

        elif self.face_pos == 3:
            self.x -= 1
            self.face_pos = 4

        elif self.face_pos == 4:
            self.y -= 1
            self.face_pos = 1

        self.counter += 1

        city[self.y-1][self.x-1] = self.counter
        return city

    def move_up(self, city):

        if self.face_pos == 1:
            self.y -= 1

        elif self.face_pos == 2:
            self.x += 1

        elif self.face_pos == 3:
            self.y += 1

        elif self.face_pos == 4:
            self.x -= 1

        self.counter += 1

        city[self.y-1][self.x-1] = self.counter
        return city

    def print_position(self, city):
        print("Current: [" + str(self.x) + ", " + str(self.y) + "]" + " || Counter: " + str(self.counter))
        for road in city:
            print(road)

    def position(self):
        return [self.x, self.y]


def find_shortest_path(nmk, start_finish, broken_paths):
    n = nmk[0]
    m = nmk[1]
    k = nmk[2]
    start = list(reversed(start_finish[0:2]))
    finish = list(reversed(start_finish[2:]))

    print("Rozmer: " + str(n) + "x" + str(m))
    print("Pocet rozbitych silnic: " + str(k))
    print("Start: " + str(start))
    print("Finish: " + str(finish))

    print()

    curr = Current(start)
    #curr.print_position()

    city = [[True for x in range(m)] for y in range(n)]
    print(curr.x, curr.y)
    for broken in broken_paths:
        city[broken[0]-1][broken[1]-1] = False

    city[curr.y-1][curr.x-1] = 0

    for road in city:
        print(road)

    #while curr.position() != finish:
    city = curr.move_right(city)
    city = curr.move_right(city)
    city = curr.move_up(city)
    city = curr.move_up(city)
    '''curr.move_right()
        curr.move_up()
        curr.move_right()
        curr.move_up()
        curr.move_right()
        curr.move_up()'''
    curr.print_position(city)


find_shortest_path([4, 3, 1], [1, 2, 1, 1], [[2, 2]])
