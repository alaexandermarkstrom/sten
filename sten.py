import random
options = 0
#vi skapar en variabel och ger den ett värde för att användas senare
mypoints = 0
aipoints = 0 
ai = random.randint(1, 3) 
#vi skapar en variablel som är ett slumpat nummer mellan 1, 2, 3

print("Hej på dig där! Välkommen till vårat program.")

while options != 4: 
#medans vi inte skriver 4 så fortsätter programmet
    print ("mina poäng " + str(mypoints))
    print ("ai poäng " + str(aipoints))
    #vi printar ut hur många poäng båda spelarna har
    ai = random.randint(1, 3)
    if mypoints == 2:
        print ("Du har vunnit!")
        break
        #om mina poäng är 2 så printar programmet ut att jag har vunnit och programmet avslutas
    elif aipoints == 2:
        print ("ai har vunnit!")
        break
    try:
        options = int(input("Här väljer du mellan sten sax och påse."))
        #programmet testar för en imput på nummer mellan 1-4
    except:
        print ("måste välja sten, sax eller påse")
        #om det inte händer så printar den ut ett meddelande 

    if options == 1:
        print ("du har valt sten")
        #om du väljer 1 (sten) så printar den ut att du har valt sten
        if ai == 1:
            print ("ai valde sten, det blev lika")
        elif ai == 2:
            print ("ai valde sax, du vann!")
            mypoints += 1
            #om ai väljer något som förlorar till det så printar den ut att vi vinner och variabel mypoints får +1 poäng
        elif ai == 3:
            print ("ai valde påse, du förlorade")
            aipoints += 1
    elif options == 2:
        print ("du har valt sax")
        if ai == 1:
            print ("ai valde sten, du förlorade!")
            aipoints += 1
        elif ai == 2:
            print ("ai valde sax, det blev lika")
        elif ai == 3:
            print ("ai valde påse, du vann")
            mypoints += 1
    elif options == 3:
        print ("du har valt påse")
        if ai == 1:
            print ("ai valde sten, du vann!")
            mypoints += 1
        elif ai == 2:
            print ("ai valde sax, du förlorade")
            aipoints += 1
        elif ai == 3:
            print ("ai valde påse, det blev lika")
    elif options == 4:
        print ("nu avslutas programmet")
        #eftersom 4 avslutar loopen så avslutas programmet och den printar ut att vi gör det
    else:
        print ("det blev fel")
        #om vi inputar något som inte är 1-4 så printar den ut att det blir fel