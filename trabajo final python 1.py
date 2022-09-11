from tkinter import *
from AsistenteIA import Asistente



root = Tk() #root = nombre de mi raiz
root.title('Ferretería "El tornillo feliz"') # nombre del titulo de mi ventana
root.resizable(False,False)
root.iconbitmap("ferretería.ico")
#---------------------------------Productos-----------------------------------

def hallar_desc():
    if obtenerCodigo.get() == "Prod1":
        obtenerDescripcion.set("Madera")
        obtenerPrecio.set(int(20))
    elif obtenerCodigo.get() == "Prod2":
        obtenerDescripcion.set("Palos")
        obtenerPrecio.set(int(15))
    elif obtenerCodigo.get() == "Prod3":
        obtenerDescripcion.set("Pegamento")
        obtenerPrecio.set(int(4))
    elif obtenerCodigo.get() == "Prod4":
        obtenerDescripcion.set("cinta")
        obtenerPrecio.set(int(5))

def hallar_desc1():
    if obtenerCodigo1.get() == "Prod1":
        obtenerDescripcion1.set("Madera")
        obtenerPrecio1.set(int(20))
    elif obtenerCodigo1.get() == "Prod2":
        obtenerDescripcion1.set("Palos")
        obtenerPrecio1.set(int(15))
    elif obtenerCodigo1.get() == "Prod3":
        obtenerDescripcion1.set("Pegamento")
        obtenerPrecio1.set(int(4))
    elif obtenerCodigo1.get() == "Prod4":
        obtenerDescripcion1.set("cinta")
        obtenerPrecio1.set(int(5))
        
def hallar_desc2():
    if obtenerCodigo2.get() == "Prod1":
        obtenerDescripcion2.set("Madera")
        obtenerPrecio2.set(int(20))
    elif obtenerCodigo2.get() == "Prod2":
        obtenerDescripcion2.set("Palos")
        obtenerPrecio2.set(int(15))
    elif obtenerCodigo2.get() == "Prod3":
        obtenerDescripcion2.set("Pegamento")
        obtenerPrecio2.set(int(4))
    elif obtenerCodigo2.get() == "Prod4":
        obtenerDescripcion2.set("cinta")
        obtenerPrecio2.set(int(5))

#------------------------------
    
def hallar_total():
        obtenerTotal.set(float(obtenerSubtotal.get())+ float(obtenerSubtotal1.get())+ float(obtenerSubtotal2.get()))
        imprimir_datos()
        
 

def CallAssistant():
    Asistente.prueba()

    
#-------------------------------------------
        
def total_definitivo():
    hallar_sub_total()
    hallar_sub_total1()
    hallar_sub_total2()

    
def hallar_sub_total():
    try:
        obtenerSubtotal.set(float(obtenerCantidad.get())*float(obtenerPrecio.get()))
    except ValueError:
        obtenerSubtotal.set(int(0))
        
def hallar_sub_total1():
    try:
        obtenerSubtotal1.set(float(obtenerCantidad1.get())*float(obtenerPrecio1.get()))
    except ValueError:
        obtenerSubtotal1.set(int(0))
def hallar_sub_total2():
    try:
        obtenerSubtotal2.set(float(obtenerCantidad2.get())*(float(obtenerPrecio2.get())))
    except ValueError:
        obtenerSubtotal2.set(int(0))
    
def imprimir_datos():
    print("hola, Señor "+obtenerApellido.get()+" "+obtenerNombre.get())
    print("El total de su compra es: "+obtenerTotal.get()+" Nuevos soles")
    
miFrame = Frame(root)# primer frame
miFrame.pack() #empaquetando





#Insertamos los widgets
#label titulo
Title = Label(miFrame, text='Ferretería "El tornillo Feliz"', font=("calibri", 18))
Title.grid(row=0, column=2, pady=10, padx=10)

#Label y entry de DNI
obtenerDni=StringVar()
lDni = Label(miFrame, text='DNI:')
lDni.grid(row=5, column=0, sticky='e', pady=5, padx=5)
tDni = Entry(miFrame,textvariable=obtenerDni)
tDni.grid(row=5, column=1, pady=5, padx=5)

#Label y entry Apellido
obtenerApellido=StringVar()
lApellido = Label(miFrame, text='Apellidos:')
lApellido.grid(row=6, column=2, sticky='e', pady=5, padx=5)
tApellido = Entry(miFrame,textvariable=obtenerApellido)
tApellido.grid(row=6, column=1, pady=5, padx=5)

