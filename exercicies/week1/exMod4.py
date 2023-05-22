# MODULO 4 - EX01
def show_number_int():
    try:
        number = int(input("Digite um número inteiro: "))
        print("O número digitado foi:", number)
    except ValueError:
        print("Você não digitou um número inteiro!")
        
# MODULO 4 - EX02
def show_number_float():
    try:
        number = float(input("Digite um número REAL: "))
        if int(number) == number:
            raise ValueError("O numero NÃO é REAL!")
        print("O número digitado foi:", number)
    except ValueError as error:
        print(error)
        
# MODULO 4 - EX03
def sum_numbers():
    try:
        listNumber = list([int(input("Digite um numero:")),
                           int(input("Digite um numero:")),
                           int(input("Digite um numero:"))])
        sum = 0
        for number in listNumber:
            sum += number
        print(f'A soma dos numeros é: {sum}')
    except ValueError as e:
        print(e)

# MODULO 4 - EX04
def square_numb():
    try:
        number = float(input('Digite um numero para saber o quadrado do mesmo:'))
        number = number**2
        print(number)
    except ValueError as e:
        print(e)

# MODULO 4 - EX05
def part_numb():
    try:
        number = float(input("Digite um número REAL: "))
        if int(number) == number and not '.':
            raise ValueError("O numero NÃO é REAL!")
        print("A quinta parte do numero é:", (number/5))
    except ValueError as error:
        print(error)
       
# MODULO 4 - EX06
def temp_c_to_f():
    try:
        tempc = float(input('Digite a temperatura em graus Celsius: '))
        tempf = float(tempc * 1.8 + 32)
        print(f'Temperatura em Fahrenheit: {tempf}')
    except ValueError as error:
        print(error)
        
# MODULO 4 - EX07
def temp_f_to_c():
    try:
        tempf = float(input('Digite a temperatura em graus Fahrenheit: '))
        tempc = float((tempf-32) * 1.8)
        print(f'Temperatura em Celsius: {tempc}')
    except ValueError as error:
        print(error)

# MODULO 4 - EX08  ##########
def temp_k_to_c():
    try:
        tempk = float(input('Digite a temperatura em graus Kelvin: '))
        tempc = float(tempk - 273)
        print(f'Temperatura em Celsius: {tempc}')
    except ValueError as error:
        print(error)

# MODULO 4 - EX09  ##########
def temp_k_to_c():
    try:
        tempc = float(input('Digite a temperatura em graus Celsius: '))
        tempk = float(tempc + 273)
        print(f'Temperatura em Kelvin: {tempk}')
    except ValueError as error:
        print(error)

# MODULO 4 - EX10  ##########
def velocity_km_to_ms():
    try:
        veloc_km = float(input('Digite a Velocidade em Km/h: '))
        veloc_ms = float(veloc_km/3.2)
        print(f'Velocidade em M/s: {veloc_ms}')
    except ValueError as error:
        print(error)