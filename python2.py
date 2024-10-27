import math

def eh_triangulo(a, b, c):

    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

def area_triangulo(a, b, c):

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if eh_triangulo(a, b, c):
    area = area_triangulo(a, b, c)
    print(f"Os valores formam um triângulo. A área é {area:.2f}.")
else:
    print(f"Os valores {a}, {b}, {c} não formam um triângulo.")