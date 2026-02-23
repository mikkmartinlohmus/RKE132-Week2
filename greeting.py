pere_nimi = input ("Sisesta enda perekonnanimi:")
sugu = input ("Sisesta enda sugu (m/n): ")


if sugu == "m":
    print (f"Tere, härra {pere_nimi}!")
elif sugu == "n":
    print (f"Tere, proua {pere_nimi}!")
else: 
    print (f"Tere tulemast, {pere_nimi}! (sugu ei olegi täthtis)")