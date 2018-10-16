import random
options = 0 #["sten", "sax", "påse"]
sten = 1
sax = 2
påse = 3
spelare = 4
motståndare = 5
ai = random.randint(1, 3)


print("Hej på dig där! Välkommen till vårat program.")

while options != 4:

    try:
        options = int(input("Här väljer du mellan sten sax och påse."))
    except:
        print ("måste välja sten, sax eller påse")
    if options == 1:
        print ("du har valt sten")
    elif options == 2:
        print ("du har valt sax")
    elif options == 3:
        print ("du har valt påse")
    else:
        print("nu avslutas programmet")


