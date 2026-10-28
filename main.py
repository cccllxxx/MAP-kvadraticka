import math
def main():
    a:float = float(input("Zadaj a: "))
    b:float = float(input("Zadaj b: "))
    c:float = float(input("Zadaj c: "))
    print(f"tvar rovnice je {a}x² {b:+}x {c:+} = 0")
    D = b**2 - 4*a*c
    if a == 0:
        print("rovnica je linearna, riesim iba kvadraticku")
    elif D <0:
        print(f"Rovnica nema riesenie, diskriminant je {D}")
    elif D==0:
        print(f"koren je {x1:.2f} {x2}")
    else:
        x1 = (-b+math.sqrt(D))/(2*a)
        x2 = (-b-math.sqrt(D))/(2*a) 
        print(f"x1 je {x1:.2f}\nx2 je {x2:.2f}")
        
if __name__ == "__main__":    
    main()
    