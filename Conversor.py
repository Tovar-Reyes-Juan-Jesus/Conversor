#App para convertir Pies a Metros usando Tkinter
#Tovar Reyes Juan de Jesus
#23/Feb/2023.
#la raiz es el padre!!!!
from tkinter import *     #estos son los paquetes a importar.
from tkinter import ttk

class Conversor:
    #__init__ es el contructor pero para la version de python. siempre el primer parametro siempre sera el "self"
    #tipo de constructor de la clase
    def __init__(self, raiz):
        raiz.title("Conversor de Pies a Metros")

        self.pies = StringVar() #forma de declarar el objeto.
        self.metros = StringVar()

        mainFrame = ttk.Frame(raiz, padding="14 14 14 14") #mainframe es el hijo de raiz "entry son las cajas de texto" padding( Izq, arriba, derecha, abajo)
        mainFrame.grid(column=0, row=0)

        piesEntry= ttk.Entry(mainFrame, width= 7,textvariable=self.pies)#cuadro para ingresar texto o caja de texto
        piesEntry.grid(column=1 , row=0, sticky=(W, E))# el grid lo agrega a el frame.

        ttk.Label(mainFrame, text="pies").grid(column=2, row=0 ) #esto es un objeto anonimo que no necesita. sticky=(W) es para mantenerlo en u cierto lugar, si no tiene coordenada se centra.
        ttk.Label(mainFrame, text="Son equivalentes a", padding=(5, 10, 5, 10)).grid(column=0, row=1)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1, row=1) #SIEMPRE QUE USEMOS UNA VARIABLE UTILIZAMOS UN SELF
        ttk.Label(mainFrame, text="Metros").grid(column=2, row=1)
        
        ttk.Button(mainFrame, text= "Calcular", command=self.calcular).grid(column= 2, row= 2) # este en command es self para llamarse a si mismo.
        piesEntry.focus()
        #HACER LA OPERACION PRESIONANDO <ENTER> 
        raiz.bind("<Return>", self.calcular)
    #try es para intentar una accion.
    def calcular(self, *args): #args es un arreglo de argumentos para poder detectar los eventos por las teclas y reciba una serie de argumentos.
        print("Boton presionado") 
        #self es el this en python
        piesUsuario = self.pies.get() #SIEMPRE DEVUELVE UNA CADENA.
         #CONVERSION DE CADENA A FLOTANTE.
        print("pies ingresados: ", piesUsuario)
        try:
             piesFlotantes = float(piesUsuario)
             metros = piesFlotantes*0.3048
             print("Metros ", metros)
             self.metros.set(metros)
             
        except:#esto es para poder excepcionar un error en particular.
            print("No es un dato valido.")
            self.pies.set("")


        #cualquier logica de tkinter va a hacer la misma logica.
        #la paqueteria de tkinter nos facilita en la paqueteria, nos facilita un tipo de objeto que automaticamente va a guardar el dato y actualizarlo.

if __name__=="__main__": #este sirve para declararlo como main por asi decirlo.

     print("Este es el archivo principal.")
     print("Nada mas se mostrara esto si es el principal.")



