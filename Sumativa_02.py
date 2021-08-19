#Simulacion
def cine():
    descuento = 0
    eTotaln = 0
#Entrada normal
    entradanP = 2900
    eTotaln = 0
#Entrada estreno
    entradaeP = 4800
    eTotale = 0
    eqEstreno = 0
#Palomitas
    pchicas = 0
    pmedianas = 0
    pgrandes = 0
#Bebidas
    bchicas = 0
    bmedianas = 0
    bgrandes = 0
    
    afiliado = int(input("¿Cliente con convenio INACAP? \n 1.SI \n 2. NO"))
    if afiliado == 1:
        descuento = 1
    elif afiliado == 2:
        print("\n Cliente no perteneze a INACAP - NO APLICA DESCUENTO \n")
    else:
        print("\n*******************************************") 
        print("\n Ingrese digitos correctos \n")
        print("*******************************************\n")
        cine()

    entrada = int(input("¿Seleccione tipo de entrada? \n 1.Normal -> $ 2.900 c/u \n 2. Estreno -> $ 4.800 c/u \n"))
    if entrada == 1:
        cantNormal = int(input("Seleccione cantidad de entradas: \n"))
        eqNormal = cantNormal*entradanP
        eTotaln = eqNormal
        if descuento == 1:
            eTotaln = eTotaln*0.70
    elif entrada == 2:
        cantEstreno = int(input("\n Seleccione cantidad de entradas:\n"))
        eqEstreno = cantEstreno*entradaeP
        eTotale = eqEstreno
        if descuento == 1:
            eTotale = eqEstreno*0.70
    else:
        print("\n*******************************************")
        print("\n Ingrese digitos correctos \n")
        print("\n*******************************************\n")
        cine()
    
    palomitas = int(input("¿Desea agregar palomitas? \n 1.SI \n 2. NO"))
    while palomitas>2:
        print("\n*******************************************")
        print("\n Ingrese digitos correctos \n")
        print("\n*******************************************\n")
    if palomitas == 1:
        tamanoP = int(input("¿Seleccione tamaño? \n 1.Pequeña -> $ 2.500. c/u \n 2. Mediana -> $ 4.500. c/u \n 3. Grande -> $ 7.800."))
        if tamanoP == 1:
            palomq = int(input("Ingrese cantidad de palomitas CHICAS:"))
            pchicas = palomq*2500
        elif tamanoP == 2:
            palomq = int(input("Ingrese cantidad de palomitas MEDIANAS:"))
            pmedianas = palomq*4500
        elif tamanoP == 3:
            palomq = int(input("Ingrese cantidad de palomitas GRANDES:"))
            pgrandes = palomq*7800

    bebidas = int(input("¿Desea agregar bebidas? \n 1.SI \n 2. NO"))
    if bebidas>2:
        print("\n*******************************************")
        print("\n Ingrese digitos correctos \n")
        print("\n*******************************************\n")
        cine()
    if bebidas == 1:
        tamanoB = int(input("¿Seleccione tamaño? \n 1.Pequeña -> $ 1.000. c/u \n 2. Mediana -> $ 1.250. c/u \n 3. Grande -> $ 2.000."))
        while tamanoB >3:
            print("Ingrese digito correcto...")
            tamanoB = int(input("¿Seleccione tamaño? \n 1.Pequeña -> $ 1.000. c/u \n 2. Mediana -> $ 1.250. c/u \n 3. Grande -> $ 2.000."))
        if tamanoB == 1:
            bebidasq = int(input("Ingrese cantidad de bebidas CHICAS:"))
            bchicas = bebidasq*1000
        elif tamanoB == 2:
            bebidasq = int(input("Ingrese cantidad de bebidas MEDIANAS:"))
            bmedianas = bebidasq*1250
        elif tamanoB == 3:
            bebidasq = int(input("Ingrese cantidad de bebidas GRANDES:"))
            bgrandes = bebidasq*2000
    totalb = int(bchicas+bmedianas+bgrandes)
    totale = int(eTotaln+eTotale)
    totalp = int(pchicas+pmedianas+pgrandes)
    total = int(totalb+totalp+totale)

    print("\n*******************************************\n")
    print("\n Total a pagar $:",total,"\n")
    pay = int(input("\n Monto en efectivo $:"))
    while pay<total:
        print("\n Monto insuficiente. Reintente...")
        print("\n Total a pagar $:",total,"\n")
        pay = int(input("\n Monto en efectivo $:"))
    print("\n Vuelto $:",pay-total,"\n")
    print("\n*******************************************\n")
    print("\n ****GRACIAS POR SU PREFERENCIA**** \n")
    
cine()