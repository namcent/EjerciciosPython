'''Pedir al usuario que ingrese un número por pantalla.
Validar que el dato ingresado sea un número, caso contrario imprimir por pantalla una leyenda con el error y volver a solicitar al usuario la info.
Si el dato ingresado es un número entero, calcular e imprimir por pantalla cuantas gruesas, docenas y unidades son (una gruesa son 12 docenas o 144 unidades). Ejemplo: 53783 son 373 gruesas, 5 docenas y 11 unidades.
También calcular e imprimir por pantalla si el número es primo.
Saludar al usuario e informarle cuantos días faltan para el invierno.'''

from datetime import datetime

def main(): 
    print("\n¡Bienvenido!")
    numero=ingresar()
    contar_gruesas_doc_unid(numero)
    es_primo(numero)
    dias_para_el_invierno()

def ingresar():
    num=None
    var=False
    while num==None:
        numero=input("\nPor favor ingrese un numero: ")
        for tipo in (int, float, complex):
            try:
                num=tipo(numero)
                var=True
                return num
                break
            except ValueError:
                pass
        if (var==False):
            print ("\nError. Usted no ha ingresado el tipo de valor solicitado. ")


def contar_gruesas_doc_unid(numero):
    if type(numero)==int:
        gruesas=numero//144
        docenas=(numero%144)//12
        unidades=numero%12
        print("\nEl numero que ingreso son %s gruesas, %s docenas y %s unidades." % (gruesas, docenas, unidades))
        
def es_primo(numero):
    if type(numero)==int:
        var=False
        for i in range(2, numero):
            if (numero%i)==0:
                break
            else:
                var=True
        if var==True:
            print("\nEl numero es primo.")
        else:
            print("\nEl numero no es primo.")
    

def dias_para_el_invierno():
    hoy=datetime.now()
    invierno=datetime(2020, 6, 21)
    dif=str(invierno-hoy)
    mensajesep=dif.split()
    tiemposep=(mensajesep[2]).split(':')
    segundossep=(tiemposep[2]).split('.')
    dias=mensajesep[0]
    horas=tiemposep[0]
    minutos=tiemposep[1]
    segundos=segundossep[0]
    print(f"\n¡Hola! Faltan {dias} dias, {horas} horas, {minutos} minutos y {segundos} segundos para el invierno.\n")

if __name__ == ('__main__'):
	main()