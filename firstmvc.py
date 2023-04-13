#Programa que calcula los descuentos y bonos con los que cuenta
#una persona según su estrato económico. 

from tkinter import *

# ---------Modelo----------

class Persona:
    def __init__(self, estrato):
        self.estrato = estrato

    def calcular_descuentos(self):
        descuentos = {}
        if self.estrato == 1:
            descuentos["descuento_compra"] = 0.05
            descuentos["descuento_ropa"] = 0.10
            descuentos["bono_regalo"] = 10000
        elif self.estrato == 2:
            descuentos["descuento_compra"] = 0.03
            descuentos["descuento_ropa"] = 0.05
            descuentos["bono_regalo"] = 5000
        else:
            descuentos["descuento_compra"] = 0.01
            descuentos["descuento_ropa"] = 0.03
            descuentos["bono_regalo"] = 0
        return descuentos

# ------------Vista-------------

class Interfaz():
    def __init__(self, master) -> None:
        self.master = master
        master.title("Prueba")
        master.geometry("300x200")

        # Etiqueta de estrato
        self.labelEstrato = Label(master, text="Estrato:")
        self.labelEstrato.grid(row=0, column=0, padx=10, sticky='e')
        
        #Etiqueta de error en la entrada.
        self.labelError = Label(master, text="")
        self.labelError.grid(row=0, column=3, padx=1, sticky='e')

        #Etiqueta de descuentos
        self.labelDescuentos = Label(master, text="",justify=LEFT)
        self.labelDescuentos.grid(row=3, column=1, padx=10)

        # Cuadro de entrada de estrato
        self.entEstrato = Entry(master, width=5)
        self.entEstrato.grid(row=0, column=1, sticky='w')

        # Crear el boton aceptar
        self.botonAceptar = Button(
            master, text="Aceptar", command=self.aceptar)
        self.botonAceptar.grid(row=2, column=1, pady=5)

    def aceptar(self):
        controlador.aceptar()
       
                
# ------Controlador-------

class Controller():
    def __init__(self,interfaz) -> None:
        self.interfaz = interfaz

    def aceptar(self):
        #Validación de la entrada
        self.interfaz.labelDescuentos.config(text="")
        try:
            self.estrato = int(self.interfaz.entEstrato.get())
        except ValueError:
            self.interfaz.labelError.config(text="Ingrese una opción válida (1-5).", fg='red')
        else:
            if self.estrato not in [1,2,3,4,5]:
                self.interfaz.labelError.config(text="Ingrese una opción válida (1-5).", fg='red')
            else:
                #Creación del objeto usuario a partir de la clase Persona con su No. de estrato
                self.interfaz.labelError.config(text="")
                self.usuario = Persona(self.estrato)
                self.descuentos = ''
                
                #Presentación de los datos del diccionario 'descuentos'
                for k,v in self.usuario.calcular_descuentos().items():
                    if v < 1:
                        self.descuentos += f"{k}: {v*100:.2f}% "+ "\n"
                    else:
                        self.descuentos += f"{k}: $ {v}"
                self.interfaz.labelDescuentos.config(text=self.descuentos)
        
#Inicio de la aplicación
if __name__ == '__main__':
    root = Tk()
    interfaz = Interfaz(root)
    controlador = Controller(interfaz)
    root.mainloop()
