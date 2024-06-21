#Import math library to use its functions
import math

#Take some random points.
points = [(3,5), (1,7), (7,12), (4,6), (13,7), (5,8)]

#Define a function that calculates the distance between given any two points.
def euclideanDistance(point_1, point_2):
    return math.sqrt((point_1[0]-point_2[0])**2 + (point_1[1]-point_2[1])**2)

#Create an empty list to save later all calculated distances.
distances = []

#Add all calculated distances to the empty list.
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        d = euclideanDistance(points[i], points[j])
        distances.append(d)
        
#Create a variable and assing the smallest value of the distances list and print it.
min_distance = min(distances)
print(f"Minimum Euclidean Distance is {min_distance}")
