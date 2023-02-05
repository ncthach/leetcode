from typing import List

class Robot:
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    DIRECTION_NAMES = ["East", "North", "West", "South"]

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.circle_length = (self.width + self.height - 2) * 2
        self.x = 0 
        self.y = 0
        self.dir = 0

    def steps_to_bound(self) -> int:
        if self.dir == 0: # east
            return self.width - self.x - 1
        elif self.dir == 2: # west
            return self.x
        elif self.dir == 1: # noth
            return self.height - self.y - 1
        else: # south
            return self.y

    def step_in_bound(self, num:int) -> None:
        self.x += self.DIRECTIONS[self.dir][0] * num
        self.y += self.DIRECTIONS[self.dir][1] * num

    def step(self, num: int) -> None:
        num = num % self.circle_length
        if num == 0:
            if self.x == 0 and self.y == 0:
                self.dir = 3 # south
            elif self.x == self.width - 1 and self.y == 0:
                self.dir = 0 # east
            elif self.x == self.width - 1 and self.y == self.height - 1:
                self.dir = 1 # noth
            elif self.x == 0 and self.y == self.height - 1:
                self.dir = 2 # west
            return
        to_bound = self.steps_to_bound()
        while to_bound < num:
            self.step_in_bound(to_bound)
            num -= to_bound
            self.dir = (self.dir + 1) % 4
            to_bound = self.steps_to_bound()
        self.step_in_bound(num)

    def getPos(self) -> List[int]:
        return [self.x, self.y]
        

    def getDir(self) -> str:
        return self.DIRECTION_NAMES[self.dir]

cases = [
    #((20, 13), [12, 21, 17]),
    ((97, 98), [66392,83376,71796,57514,36284 ,69866 ,31652 ,32038])
]

for case in cases:
    r = Robot(case[0][0], case[0][1])
    for steps in case[1]:
        r.step(steps)
        print(r.getPos(), r.getDir())
