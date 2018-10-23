options = 0
mypoints = 0


while options != 3:
    print ("mina poäng " + str(mypoints))
    try:
        options = int(input("välj nummer:"))
    except:
        print ("måste välja 1-4")
    if options == 1:
        mypoints += 1
    elif options == 2:
        mypoints -= 1
    else:
        print ("oj")
