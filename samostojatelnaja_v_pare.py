from math import * 
from random import * 
print("Isikukoodi kontrolimine")
text=input("Palun kirjuta teieisikukoodi: ")
n=len("text")
if n==11 and text.isdigit():
    print("sobib")
else:
    print("Sa kirjutasid palun või vähe sümboleid")
