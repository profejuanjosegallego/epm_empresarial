import random

def registrar_usuarios(numeroEmpleados): #Funcion que retorna una lista de N empleados
    listaUsuarios=[]
    for i in range(numeroEmpleados):
        diccionarioUsuario={
            "id":input("➕ id: "),
            "nombre":input("🤖 nombre: "),
            "documento":input("😶‍🌫️ documento: "),
            "eps":input("😎 eps: "),
            "telefono":input("🔭 telefono: "),
            "correo":input("📧 correo: "),
            "contraseña":input("🐍 contraseña: ")
        }
        listaUsuarios.append(diccionarioUsuario)
    return(listaUsuarios)


def controlar_acceso(): #Funcion que devuelve TRUE /FALSE dependiendo de los datos ingresados
    correoBD="correo@gmail.com"
    contraseñaBD="admin123*"
    for intento in range(1,4):
        correoDigitado=input("Escribe tu correo: ")
        contraseñaDigitada=input("Escribe tu contraseña: ")
        if correoDigitado==correoBD and contraseñaDigitada==contraseñaBD:
            print("Bienvenido")
            return True
            break
        else:
            print("revisa por favor")
            return False


def generar_mediciones(): #Funcion que devuelve una lista de mediciones
    listaMediciones=[]
    for i in range(200):
        medidaNivelAgua=random.randint(0,800)
        listaMediciones.append(medidaNivelAgua)
    return(listaMediciones)


def obtener_promedio(listaMediciones): #FUNCION DEVUELVE UN promedio de una lista de numeros
    medicionAguaPromedio=sum(listaMediciones)/len(listaMediciones)
    return medicionAguaPromedio

def clasificar_medicion_agua(medicionAguaPromedio): #Funcion para clasificar el promedio de nvel de agua
    if medicionAguaPromedio > 0 and medicionAguaPromedio <=250 :
        return("Estamos operando con poca agua, apaga algunas maquianrias...")
    elif medicionAguaPromedio >250 and medicionAguaPromedio <=400:
        return("Estamos operando con normalidad, puedes exigirle a la maquinaria...")
    elif medicionAguaPromedio>400:
        return("PELIGRO 💀 REVISE la opción de abrir compuertas el nivel de agua es muy elvado...")
    else:
        return("EL nivel de agua registrado no es el adecuado, revisar por favor")