import time


a = True
while a == True:
    Welkom = " hallo welkom bij mijn textbased application over een vluchteling"
    print(Welkom)

    time.sleep (1)
    while True:
     time.sleep( 2 )

     def vraag2():
         antwoord2 = input("De Taliban bedreigt je na een paar jaar dit werk te doen. Ze zeggen als je nu niet stopt met dit werk staat je niet veel goeds te verwachten. \n wat doe je \n A Je besluit alsnog je studie architectuur te vervolgen. \n B Je besluit te verhuizen naar Kabul. \n C Je gaat alsnog op de markt werken aangezien je niet wil opvallen.")
         if ( antwoord2 == "A"):
            vraag5()
         elif ( antwoord2 == "B"):
            vraag3()
         elif ( antwoord2 == "C"):
            vraag4()

     def vraag3():
         antwoord3 = input("Je komt aan in Kabul en je vervolgt je werk. Je wordt nogmaals bedreigd. \n Wat doe je? \n A Je besluit het land uit te vluchten \n B Je besluit alsnog ander werk te zoeken")
         if ( antwoord3 == "A"):
            print("A")
         elif ( antwoord3 == "B"):
            print("B")

     def vraag4():
         antwoord4 = ("
         
    

     antwoord1 = input("Je begint als een normale burger in Kandahar (Afghanistan). Je doet een studie architectuur. Maar je familie heeft geld nodig.\n Wat doe je? \n A je kiest ervoor om je studie te vervcolgen. \n B je kiest ervoor om internationaal werk te gaan doen \n C je gaat op een markt werken.")
     if ( antwoord1 == "A"):
        vraag5()
     elif ( antwoord1 == "B"):
        vraag2()
     elif ( antwoord1 == "C"):
        vraag4()
    

    
    
