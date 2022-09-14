from tkinter import *

from AsistenteIA import Asistente
#import MySQLdb

#VARIABLES


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
    try: 
        obtenerTotal.set(float(obtenerSubtotal.get())+ float(obtenerSubtotal1.get())+ float(obtenerSubtotal2.get()))
        imprimir_datos()
    except ValueError:
        obtenerTotal.set("")
        
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
        global des 
        obtenerSubtotal.set(0)
        
def hallar_sub_total1():
    try:
        obtenerSubtotal1.set(float(obtenerCantidad1.get())*float(obtenerPrecio1.get()))
    except ValueError:
        global des1 
        obtenerSubtotal1.set(0)
def hallar_sub_total2():
    try:
        obtenerSubtotal2.set(float(obtenerCantidad2.get())*(float(obtenerPrecio2.get())))
    except ValueError:
        global des2 
        obtenerSubtotal2.set(0)
def Info():
    obtenerDni.set("76577686")
    obtenerTel.set("918914094")
    obtenerApellido.set("Mamani Mamani")
    obtenerNombre.set("Edward Josue")
    obtenerDir.set("Calle Jorge Chaves G-6")
def imprimir_datos():
    emergent = Tk()
    emergent.title('Ferretería "El tornillo feliz"') # nombre del titulo de mi ventana
    emergent.resizable(True,True)
    emergent.iconbitmap("ferretería.ico")
    
    frameem = Frame(emergent)
    frameem.pack() 
    Ttl = Label(frameem, text='Ferretería "El tornillo Feliz"', font=("calibri", 18))
    Ttl.grid(row=0, column=1, pady=10, padx=10)
    frameem1 = Frame(emergent)
    frameem1.pack() 
    lbl = Label(frameem1, text=f"Cliente: {obtenerNombre.get()} {obtenerApellido.get()}", font=("Sans-Serif",11)).grid(row=0, column=0, pady=5, padx=10)
    lbl1 = Label(frameem1, text=f"DNI : {obtenerDni.get()}",  font=("Sans-Serif",11)).grid(
        row=0, column= 1, pady=5, padx=5)
    lbl1 = Label(frameem1, text=f"Dirección : {obtenerDir.get()}",  font=("Sans-Serif",11),justify='left')
    lbl1.grid(row=1, column= 0, pady=5, padx=5)
    lbl1 = Label(frameem1, text=f"Telefono : {obtenerTel.get()}",  font=("Sans-Serif",11),justify='left')
    
    frameem2 = Frame(emergent)
    frameem2.pack()        
    emergent.mainloop()

root = Tk() #root = nombre de mi raiz
root.title('Ferretería "El tornillo feliz"') # nombre del titulo de mi ventana
root.resizable(False,False)
root.iconbitmap("ferretería.ico")


#---------------------------------Productos-----------------------------------


miFrame = Frame(root)# primer frame
miFrame.pack() #empaquetando
miFrame #


'''
def Enviardatos():
    dato = [DNI,NOM,APE,DIR,TEL]
    query = "INSERT INTO usuarios(dni,nombre,apellidos,direccion,telefono) VALUES '%s')" % dato
    run_query(query)
    VARIABLES:
    obtenerDni
    obtenerTel
    obtenerApellido
    obtenerNombre
    obtenerDir
    obtenerCodigo
    obtenerCodigo1
    obtenerCodigo2
    obtenerDescripcion
    obtenerDescripcion1
    obtenerDescripcion2
    obtenerUnidad
    obtenerUnidad1
    obtenerUnidad2
    obtenerCantidad
    obtenerCantidad1
    obtenerCantidad2
    obtenerPrecio
    obtenerPrecio1
    obtenerPrecio2
    obtenerSubtotal
    obtenerSubtotal1
    obtenerSubtotal2
    obtenerTotal
    
'''

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
#botonDB = Button(miFrame,width=9,height=2, text="Enviar",command=Enviardatos).grid(row=5, column=2, pady=8, padx=8)
#Label y entry Apellido
obtenerApellido=StringVar()
lApellido = Label(miFrame, text='Apellidos:')
lApellido.grid(row=6, column=2, sticky='e', pady=5, padx=5)
tApellido = Entry(miFrame,textvariable=obtenerApellido)
tApellido.grid(row=6, column=3, pady=5, padx=5)
boton = Button(miFrame ,width=9,height=2, text="Aleatorio",command=Info).grid(row=6, column=4, pady=5, padx=8)
#Label y entry Nombre

obtenerNombre=StringVar()
lNombre = Label(miFrame, text='Nombres:')
lNombre.grid(row=6, column=0, sticky='e', pady=5, padx=5)
tNombre = Entry(miFrame,textvariable=obtenerNombre)
tNombre.grid(row=6, column=1, pady=5, padx=5)
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
'''
DNI = obtenerDni
APE = obtenerApellido
NOM = obtenerNombre
DIR = obtenerDir
TEL = obtenerTel

    

DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = '' 
DB_NAME = 'usuarios_asist' 

def run_query(query=''): 
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
    conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
    cursor = conn.cursor()         # Crear un cursor 
    cursor.execute(query)          # Ejecutar una consulta 
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else: 
        conn.commit()              # Hacer efectiva la escritura de datos 
        data = None             #usuarios_asist
    cursor.close()                 # Cerrar el cursor 
    conn.close()                   # Cerrar la conexión 

    return data

'''
root.mainloop()
#resultado.imprimir(fila)

#-------------------------------------------NUEVA VENTANA--------------------------------------------------------





