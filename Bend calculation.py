#For calculating the measurements to bend conduit
import math

#collect measurements
dist_to_obstacle = float(input("Distance to obstacle: "))
obstacle_height = float(input("Height of obstacle: "))
obstacle_width  = float(input("Width of obstacle: "))
bend_radius = int(input("Bend radius to be used (10, 22, 30): "))


#set bend multiplier
if bend_radius == 10:
    mult = 6.0
elif bend_radius == 22:
    mult = 2.6
elif bend_radius == 30:
    mult = 2.0
else:
    pass

#adjust bend position from obstacle
lin_offset = obstacle_height / math.tan(bend_radius)

    
#Find distance from end of stick to first bend, dependent on bend radius
first_bend = dist_to_obstacle - (lin_offset)

#Find distance from first bend to second bend, dependent on bend radius
second_bend = first_bend + (obstacle_height * mult)

#Find distance from second bend to third bend, dependent on bend radius
third_bend = second_bend + obstacle_width

#Find distance from third bend to fourth bend, dependent on bend radius
fourth_bend = third_bend + (obstacle_height * mult)

print("first mark at", round(first_bend, 2),"second mark at", round(second_bend,2),round(third_bend,2), \
      "\nthird bend at",round(third_bend, 2), "fourth bend at", round(fourth_bend))

if lin_offset <0 or first_bend < 0 :
    print("ERROR")
else:
    pass

outro = input("Good luck, Hackman")

    
