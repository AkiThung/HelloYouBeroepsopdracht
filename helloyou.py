import time

a = True
while a == True:
    hello = "Hey my name is {owner}. what is yours?"
    print(hello.format(owner = "Aki"))

    time.sleep (1)

    username = input("My name is:")
    print("good day sir " + username, "here is your date and time")

    time.sleep (1)

    import datetime

    x = datetime.datetime.now()

    print("today it's " + x.strftime("%d"), "van " + x.strftime ("%B"))
    while True: 
             query = input('You wanna continue? Y/N')
             Fl = query[0].lower()
             if query == '' or not Fl in ['y','n']: 
                print('just answer!') 
             else: 
                break 
    if Fl == 'y': 
            print("Hoezeeee!")
    if Fl == 'n': 
             break