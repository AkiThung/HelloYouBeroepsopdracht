import time


a = True
while a == True:
    hello = "Hello You! \nik ben {owner}. hoe heet jij?"
    print(hello.format(owner = "Aki"))

    time.sleep (1)

    username = input("Mijn naam is:")
    print("Hallo " + username, "hier is je datum ")

    time.sleep (1)

    import datetime

    x = datetime.datetime.now()

    print("vandaag is het " + x.strftime("%d ") + x.strftime ("%B"))
    while True:
     time.sleep( 2 )

     antwoord1 = input("ik kom uit \n A Amsterdam \n B Haarlem \n C Utrecht \n antwoord: ")
     if ( antwoord1 == "A"):
        print("goed")
     elif ( antwoord1 == "B"):
        print("fout")
     elif ( antwoord1 == "C"):
        print("fout")
     time.sleep( 2 )
        
     antwoord2 = input("Hoe oud ben ik? \n A 18 \n B 16  \n C 17 \n antwoord: ")
     if ( antwoord2 == "A"):
         print("fout")
     elif ( antwoord2 == "B"):
        print("fout")
     elif ( antwoord2 == "C"):
        print("goed")
     time.sleep( 2 )
     antwoord3 = input("Wanneer ben ik jarig \n A 24 mei \n B 25 mei \n C 26 mei \n antwoord:")
     if ( antwoord3 == "A"):
         print("goed")
     elif ( antwoord3 == "B"):
        print("fout")
     elif ( antwoord3 == "C"):
        print("fout")
    
    
