import random 
placesToLive = ["Mansion","Apartment","Shack","House","Dumpster","streets","Your moms house"]
Money = ["1","2","3","5"]
Kids = ["1","12","3","11","0"]


Home = input("Where do you think you will live in?")
Salary = input("What do you think your incom?")
Children= input("How many kids do you want?")

print("You will be living at a "+ random.choice(placesToLive)+
        " while making " + random.choice(Money) + 
        " dollars. And you will have " + random.choice(Kids) + " kids.")
        
        

