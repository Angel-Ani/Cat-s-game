from cat import Cat 

print("***WELCOME TO MY CAT GAME ^W^!***")

name = input("Enter Cat name: ")
colour = input("Enter Cat colour: ")
my_cat = Cat(name, colour)

while True:
    action = input("""
What would you like to do?
                   
1. Train
2. Feed
3. Play 
4. Sleep
5. Show stats                   
""")                                                                                                       
    if action == "1":
       my_cat.train()
    elif action == "2":   
       my_cat.feed()
    elif action == "3":
       my_cat.play()
    elif action == "4":
       my_cat.sleep() 
    elif action == "5":
       my_cat.show_stats()        
 
# We will now make 2 cats

# Thses are called instances(specific occurance of a class) of the Cat class 
sid = Cat("Sid", "Black")        
mista = Cat("Mista", "White")

sid.train()
print(sid.intelligence)
print(mista.intelligence)