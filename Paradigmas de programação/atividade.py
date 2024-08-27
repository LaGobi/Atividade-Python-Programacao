#Programação procedural
def fatorial (n):
    if n == 0:
        return 1
    else:
        return n * fatorial (n-1)
print("fatorial de 5 (procedual):", fatorial(5))
# Programação orientada a objetos
class Fatorial:
    def calcular (self, n):
        if n == 0:
            return 1 
        else:
            return n * self.calcular (n-1)
        f = Fatorial ()
        print("Fatorial de 5 (orientado a objetos):", f.calcular(5))