
match = "Esto es un match variable"
n = 19
type=10 
print(type)
_ = 0
print(_)
match n: 
    case 42:
        print("El numero es 42")
    case 19:
        print("El numero es 19")
    case _:
        print("El numero no es 42 ni 19")

print (match)