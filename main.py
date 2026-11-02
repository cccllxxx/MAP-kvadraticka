import math
from common.utils import get_number
#funkcia vrat diskriminant, funkcia vrat vysledok

def diskriminant(a:float, b:float, c:float) -> float:
    return b**2 - 4*a*c

def vrat_riesenie(a:float, b:float, c:float) -> tuple[str, None | float] | tuple[str, float, float]:
    """
    funkcia podla diskriminantu zisti riesenia rovnice
    vstupne parametre:
        a,b,c:float - koeficienty rovnice
    navratova hodnota:
        ntica obsahujuca text a vypocitany koren
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
    
    
def vypis_riesenie(vysledok:tuple) -> None :
    """
    vypise riesenie rovnice
    """
    match vysledok:
        case ("ziadny",None):
            print("Rovnica nema ziadny koren")
        case ("jeden", x1):
            print(f"rovnica ma jeden koren, x = {x1}")
        case ("dva", x1,x2):
            print(f"rovnica ma 2korene\nx1 = {x1}\nx2 = {x2}")
        case _:
            raise ValueError("Neznama n-tica")


def main():
    a = get_number("Zadaj a",-100,100, False)
    b = get_number("Zadaj b",-100,100, True)
    c = get_number("Zadaj c",-100,100, True)
    print(f"tvar rovnice je {a}x² {b:+}x {c:+} = 0")
    riesenie:tuple = vrat_riesenie(a,b,c)
    vypis_riesenie(riesenie)
 
 
 
 
if __name__ == "__main__":    
    main()
    