#Label y entry Nombre
obtenerNombre=StringVar()
lNombre = Label(miFrame, text='Nombres:')
lNombre.grid(row=6, column=0, sticky='e', pady=5, padx=5)
tNombre = Entry(miFrame,textvariable=obtenerNombre)
tNombre.grid(row=6, column=3, pady=5, padx=5)
#Label y entry Diección
obtenerDir=StringVar()
lDireccion = Label(miFrame, text='Dirección:')
lDireccion.grid(row=7, column=0, sticky='e', pady=5, padx=5)
tDireccion = Entry(miFrame,textvariable=obtenerDir)
tDireccion.grid(row=7, column=1, columnspan=2, sticky='we',pady=5, padx=5)
#Label y entry Teléfono
obtenerTel=StringVar()
lTel = Label(miFrame, text='Teléfono:')
lTel.grid(row=8, column=0, sticky='e', pady=5, padx=5)
tTel = Entry(miFrame,textvariable=obtenerTel)
tTel.grid(row=8, column=1,columnspan=2, sticky='we', pady=5, padx=5)

#segundo frame
miFrame1 = Frame(root)
miFrame1.pack()


#nombre de mis variables(CODIGO)
obtenerCodigo = StringVar()
obtenerCodigo1 = StringVar()
obtenerCodigo2 = StringVar()
#Label y entry,s Código producto -----------------------
lCodigo = Label(miFrame1, text='Cod_Prod')
lCodigo.grid(row=9, column=0,sticky='e', pady=5, padx=5)
tCodigo1 = Spinbox(miFrame1,values=("Prod1", "Prod2","Prod3","Prod4"), width=7,command=hallar_desc, textvariable =obtenerCodigo,state='readonly')
tCodigo1.grid(row=10, column=0, pady=5, padx=5)
tCodigo2 = Spinbox(miFrame1,values=("Prod1", "Prod2","Prod3","Prod4"), width=7,command=hallar_desc1, textvariable =obtenerCodigo1,state='readonly')
tCodigo2.grid(row=11, column=0, pady=5, padx=5)
tCodigo3 = Spinbox(miFrame1,values=("Prod1", "Prod2","Prod3","Prod4"), width=7,command=hallar_desc2, textvariable =obtenerCodigo2,state='readonly')
tCodigo3.grid(row=12, column=0, pady=5, padx=5)

#nombres de mis variables (DESCRIPCION)
obtenerDescripcion = StringVar()
obtenerDescripcion1 =StringVar()
obtenerDescripcion2 =StringVar()
#Label y entry,s Descripción ---------------------------
lDes = Label(miFrame1, text='Descripción')
lDes.grid(row=9, column=1,sticky='ew', pady=5, padx=5)
tDes1 = Entry(miFrame1, width=25,state='readonly', textvariable = obtenerDescripcion)
tDes1.grid(row=10, column=1, pady=5, padx=5)
tDes2 = Entry(miFrame1, width=25,state='readonly', textvariable = obtenerDescripcion1)
tDes2.grid(row=11, column=1, pady=5, padx=5)
tDes3 = Entry(miFrame1, width=25,state='readonly',textvariable = obtenerDescripcion2)
tDes3.grid(row=12, column=1, pady=5, padx=5)

#nombres de mi variable (UNIDAD)
obtenerUnidad = StringVar()
obtenerUnidad1 = StringVar()
obtenerUnidad2 = StringVar()
#Label y entry,s Unidad --------------------------------
lUni = Label(miFrame1, text='Unidad')
lUni.grid(row=9, column=2,sticky='ew', pady=5, padx=5)
lUni = Spinbox(miFrame1, width=5, values=("Und","Kg","Lt","cm","m","Paq",),state='readonly',textvariable = obtenerUnidad)
lUni.grid(row=10, column=2,sticky='ew', pady=5, padx=5)
tUni2 = Spinbox(miFrame1, width=5, values=("Und","Kg","Lt","cm","m","Paq",),state='readonly',textvariable = obtenerUnidad1)
tUni2.grid(row=11, column=2,sticky='ew', pady=5, padx=5)
tUni3 = Spinbox(miFrame1, width=5, values=("Und","Kg","Lt","cm","m","Paq",),state='readonly',textvariable = obtenerUnidad2)
tUni3.grid(row=12, column=2,sticky='ew', pady=5, padx=5)

