
""" def main(): 
    nombre = input("Digite el Nombre ==> ")
    edad = int(input("Digite la edad: ")) 
    print(f"Mi nombre es: {nombre} y mi edad es: {edad}")




if __name__ == "__main__":
     main()
 """
#nombre, salario, dias_trabajados. Calcular el sueldo a pagar
#Tipos de funciones: sin parametros, con parametros, con o sin retorno de valores
#sin parametros

""" def calcularSueldo():
    nombre = input("Digite el Nombre ==> ")
    salario = int(input("Digite el salario: ")) 
    dias_trabajados = int(input("Digite los dias trabajados: ")) 

    sueldo=((salario/30)*dias_trabajados)

    print (f"Su nombre es: {nombre} y el sueldo a pagar es: {sueldo:.0f}")

def main(): 

    calcularSueldo()

if __name__ == "__main__":
     main()
 """

 #con parametros

def calcularSueldo(salario, dias_trabajados):
    sueldoPagar=((salario/30)*dias_trabajados)
    return sueldoPagar

def main(): 
    SALARIO_MIN = 1000000
    SUB_ALIM = 120000
    SUB_TRANSP = 80000
    BONO = 50000
    nombre = input("Digite el Nombre ==> ")
    salario = int(input("Digite el salario: ")) 
    dias_trabajados = int(input("Digite los dias trabajados: ")) 
    sueldoPagar = calcularSueldo(salario, dias_trabajados)

    if salario < (SALARIO_MIN * 2):
        sueldoPagar= sueldoPagar + SUB_ALIM + SUB_TRANSP
    else:
        sueldoPagar = sueldoPagar + BONO


    print (f"Su nombre es: {nombre} y el sueldo a pagar es: {sueldoPagar:.0f}")

if __name__ == "__main__":
    main()

#Condicionales

