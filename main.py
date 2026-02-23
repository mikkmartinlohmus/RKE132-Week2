""" day = input ("Mis päev on homme? (tööpaev/puhkepäev):")

if day == "tööpäev":
    print("Ma lähen magama, head ööd!")
elif day == ("puhkepäev"):
    print("Veel üks osa Netflixi")
else: 
    print("Vale väärtus") """

""" 
print ("Tere tulemast programmi 'Finantsnõustaja'")
print ("Sinu isiklik nõustaja ei  tee emotsionaalseid oste")

money = int(input("Kui palju raha sul praegu on?"))

if money < 2500:
    print("Sul pole piisavalt, kogu veel raha!")
elif money == 2500:
    print("Palju õnne, saad osta Iphone")
else:
    print("Saad osta Iphone 17 Pro ja raha jääb ka üle")
 """

#Sammulugeja

goal = 10000
steps = int(input("Mitu sammu oled täna teinud?"))

percent = (steps/goal) * 100

if percent < 50:
    print("Oled alles poolel teel!")
elif percent < 75:
    print("Tubli! Jätka samas vaimus")
elif percent < 100:
    print ("Väga tubli, oled lähedal!")
else: 
    print("Palju õnne, täitsid eesmärgi!")
