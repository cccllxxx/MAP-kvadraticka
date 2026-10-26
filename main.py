def main():
    a:int = int(input("Zadaj a: "))
    b:int = int(input("Zadaj b: "))
    c:int = int(input("Zadaj c: "))
    print(f"tvar rovnice je {a}x² + {b}x + {c} = 0")
    
    D = b**2 - 4*a*c
    if D <0:
        print(f"Rovnica nema riesenie, diskriminant je {D}")
        
        
        
if __name__ == "__main__":    
    main()