import random

isRunning = True

while (isRunning == True):
    print("Herhaal!")
    if ( random.randrange(0, 2) == 1 ):
        isRunning = False
else:
    print("Doe als laatste dit")


print("einde programma")


#INDEX       0     1    2     3
lijstA = ["tekst", 1, True, 44.05]
lijstB = ["Dit", "is", "een", "reeks"]

print(lijstA)
print(lijstA[3])

print(lijstB)
lijstB[1] = "VERANDERT!"
print(lijstB)

#Door lijst B heen gaan:
for waarde in lijstB:
    print("Dit is waarde:", waarde)



lijstGrootte = len(lijstA)
print("lijstA is", lijstGrootte, "lang")
print("-----------------------------------------------------")

for waarde in lijstB:
    waarde = "iets"
    print(waarde)

print(lijstB)

for waarde in range(5):
    print("LEUK, waarde is", waarde)
