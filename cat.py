class Cat:
    #The constructor:
    # - the constructor will create a cat for us in code
    # - To create a cat, we need given_name & given_colour
    # - self is the cat that we are creating.
    def __init__(self, given_name, given_colour):
        #Name attribute
        self.name = given_name
        #Colour attribute 
        self.colour = given_colour
        self.age = 1
        self.energy = 50
        self.intelligence = 5
        self.weight = 5
    
    def train(self):
        print(f"{self.name} is training...") 
        self.energy -= 5
        self.intelligence += 1
        self.age +=  0.1 
        
    def feed(self):
        print(f"{self.name} is eating...") 
        self.energy += 10
        self.weight += 1
        self.age +=  0.1 

    def play(self):
        print(f"{self.name} is playing...") 
        self.energy -= 2
        self.intelligence += 2
        self.age +=  0.1 

    def sleep(self):
        print(f"{self.name} is sleeping...") 
        self.energy += 15
        self.intelligence += 5
        self.age +=  0.1 

    def show_stats(self):
        print(f'{self.name} has {self.energy} of energy, {self.intelligence} of intelligence, is {self.weight}  in kg and is {self.age} in age ')    


