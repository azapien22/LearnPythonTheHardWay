# Exercise 30 Else and If

people = 30 
cars = 40 
trucks = 15

if cars > people:
    print("we Should take the cars.")

elif cars < people:
    print("We should not take the cars.")
    
else:
    print("We cant decide.")
    
if trucks > cars:
    print("Thats too many")
    
elif trucks < cars:
    print("Maybe we could take the trucks.")
    
else:
    print("We still can't decide.")
    
if people > trucks:
    print("ALright, Let's just take the trucks.")

else: 
    print("Fine, Let's stay home then.")