from math import * 
from random import * 
#1
try: 
    vanus=int(input("Kai vana sa oled?"))
    if vanus>=18:
        print("Kas te annate vanemtele loa oma Tahvelit vaadata?")
        o=(input("Jah või ei. "))
        if o.lower()=="Jah":
            print({o})
            print("See on Ligipääs teie vanematele.")
            print("Tahvel on kinni")
        elif o.upper()=="EI":
            print("Sissepääs puudub.") 
            print("Tahvel on kinni.")
    if vanus<18:
        print("Juurdepääs vanematele on automaatselt antud.")
except:
    print("Tahvel on kinni.")





from math import * 
from random import * 
#2
try:
    vanus=int(input("Kui vana sa oled?"))
except:
    print("!!!!!!")
if  vanus==19:
    luba=int(input("Kas lubate vanematele hindeid vaadata?"))

elif vanus==15 or vanus==16 or vanus==18: 
    print("Automaatne juurdepääs vanematele")
else:
    print("Viga!")








from math import * 
from random import * 
#3
print("Määrata ja tuletada suurem kahest sisestatavast arvust")
a=randint(-300,300)
b=randint(-300,300)
print(f"a={a}\nb={b}")
if a>b:
    print(f"arv {b} on suurem arv {a}") 
elif a>b:
    print(f"arv {a} on suurem arv {b}") 

print()







from math import * 
from random import * 
#4
try: 
    päev=int(input("Mis päev ja mittu tundi täna on ?"))
    if päev==1:
        n="Esmaspäev"
        n="6 tundi"
    elif päev==2:
         n="Teisipäev"
         n="8 tundi"
    elif päev==3:
         n="Kolmapäev"
         n="6 tundi"
    elif päev==4:
         n="Neljapäev"
         n="5 tundi"
    elif päev==5:
         n="Reede"
         n="7 tundi"
    elif päev==6:
         n="Lauapäev"
         n="0 tundi"
    elif päev==7:
         n="Pühapäev"
         n="0 tundi"
    else:
        n="vale number"
    print(n)
except:
    print("!!!!!!!")









from math import * 
from random import * 
print("Isikukoodi kontrolimine")
text=input("Palun kirjuta teieisikukoodi: ")
n=len("text")
if n==11 and text.isdigit():
    print("sobib")
else:
    print("Sa kirjutasid palun või vähe sümboleid")

