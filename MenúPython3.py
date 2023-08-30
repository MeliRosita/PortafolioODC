menuprincipal=int(input("Menú Principal: \n 1-Suma \n 2-Resta \n 3-División \n 4-Multiplicación \n 5-Conversión de binario a decimal \n 6-Conversión de decimal a binario \n 0- Salir \n"))
while menuprincipal !=0:
    
    if menuprincipal ==1:
        print("Suma")
    elif menuprincipal ==2:
        print("Resta")
    elif menuprincipal ==3:
        print("División")
    elif menuprincipal ==4:
        print("Multiplicación")
    elif menuprincipal ==5:
        print("Conversión de binario a decimal")
    elif menuprincipal ==6:
        print("Conversión de decimal a binario")
    else:
        print("Opción no valida, escriba un número del cero al seis")
        
    menuprincipal=int(input("Menú Principal: \n 1-Suma \n 2-Resta \n 3-División \n 4-Multiplicación \n 5-Conversión de binario a decimal \n 6-Conversión de decimal a binario \n 0- Salir \n"))