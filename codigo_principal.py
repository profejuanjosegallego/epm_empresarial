from funcionesEPM import registrar_usuarios,controlar_acceso,generar_mediciones,obtener_promedio,clasificar_medicion_agua


listaEmpleados=registrar_usuarios(1)
resultado_login=controlar_acceso()
if resultado_login==True:
    listaMediciones=generar_mediciones()
    promedio=obtener_promedio(listaMediciones)
    clasificacion=clasificar_medicion_agua(promedio)
    print(clasificacion)


    3225962363

    