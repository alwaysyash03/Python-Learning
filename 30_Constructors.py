class Point:
    #creating an constructor object
    def __init__(self, x , y):  #init is short form of initialize
        self.x = x  #Here self is used to referece the current object
        self.y = y
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")


#A constructor is an object that is called at the time of creating an object
point = Point(10, 20)
print(point.x)

# We can also update its value
point.x = 11
print(point.x)