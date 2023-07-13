from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

def vista(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end',values=i)

def consulta():
    q2= q.get()
    query = "SELECT nombre, apellido, direccion, telefono from customer WHERE nombre LIKE '%"+q2+"%' OR apellido LIKE '%"+q2+"%'"
    curso.execute(query)
    rows = curso.fetchall()
    vista(rows)

def restablecer():
    query = "SELECT nombre, apellido, direccion, telefono from customer"
    curso.execute(query)
    rows = curso.fetchall()
    vista(rows)


def agregar():
    if t1.get()== "" or t2.get()== "" or t3.get()=="" or t4.get()=="":
        messagebox.showerror("Por favor" , "Complete los campos")
    else:
        negocio = pymysql.connect(host="localhost",user="root",password="", database="negocio")
        curso = negocio.cursor()
        curso.execute("insert into customer values(%s,%s,%s,%s)",(t1.get(),t2.get(),t3.get(),t4.get()))
        negocio.commit()
        negocio.close()
        messagebox.showinfo("Datos completado" , "Se registraron los datos correctamente")
        mostrar()

def traineeInfo(ev):
    viewInfo = trv.focus()
    learnerData = trv.item(viewInfo)
    row = learnerData['values']
    t1.set(row[0])
    t2.set(row[1])
    t3.set(row[2])
    t4.set(row[3])


def mostrar():
    negocio = pymysql.connect(host="localhost",user="root",password="", database="negocio")
    curso = negocio.cursor()
    curso.execute("select * from customer")
    result = curso.fetchall()
    if len(result) != 0:
        trv.delete(*trv.get_children())
        for row in result:
            trv.insert('',END, values=row)
    negocio.commit()
    negocio.close()

def actualizar():
    negocio =  pymysql.connect(host="localhost",user="root",password="", database="negocio")
    curso = negocio.cursor()
    curso.execute("update customer set apellido=%s, direccion=%s, telefono=%s where nombre ")


def limpiar():
    ent1n.delete(0, END)
    ent1a.delete(0, END)
    ent1d.delete(0, END)
    ent1t.delete(0, END)

def eliminar():
    negocio = pymysql.connect(host="localhost", user="root", password="", database="negocio")
    curso = negocio.cursor()
    curso.execute("delete from customer where nombre=%s", t1.get())
    negocio.commit()
    mostrar()
    negocio.close()
    limpiar()



negocio = pymysql.connect(host="localhost",user="root",password="", database="negocio")
curso = negocio.cursor()


root  = Tk()
Id = StringVar()
q = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()

root.title("Aplicacion python")
root.geometry("800x550")
root.config(bg="silver")

frame1 = LabelFrame(root, text="Datos del cliente", font=('Arial', 14))
frame2 = LabelFrame(root, text="Consulta", font=('Arial', 14))
frame3 = LabelFrame(root, text="Lista del cliente", font=('Arial', 14))

frame1.pack(fill="both", expand="yes", padx= 20, pady=10)
frame2.pack(fill="both", expand="yes", padx= 20, pady=10)
frame3.pack(fill="both", expand="yes", padx= 20, pady=10)
trv= ttk.Treeview(frame3, columns=(1,2,3,4), show="headings", height="10")
trv.pack()

trv.heading(1, text="Nombre")
trv.heading(2, text="Apellido")
trv.heading(3, text="Dirección")
trv.heading(4, text="Telefono")
trv.bind("<ButtonRelease-1>", traineeInfo)

query = "SELECT nombre, apellido, direccion, telefono from customer"
curso.execute(query)
rows = curso.fetchall()
vista(rows)

lbl = Label(frame2, text="Consulta")
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(frame2, textvariable=q)
ent.pack(side=tk.LEFT, padx=6)
btn = Button(frame2, width=10, text="Consulta", command=consulta)
btn.pack(side=tk.LEFT, padx=6)
cbtn = Button(frame2, width=10 , text="Restablecer" , command= restablecer)
cbtn.pack(side=tk.LEFT, padx=6)

lbl1 = Label(frame1, text="Nombre")
lbl1.grid(column=0, row=0 , padx=5 , pady=3)
ent1n = Entry(frame1, textvariable= t1)
ent1n.grid(column=1, row=0 , padx=5, pady=3)

lbl1 = Label(frame1, text="Apellido")
lbl1.grid(column=0, row=1 , padx=5 , pady=3)
ent1a = Entry(frame1, textvariable= t2)
ent1a.grid(column=1, row=1 , padx=5, pady=3)

lbl1 = Label(frame1, text="Direccion")
lbl1.grid(column=0, row=2 , padx=5 , pady=3)
ent1d = Entry(frame1, textvariable= t3)
ent1d.grid(column=1, row=2 , padx=5, pady=3)

lbl1 = Label(frame1, text="Telefono")
lbl1.grid(column=0, row=3 , padx=5 , pady=3)
ent1t = Entry(frame1, textvariable= t4)
ent1t.grid(column=1, row=3 , padx=5, pady=3)


actualizar_btn = Button(frame1, width=10, text="Agregar", command=agregar)
actualizar_btn.grid(column=0, row=4, padx=5, pady=3)

agregar_btn = Button(frame1, width=10, text="Actualizar", command=actualizar)
agregar_btn.grid(column=1, row=4, padx=5, pady=3)

eliminar_btn = Button(frame1, width=10, text="Eliminar", command=eliminar)
eliminar_btn.grid(column=2, row=4, padx=5, pady=3)

limpiar_btn = Button(frame1, width=10, text="Limpiar", command=limpiar)
limpiar_btn.grid(column=3, row=4, padx=20, pady=3)

mostrar_btn = Button(frame1, width=10, text="Mostrar", command=mostrar)
mostrar_btn.grid(column=4, row=4, padx=20, pady=3)
root.mainloop()