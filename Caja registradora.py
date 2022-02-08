from tkinter import *
from tkinter import ttk

class Interfaz:
    
    # Genera las variables que intervendrán en el programa
    def __init__(self, ventana):
        self.ventana=ventana
        self.productos=('Galletas-$10', 'Jugo-$8','Gomitas-$9','Agua-$7', 'Chocolate-$5', 'Donas-$11')
        self.cajaCantidad=IntVar()
        self.cajaTotal=IntVar()
        self.total = 0
        self.dibujarComponentes()
             
    # Creación de la ventana y todos sus componentes
    def dibujarComponentes(self):
        # Creación de la Ventana
        self.ventana.title('Caja Registradora')
        self.ventana.geometry('650x450')
        # Creación de los Labels
        Label(self.ventana, text='Seleciona tu producto: ').place(x=10, y=10)
        Label(self.ventana, text='Selecciona la cantidad: ').place(x=10, y=60)
        Label(self.ventana, text='El total es: ').place(x=450, y=400)
        # Creación del Combo
        self.combo=ttk.Combobox(self.ventana, state='readonly')
        self.combo.place(x=10, y=35)
        self.combo['values']=self.productos
        self.combo.current(0)
        # Creación de las ventanas de Datos
        Entry(self.ventana, textvariable=self.cajaCantidad).place(x=10, y=85)
        Entry(self.ventana, textvariable=self.cajaTotal).place(x=520, y=400)
        Button(self.ventana, text='Agregar',command=self.agregarProducto).place(x=10, y=110)
        # Creación de la tabla
        self.tabla=ttk.Treeview(self.ventana, columns=('Cantidad', 'Subtotal'))
        self.tabla.heading('#0', text='Producto')
        self.tabla.heading('Cantidad', text='Cantidad')
        self.tabla.heading('Subtotal',text='Subtotal')
        self.tabla.place(x=10, y=150)
        
    def agregarProducto(self):
        texto=self.combo.get()
        datos=texto.split('-$')
        producto=datos[0]
        precio=datos[1]
        cantidad=self.cajaCantidad.get()
        subtotal=int(precio)*int(cantidad)
        self.tabla.insert('',END,text=producto, values=(cantidad, '$'+str(subtotal)))
        self.total=self.total+subtotal
        self.cajaTotal.set('$'+str(self.total))
           
obj = Interfaz(Tk())
obj.ventana.mainloop()