#nombres de mi variable (CANTIDAD)
obtenerCantidad = StringVar()
obtenerCantidad1 = StringVar()
obtenerCantidad2 = StringVar()
#Label y entry,s Cantidad ------------------------------
lCantidad = Label(miFrame1, text='Cantidad')
lCantidad.grid(row=9, column=3,sticky='ew', pady=5, padx=5)
tCantidad1 = Entry(miFrame1, width=7, textvariable = obtenerCantidad)
tCantidad1.grid(row=10, column=3, pady=5, padx=5)
tCantidad2 = Entry(miFrame1, width=7, textvariable = obtenerCantidad1)
tCantidad2.grid(row=11, column=3, pady=5, padx=5)
tCantidad3 = Entry(miFrame1, width=7, textvariable = obtenerCantidad2)
tCantidad3.grid(row=12, column=3, pady=5, padx=5)

#Nombres de mis variables (PRECIO)
obtenerPrecio = StringVar()
obtenerPrecio1 = StringVar()
obtenerPrecio2 = StringVar()
#Label y entry,s Precio --------------------------------
lPrecio = Label(miFrame1, text='Precio')
lPrecio.grid(row=9, column=4,sticky='ew', pady=5, padx=5)
tPrecio1 = Entry(miFrame1, width=7,textvariable = obtenerPrecio,state='readonly')
tPrecio1.grid(row=10, column=4, pady=5, padx=5)
tPrecio2 = Entry(miFrame1, width=7,textvariable = obtenerPrecio1,state='readonly')
tPrecio2.grid(row=11, column=4, pady=5, padx=5)
tPrecio3 = Entry(miFrame1, width=7,textvariable = obtenerPrecio2,state='readonly')
tPrecio3.grid(row=12, column=4, pady=5, padx=5)

#nombre de mi variable (SUB TOTAL)
obtenerSubtotal = StringVar()
obtenerSubtotal1 = StringVar()
obtenerSubtotal2 = StringVar()
#Label y entry,s Subtotal ------------------------------
lSubtotal = Label(miFrame1, text='Subtotal')
lSubtotal.grid(row=9, column=5,sticky='ew', pady=5, padx=5)
tSubtotal1 = Entry(miFrame1, width=7, state="readonly",textvariable = obtenerSubtotal)
tSubtotal1.grid(row=10, column=5, pady=5, padx=5)
tSubtotal2 = Entry(miFrame1, width=7, state="readonly",textvariable = obtenerSubtotal1)
tSubtotal2.grid(row=11, column=5, pady=5, padx=5)
tSubtotal3 = Entry(miFrame1, width=7, state="readonly",textvariable = obtenerSubtotal2)
tSubtotal3.grid(row=12, column=5, pady=5, padx=5)


#Label y entry,s Total --------------------------------
obtenerTotal = StringVar() # Nombre de la variable de total
lTotal = Button(miFrame1, text='Total',font=("calibri", 9),command=hallar_total)
lTotal.grid(row=12, column=7,sticky='ew', pady=5, padx=5)
tTotal = Entry(miFrame1, width=10, state="readonly", textvariable = obtenerTotal)
tTotal.grid(row=12, column=8, pady=5, padx=5)

boton = Button(miFrame1,width=9,height=2, text="Sub-total",command=total_definitivo).grid(row=10, column=6, pady=5, padx=5)
botonIA = Button(miFrame1,width=9,height=2, text="ASISTENTE",command=CallAssistant).grid(row=11, column=8, pady=8, padx=8)
#boton = Button(miFrame1,width=5, text="Exhibir",command=hallar_sub_total1).grid(row=11, column=6, pady=5, padx=5)
#boton = Button(miFrame1,width=5, text="Exhibir",command=hallar_sub_total2).grid(row=12, column=6, pady=5, padx=5)

#-------------------------------------------NUEVA VENTANA--------------------------------------------------------
root.mainloop()

'''
mydb = mysql. conector . connect ( host = “localhost” , usuario = “root” , contraseña = “” , database = “database_name” )
cursor = mydb. cursor ( )
cursor. ejecutar ( “SELECCIONAR * de los usuarios” )
resultado = cursor. fetchall ( )
para la fila en el resultado: imprimir ( fila )


'''
