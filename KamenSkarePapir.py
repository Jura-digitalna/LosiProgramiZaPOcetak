import random
Komp = random.randrange(1,3)
User = input("odaberi broj od jedan do 3 \n")
if int(User) == Komp:
    print("Pobjedi")
else:
    print("Izgubili ste")
