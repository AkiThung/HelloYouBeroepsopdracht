import time


a = True
while a == True:
    hello = "Hello You! \nik ben {owner}. hoe heet jij?"
    print(hello.format(owner = "Aki"))

    time.sleep (1)

    username = input("Mijn naam is:")
    print("Hallo " + username, "welkom in TAFARIA")

    time.sleep (1)

    while True:
     time.sleep( 2 )

     antwoord1 = input("Je komt aan  in TAFARIA. De eerste vraag in deze wereld is welk ras wil je worden, aangezien alles in deze wereld kan \n A Dwerg \n B Elf \n C Minataurus \n antwoord: ")
     if ( antwoord1 == "A"):
        print("eyy Kleintje")
     elif ( antwoord1 == "B"):
        print("Welkom onsterfelijke")
     elif ( antwoord1 == "C"):
        print("Nice cut G, like them horns")
     time.sleep( 2 )
        
     antwoord2 = input("Wat is je class \n A Archer \n B Warrior  \n C Mage \n antwoord: ")
     if ( antwoord2 == "A"):
         print("Scherpschutter ;)")
     elif ( antwoord2 == "B"):
        print("Strong Warrior u are the base of our existence as a clan")
     elif ( antwoord2 == "C"):
        print("Gekke Magie, Als Mage ga je naar de citadel genaamd SEKARA om te leren je krachten te gebruiken")
        antwoord4 = input("Wat is je  preference binnen de Magie?\n A Vuur \n B Water \n C Bloodmagic \n antwoord:")
        if ( antwoord4 == "A"):
            print("FIREEE")
        elif ( antwoord4 == "B"):
            print("can u make a tsunami??")
        elif ( antwoord4 == "C"):
            print("the powers of the evil")
         break  
     time.sleep( 2 )
     antwoord3 = input("Wanneer ben ik jarig \n A 24 mei \n B 25 mei \n C 26 mei \n antwoord:")
     if ( antwoord3 == "A"):
         print("goed")
     elif ( antwoord3 == "B"):
        print("fout")
     elif ( antwoord3 == "C"):
        print("fout")
    
    
