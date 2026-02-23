goal = 8
glass = int(input("Mitu klaasi vett sa täana oled joonud?"))

percent = (glass/goal) * 100

if percent < 50:
    print("Joo rohkem vett, keha vajab seda!")
elif percent < 100:
    print("Tubli, jätka samas vaimus!")
else:
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")