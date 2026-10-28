import math
from common.utils import get_number
#funkcia vrat diskriminant, funkcia vrat vysledok

def diskriminant(a:float, b:float, c:float) -> float:
    return b**2 - 4*a*c


def main():
    a = get_number(popis="Zadaj a", nulaPovolena=False)
    b = get_number(popis="Zadaj b", nulaPovolena=True)
    c = get_number(popis="Zadaj c", nulaPovolena=True)
    print(f"tvar rovnice je {a}x² {b:+}x {c:+} = 0")
    D = diskriminant(a,b,c)
    print(D)
    x1 = (-b+math.sqrt(D))/(2*a)
    x2 = (-b-math.sqrt(D))/(2*a) 
    if a == 0:
        print("rovnica je linearna, riesim iba kvadraticku")
    elif D <0:
        print(f"Rovnica nema riesenie, diskriminant je {D}")
    elif D==0:
        print(f"koren je {x1:.2f}")
    else:
        print(f"x1 je {x1:.2f}\nx2 je {x2:.2f}")
        
if __name__ == "__main__":    
    main()
    