# how to calculate if a car will catch up to another
# speed must be greater for tailing car
# how much greater?
# the trajectories of the cars are like lines on a graph.
# we need to find where they intersect, and also when the leading
# car passes the target
# if they intersect before the leading car passes the target,
# we win
# after getting through this logic, we need to consider a case in 
# which the car in front of the leading car slows the leading car down

# derivation of intersection time: 
    # y = cx + b
    # y = dx + e
    # dx + e = cx + b
    # dx - cx = b - e
    # x = (b - e)/(d - c)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def will_intersect(p1, s1, p2, s2, target):
            if p1 < p2:
                lead = (p2, s2)
                tail = (p1, s1)
            else:
                lead = (p1, s1)
                tail = (p2, s2)
            
            lead_pos, lead_sp = lead[0], lead[1]
            tail_pos, tail_sp = tail[0], tail[1]

            if tail_sp <= lead_sp: # base case
                return False
            
            time_to_target = (target - lead_pos)/lead_sp
            time_to_cross = (lead_pos - tail_pos)/(tail_sp - lead_sp)

            if time_to_cross <= time_to_target:
                return True

        if len(position) == 1:
            return(1)

        cars = []
        for pos, sp in zip(position, speed):
            cars.append((pos, sp))
        
        cars.sort(reverse = True)

        fleet = []
        car_fleets = []
        leading = cars[0]
        fleet.append(leading)
        for i in range(1, len(cars)):
            p1, s1 = leading[0], leading[1]
            p2, s2 = cars[i][0], cars[i][1]
            if will_intersect(p1, s1, p2, s2, target):
                fleet.append(cars[i])
                if i == len(cars) - 1:
                    car_fleets.append(fleet)
                    fleet = []
                continue
            else:
                print(cars[i])
                leading = cars[i]
                car_fleets.append(fleet)
                fleet = []
                fleet.append(cars[i])
        if len(fleet) != 0:
            car_fleets.append(fleet)
        print(car_fleets)
        return(len(car_fleets))








            


            