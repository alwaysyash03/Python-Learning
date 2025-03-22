class Point:   #Classes are used to define new type
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Point()  #point1 is object
point1.x = 10  #we also assign attributes like here x is attribute
point1.y = 20
print(point1.x)
point1.move()  # Move

point2 = Point()  #point2 is another object
point2.x = 4
print(point2.x)