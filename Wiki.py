import wikipedia #Esta línea importa el módulo wikipedia, que permite interactuar con la API de Wikipedia desde Python.


def main(): #Aquí se define una función llamada main. Esta función contendrá toda la lógica del programa.
    wikipedia.set_lang('es') #Esta línea configura el idioma de Wikipedia a español ('es').
    query = input("Ingresa el término que deseas buscar: ") #input() es una función que permite al usuario ingresar texto desde la consola.
    summary = wikipedia.summary(query, sentences=2) #Aquí se utiliza la función wikipedia.summary() para obtener un resumen breve del término buscado.
    print(f'Resumen de Wikipedia: {summary}') #print() es una función que muestra texto en la consola.

if __name__ == '__main__':
    main()