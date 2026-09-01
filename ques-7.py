''' Let (x,y) be a point in 2D space. Given a list of coordinates, write a sort
function that sorts them by proximity to a reference point given by the user
that is not in the list. Eg list 
[(0,1),(0,3),(1,2)] , reference 
(0,0) ,
output 
[(0,1),(1,2),(0,3)]'''

def shortest_distance(point, ref):
    x1 = point[0]
    y1 = point[1]
    x2 = ref[0]
    y2 = ref[1]
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


n = int(input("enter how many points you want to enter: "))

points = []
for i in range(n):
    x = int(input("enter x: "))
    y = int(input("enter y: "))
    points.append((x, y))

ref_x = int(input("enter reference x: "))
ref_y = int(input("enter reference y: "))
ref = (ref_x, ref_y)

result = sorted(points, key=lambda point: distance(point, ref))
print(result) 
