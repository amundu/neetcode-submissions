class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions = []
        for i in range(len(position)):
            positions.append((position[i], speed[i]))
        positions.sort()

        car_fleet_stack = []
        for i in range(len(positions)-1, -1, -1):
            pos, speed = positions[i]
            curr_time = (target-pos)/speed
            if not car_fleet_stack or car_fleet_stack[-1] < curr_time:
                car_fleet_stack.append(curr_time)
            
        return len(car_fleet_stack)
        