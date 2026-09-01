'''Consider a CSV (
cones.csv ) with cone id, x, y, colour (blue or yellow)
per row. Sort the rows by distance from the origin. Write two new CSVs, one
per colour, keeping the sorted order. Then find the midpoint between every
blue cone and its nearest yellow cone and write those midpoints to
centreline.csv .
Q8 is a stripped down version of what path planning actually does on the
car. '''
import os 
import csv

class pathplanning:
    def __init__(self):
        self.cones = []
        self.blue_cones = []
        self.yellow_cones = []

    def distance(self, x1, y1, x2, y2):
        return (x1 - x2) ** 2 + (y1 - y2) ** 2

    def input_cones(self):
        n = int(input("enter the number of cones to be added to dataset: "))

        with open("cones.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for i in range(n):
                cone_id = input("enter cone id: ")
                x = input("enter x coordinate: ")
                y = input("enter y coordinate: ")
                colour = input(" enter the colour blue/yellow (choose inly one): ")
                writer.writerow([cone_id, x, y, colour])

        with open("cones.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                cone_id = row[0]
                x = float(row[1])
                y = float(row[2])
                colour = row[3]
                self.cones.append([cone_id, x, y, colour])

    def sort_cones(self):
        n = len(self.cones)
        for i in range(n):
            smallest = i
            for j in range(i + 1, n):
                d1 = self.distance(self.cones[j][1], self.cones[j][2], 0, 0) #taking origin as ref point
                d2 = self.distance(self.cones[smallest][1], self.cones[smallest][2], 0, 0)
                if d1 < d2:
                    smallest = j
            self.cones[i], self.cones[smallest] = self.cones[smallest], self.cones[i]

    def diff_cones(self):
        for cone in self.cones:
            if cone[3] == "blue":
                self.blue_cones.append(cone)
            else:
                self.yellow_cones.append(cone)

    def save_files(self):
        with open("blue.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for cone in self.blue_cones:
                writer.writerow(cone)

        with open("yellow.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for cone in self.yellow_cones:
                writer.writerow(cone)

        with open("centreline.csv", "w", newline="") as file:
            writer = csv.writer(file)

            for blue in self.blue_cones:
                closest = self.yellow_cones[0]
                near_dist = self.distance(blue[1], blue[2], closest[1], closest[2])
                for yellow in self.yellow_cones:
                    d = self.distance(blue[1], blue[2], yellow[1], yellow[2])
                    if d < near_dist:
                        closest = yellow
                        near_dist = d
                mid_x = (blue[1] + closest[1]) / 2
                mid_y = (blue[2] + closest[2]) / 2
                writer.writerow([mid_x, mid_y])

        print("blue.csv, yellow.csv and centreline.csv created")


path = pathplanning()
path.input_cones()
path.sort_cones()
path.diff_cones()
path.save_files()
print("sorted cones:", path.cones)

