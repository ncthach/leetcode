from typing import List
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses = sorted(buses)
        passengers = sorted(passengers)
        next_passenger = 0
        num_buses = len(buses)
        num_people = len(passengers)
        for bus in buses:
            full = False
            last_passenger = self.index_last_smaller_or_equal_element(
                passengers, bus, next_passenger, min(next_passenger + capacity - 1, num_people - 1)
            )
            if last_passenger == next_passenger + capacity - 1:
                full = True
            if last_passenger != -1: # some passengers are waiting
                # print("bus", bus, "depart with passenger from ", next_passenger, "to ", last_passenger)
                next_passenger = last_passenger + 1
        if full or (next_passenger > 0 and buses[-1] == passengers[next_passenger - 1]):
            for passenger in range(next_passenger - 1, 0, -1):
                if passengers[passenger] - 1 > passengers[passenger - 1]:
                    return passengers[passenger] - 1
        else: # not full, the last person on bus doesn't arrive right when the bus leaves, and the next person arrives after that
            return buses[-1]

        return passengers[0] - 1
    
    def index_last_smaller_or_equal_element(self, a: List[int], target: int, left: int, right: int) -> int:
        if target >= a[right]:
            return right
        if target < a[left]:
            return -1
        if right - left == 1:
            return left

        mid = (left + right) // 2
        if target < a[mid]:
            return self.index_last_smaller_or_equal_element(a, target, left, mid)
        else: # target >= a[mid]
            return self.index_last_smaller_or_equal_element(a, target, mid, right)

cases = [
    ([10,20], [2,17,18,19], 2),
    ([20,30,10], [19,13,26,4,25,11,21], 2),
    ([20,30,10], [19,13,26,4,25,11,21], 3),
    ([3], [2, 4], 2),
    ([2], [2], 2)
]

for case in cases:
    sol = Solution()
    print(sol.latestTimeCatchTheBus(case[0], case[1], case[2]))