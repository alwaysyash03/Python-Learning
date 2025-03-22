import random # Built in python module for generating random numbers

for i in range(3):
    print(random.random())
 
for i in range(3):
   print(random.randint(10, 20)) # Generates a random integer between 10 and 20


members = ["Yash", "Ishita", "Sujal", "Nikki", "Lisa"]
leader = random.choice(members)
print(leader) # Chooses a random member from the list and prints it.