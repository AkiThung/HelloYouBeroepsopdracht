import time


a = True
while a == True:
    Welkom = " hallo welkom bij mijn textbased application over een vluchteling"
    print(Welkom)

   
    while True:
     

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
            vraag6()
         elif ( antwoord3 == "B"):
            vraag7()

     def vraag4():
         antwoord4 = input("Je wordt nogal depressief van de wereld waar je nu in zit. Mentaal word je ook een beetje gek omdat je nooit echt veilig hier zou zijn. \n Wat doe je? \n A Je besluit te vluchten naar het buitenland. \n B Je pleegt zelfmoord")
         if ( antwoord4 == "A"):
            vraag6()
         elif ( antwoord4 == "B"):
            EINDE_I()

     def vraag5():
         antwoord5 = input("Je hebt je studie architectuur afgerond. Maar je weet niet zo goed wat je wil doen. Je voelt je niet veilig in Afghanistan dus je besluit te proberen naar een ander land te gaan. Je bent nu op z’n minst hoog opgeleid. \n Waar ga je naartoe? \n A Istanbul.\n B Dubai.")
         if ( antwoord5 == "A"):
            EINDE_II()
         elif ( antwoord5 == "B"):
            vraag8()
            
     def vraag6():
         antwoord6 = input("Je moet vluchten naar het buitenland. Maar ga je dit zelf proberen of ga je proberen een mensensmokkelaar te vinden? \n A Je gaat t zelf proberen. \n B Je zoekt een mensensmokkelaar.")
         if ( antwoord6 == "A"):
            vraag10()
         elif ( antwoord6 == "B"):
            vraag11()

     def vraag7():
         antwoord7 = input("Je gaat nieuw werk zoeken maar er is veel werkloosheid. Het blijkt dat er eigenlijk niks meer mogelijk is. De enige mogelijkheid om iets te verdienen is het leger. \n A Je vindt het allemaal te veel worden, je pleegt zelfmoord. \n B Je gaat het leger in.  ")
         if ( antwoord7 == "A"):
            EINDE_I()
         elif ( antwoord7 == "B"):
            vraag9()

     def vraag8():
         antwoord8 = input("Je verhuist naar Dubai. Het niveau is daar extreem hoog en je komt niet aan werk, je verdient echt te weinig om te overleven in deze dure stad.  Wat doe je? \n A Je besluit zelfmoord te plegen. \n B Je besluit alsnog naar Istanbul te gaan.")
         if ( antwoord8 == "A"):
            EINDE_I()
         elif ( antwoord8 == "B"):
            EINDE_II()
             
     def vraag9():
         antwoord9 = input("Je begint met een 2-jarige training, daarna word je ingezet om een terroristische groep te bestrijden. Je hebt een hele goede vriend gemaakt tijdens je training. Je ziet hem echt als een broeder. Op een dag tijdens deze missie betreden jullie samen met jullie team een vijandig gebied. Je vriend wordt neergeschoten en valt neer. Natuurlijk probeer je hem te helpen dus je rent snel naar hem toe en probeert hem te helpen. Je twijfelt om hem naar veiligheid te brengen of hem eerst eerste hulp te geven en te wachten tot de nacht. \n A Je wacht hier en je verpleegt hem ondertussen, in de nacht ren je weg met hem. \n B Je rent nu met hem weg.")
         if ( antwoord9 == "A"):
            EINDE_III()
         elif ( antwoord9 == "B"):
            EINDE_V()

     def vraag10():
         antwoord10 = input("Je probeert zelf weg te vluchten maar neem je je familie mee? \n A Ja je neemt je familie mee. \n B Nee je gaat alleen omdat het nogal gevaarlijk is. ")
         if ( antwoord10 == "A"):
            vraag13()
         elif ( antwoord10 == "B"):
            vraag14()

     def vraag11():
         antwoord11 = input("e hebt een mensensmokkelaar geregeld, je kan hem betalen met je laatste beetje geld. Hij belooft je naar Londen te brengen, hij brengt je eerst naar Istanbul met een nep paspoort. Daar moet je voor dagen binnen wachten met een paar andere mensen. Je mag niet naar buiten en je mag geen geluid maken. Je vindt de situatie onmenselijk en twijfelt om zelf door te vluchten of te wachten wat doe je?\n A Je vlucht zelf. \n B Wacht op de mensensmokkelaar.  ")
         if ( antwoord11 == "A"):
            vraag12()
         elif ( antwoord11 == "B"):
            vraag15()

     def vraag12():
         antwoord12 = input("Je hebt besloten om vanaf Istanbul toch zelf te vluchten. Er zijn alleen verassend weinig mogelijkheden. Je kan of over de normale grenzen over land proberen te gaan. Of je kan de boot over de middellandse zee nemen. \n A Je pakt de boot.  \n B Je gaat over de normale grenzen.")
         if ( antwoord12 == "A"):
            vraag16() 
         elif ( antwoord12 == "B"):
              EINDE_VI()

     def vraag13():
         antwoord13 = input("Je hebt besloten met je familie te vluchten. Maar wat ga je nu doen? Het is moeilijk om met zo een grote groep te vluchten. Je hebt geen andere keuze dan maar te lopen. Je kan naar t noorden of westen.\n A noorden \n B westen ")
         if ( antwoord13 == "A"):
            EINDE_VII()
         elif ( antwoord13 == "B"):
            vraag17()

     def vraag14():
         antwoord14 = input("Je hebt besloten dat je alleen gaat vluchten omdat dat veiliger is, wat doe je? \n A Je lift met iemand mee. \n B Je gaat lopen. ")
         if ( antwoord14 == "A"):
            vraag17()
         elif ( antwoord14 == "B"):
            EINDE_VIII()

     def vraag15():
         antwoord15 = input("Je hebt gewacht op de mensensmokkelaar, na het lange wachten moet je een onmenselijke reis maken door meer dan een week in de achterkant van een busje te zitten zonder licht. Je kan er alleen 1x in de paar uur uit voor een plaspauze. Je komt uiteindelijk in Amsterdam terecht, maar dat weet je niet. De smokkelaar moet nog wat regelen en zegt expliciet te blijven zitten maar t duurt je te lang. \n A Je stapt uit zonder te weten waar je bent. \n B Je blijft wachten totdat hij terugkomt. ")
         if ( antwoord15 == "A"):
            EINDE_IV()
         elif ( antwoord15 == "B"):
            vraag18()

     def vraag16():
         antwoord16 = input("Je hebt besloten met de boot te gaan maar de enige betrouwbare boot gaat pas over een maand. Alleen voor een maand illegaal in Turkije blijven is moeilijk. Je kan ook een onbetrouwbare boot nemen over 3 dagen. \n A Wachten op de boot. \n B Onbetrouwbare boot. ")
         if ( antwoord16 == "A"):
            vraag20()
         elif ( antwoord16 == "B"):
            EINDE_IX()

     def vraag17():
         antwoord17 = input("Je komt aan in Istanbul maar daar blijkt dat je niet welkom bent en je wordt terug gestuurd naar huis. \n A je reist door (illegaal). \n B Je pleegt zelfmoord.")
         if ( antwoord17 == "A"):
            vraag20()
         elif ( antwoord17 == "B"):
            EINDE_I()

     def vraag18():
         antwoord18 = input("Je hebt gewacht tot de smokkelaar terugkomt, hij blijkt te hebben geregeld dat je naar London kan je zit nogmaals dagen in de auto in onmenselijke situaties, je bent de tunnel door en je bent in Engeland aangekomen. Je hebt je eerste plaspauze na tijden. Maar je bent kapot  \n A Je rent weg en zoekt zelf naar asiel. Je bent namelijk al in Engeland. /n B Je blijft zitten totdat je echt in London bent ")
         if ( antwoord18 == "A"):
            vraag19()
         elif ( antwoord18 == "B"):
            EINDE_X() 
             
     def vraag19():
         antwoord19 = input("Naar welke stad ga je? \n A Southampton. \n B Brighton.")
         if ( antwoord19 == "A"):
            EINDE_XI()
         elif ( antwoord19 == "B"):
            EINDE_XII()
             
     def vraag20():
         antwoord20 = input("Je komt aan in Italië, wil je doorreizen of blijf je hier? \n A Blijf in Italië. \n B Doorreizen. ")
         if ( antwoord20 == "A"):
            EINDE_XIII()
         elif ( antwoord20 == "B"):
            vraag21()
             
     def vraag21():
         antwoord21 = input("Naar welk land wil je doorreizen? \n A Duitsland \n B Frankrijk")
         if ( antwoord21 == "A"):
            EINDE_XIV()
         elif ( antwoord21 == "B"):
            EINDE_XV()
             
     def EINDE_I():
         print("Dood door zelfmoord")
         time.sleep( 2 )
     
     def EINDE_II():
         print("Je wordt een groot respecteerde architect in Istanbul. Je familie en jij leven goed. Je hebt nog wel heel wat trauma's en nog steeds een licht gevoel van onveiligheid. ")

     def EINDE_III():
         print("Je hebt een heldendaad verricht en je wordt gerespecteerd door veel mensen. Je zal nooit meer hoeven te werken aangezien je wordt uitbetaalt voor deze heldendaad. Je voelt je nog wel extreem onveilig aangezien je niks meer durft te doen. Trauma's hebben je overgenomen en je bent bang dat je zal worden vermoord voor je daden. ")
         time.sleep( 2 )

     def EINDE_IV():
         print("Je blijkt in Amsterdam uitgestapt te zijn je vraagt hier asiel aan. Je bent volkomen veilig, maar je voelt je eenzaam. Het zal nog wel even duren voordat de rest van je familie hier is en je kent hier niemand. ")
         time.sleep( 2 )

     def EINDE_V():
         print("Je wordt neergeschoten in de poging om je vriend te helpen. ")
         time.sleep( 2 )

     def EINDE_VI():
         print("Je probeert over land te vluchten maar je wordt gespot en rent weg. Je zit nu vast in Turkije dus je besluit hier maar te leven. ")
         time.sleep( 2 )

     def EINDE_VII():
         print("Je bent naar het noorden gevlucht, het blijkt hier echter extreem onveilig te zijn en je wordt vermoord door een terroristische groep. ")
         time.sleep( 2 )

     def EINDE_VIII():
         print("Je gaat dood aan hongersnood aangezien je lopend probeert te vluchten, je liep door een woestijn heen en had niet genoeg voedsel en drinken bij je. ")
         time.sleep( 2 )

     def EINDE_IX():
         print("Je verdrinkt, je hebt niet de juiste boot genomen en hij is gezonken. ")
         time.sleep( 2 )

     def EINDE_X():
         print("Je eindigt in London, je hebt moeite met het asiel aanvragen maar na een tijdje is het goed gekomen en heb je een huis ergens in een buitenwijk ")
         time.sleep( 2 )

     def EINDE_XI():
         print("Je eindigt in Southampton, je hebt moeite met het asiel aanvragen maar na een tijdje is het goed gekomen en heb je een huis ergens in een leuke wijk ")
         time.sleep( 2 )
         
     def EINDE_XII():
         print("Je eindigt in Brighton, je hebt moeite met het asiel aanvragen maar na een tijdje is het goed gekomen en heb je een huis ergens in drukke maar gezellige wijk. ")
         time.sleep( 2 )

     def EINDE_II():
         print("Je eindigt in Italië je hebt moeite met het asiel aanvragen aangezien er nogal veel vluchtelingen zijn, je wordt doorgestuurd naar Frankrijk waar je uiteindelijk je asiel regelt. ")
         time.sleep( 2 )

     def EINDE_XIII():
         print("Je eindigt in Duitsland waar je thuis voelt en snel je asiel geregeld hebt, je familie is er ook snel aangezien het allemaal heel makkelijk gaat. ")
         time.sleep( 2 )
     
     def EINDE_XIV():
         print("Je bent geëindigd in Frankrijk waar je je asiel regelt, je voelt je nog wel eenzaam maar er wordt beloofd snel iets geregeld te worden. ")
         time.sleep( 2 )
     
     
     antwoord1 = input("Je begint als een normale burger in Kandahar (Afghanistan). Je doet een studie architectuur. Maar je familie heeft geld nodig.\n Wat doe je? \n A je kiest ervoor om je studie te vervcolgen. \n B je kiest ervoor om internationaal werk te gaan doen \n C je gaat op een markt werken.")
     if ( antwoord1 == "A"):
        vraag5()
     elif ( antwoord1 == "B"):
        vraag2()
     elif ( antwoord1 == "C"):
        vraag4()
    

    
    
