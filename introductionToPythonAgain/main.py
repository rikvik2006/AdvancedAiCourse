print("ciao")

normal_variabile = 1


def sum(a, b):
    global normal_variabile
    normal_variabile += 5
    print(normal_variabile)
    a += 1
    b += 1
    return a + b


def media(*numbers):
    # La varaibile numbers è una tupla
    return sum(*numbers) / len(numbers)


a = 1
b = 2
result = sum(a, b)
print("⭐", result)
print("😁", a, b)
