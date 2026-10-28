import math
from common.utils import get_number
#funkcia vrat diskriminant, funkcia vrat vysledok

def diskriminant(a:float, b:float, c:float) -> float:
    return b**2 - 4*a*c

def vrat_riesenie(a:float, b:float, c:float):
    """
    funkcia podla diskriminantu zisti riesenia rovnice
    vstupne parametre:
        a,b,c:float - koeficienty rovnice
    navratova hodnota:
        entica obsahujuca text a vypocitany koren
    """
    D = diskriminant(a,b,c)
    if D <0:
        #print(f"Rovnica nema riesenie, diskriminant je {D}")
        return "ziadny", None
    elif D==0:
        x1 = (-b)/(2*a)
        #print(f"koren je {x1:.2f}")
        return "jeden", x1
    else:
        x1 = (-b+math.sqrt(D))/(2*a)
        x2 = (-b-math.sqrt(D))/(2*a)
        #print(f"x1 je {x1:.2f}\nx2 je {x2:.2f}")
        return "dva", x1, x2
    
    
def vypis_riesenie()


def main():
    a = get_number(popis="Zadaj a", nulaPovolena=False)
    b = get_number(popis="Zadaj b", nulaPovolena=True)
    c = get_number(popis="Zadaj c", nulaPovolena=True)
    print(f"tvar rovnice je {a}x² {b:+}x {c:+} = 0")
    
        
if __name__ == "__main__":    
    main()
    