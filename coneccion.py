import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter.ttk import Combobox

connection = mysql.connector.connect(user="root", password="jhonmendozq2002", host="localhost", port=3306, database="hotel_alura")
cursor = connection.cursor()

# Función para mostrar un mensaje de confirmación
def mostrar_mensaje(mensaje):
    messagebox.showinfo("Mensaje", mensaje)

# Función para insertar una reserva
def insertar_reserva():
    fecha_inicio = entry_fecha_inicio.get()
    fecha_final = entry_fecha_final.get()
    valor = entry_valor.get()
    forma_pago = combo_forma_pago.get()

    query = "INSERT INTO reservas (fecha_inicio, fecha_final, valor, forma_pago) VALUES (%s, %s, %s, %s)"
    valores = (fecha_inicio, fecha_final, valor, forma_pago)

    try:
        cursor.execute(query, valores)
        connection.commit()
        mostrar_mensaje("Reserva agregada exitosamente")
    except Exception as e:
        mostrar_mensaje(f"Error al agregar la reserva: {str(e)}")

# Función para agregar un nuevo huésped
def agregar_huesped():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()
    nacionalidad = entry_nacionalidad.get()
    telefono = entry_telefono.get()
    reserva_id = combo_reservas.get()

    query = "INSERT INTO huespedes (nombre, apellido, fecha_nacimiento, nacionalidad, telefono, reserva) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (nombre, apellido, fecha_nacimiento, nacionalidad, telefono, reserva_id)

    try:
        cursor.execute(query, valores)
        connection.commit()
        mostrar_mensaje("Huésped agregado exitosamente")
    except Exception as e:
        mostrar_mensaje(f"Error al agregar el huésped: {str(e)}")

# Función para consultar reservas disponibles
def consultar_reservas_disponibles():
    cursor.execute("SELECT * FROM reservas")
    reservas = cursor.fetchall()

    mostrar_mensaje("Reservas disponibles:\n\n" + "\n".join([str(reserva) for reserva in reservas]))

# Cerrar el cursor y la conexión al cerrar la ventana
def cerrar_conexion():
    cursor.close()
    connection.close()
    ventana.destroy()

# Configuración de la ventana
ventana = Tk()
ventana.title("Sistema de Reserva de Hotel")
ventana.geometry("400x400")


# Etiquetas y campos de entrada para la reserva
label_fecha_inicio = Label(ventana, text="Fecha de inicio:")
label_fecha_inicio.grid(row=0, column=0, sticky=W)
entry_fecha_inicio = DateEntry(ventana, width=20, background="darkblue", foreground="white", date_pattern="yyyy-mm-dd")
entry_fecha_inicio.grid(row=0, column=1)

label_fecha_final = Label(ventana, text="Fecha final:")
label_fecha_final.grid(row=1, column=0, sticky=W)
entry_fecha_final = DateEntry(ventana, width=20, background="darkblue", foreground="white", date_pattern="yyyy-mm-dd")
entry_fecha_final.grid(row=1, column=1)

label_valor = Label(ventana, text="Valor:")
label_valor.grid(row=2, column=0, sticky=W)
entry_valor = Entry(ventana)
entry_valor.grid(row=2, column=1)

label_forma_pago = Label(ventana, text="Forma de pago:")
label_forma_pago.grid(row=3, column=0, sticky=W)
opciones_pago = ["Tarjeta", "Transferencia", "Yape", "Plin"]
combo_forma_pago = Combobox(ventana, values=opciones_pago)
combo_forma_pago.grid(row=3, column=1)

# Botón para agregar reserva
boton_agregar_reserva = Button(ventana, text="Agregar Reserva", command=insertar_reserva)
boton_agregar_reserva.grid(row=4, columnspan=2)

# Etiquetas y campos de entrada para el huésped
label_nombre = Label(ventana, text="Nombre:")
label_nombre.grid(row=5, column=0, sticky=W)
entry_nombre = Entry(ventana)
entry_nombre.grid(row=5, column=1)

label_apellido = Label(ventana, text="Apellido:")
label_apellido.grid(row=6, column=0, sticky=W)
entry_apellido = Entry(ventana)
entry_apellido.grid(row=6, column=1)

label_fecha_nacimiento = Label(ventana, text="Fecha de nacimiento:")
label_fecha_nacimiento.grid(row=7, column=0, sticky=W)
entry_fecha_nacimiento = DateEntry(ventana, width=20, background="darkblue", foreground="white", date_pattern="yyyy-mm-dd")
entry_fecha_nacimiento.grid(row=7, column=1)

label_nacionalidad = Label(ventana, text="Nacionalidad:")
label_nacionalidad.grid(row=8, column=0, sticky=W)
entry_nacionalidad = Entry(ventana)
entry_nacionalidad.grid(row=8, column=1)

label_telefono = Label(ventana, text="Teléfono:")
label_telefono.grid(row=9, column=0, sticky=W)
entry_telefono = Entry(ventana)
entry_telefono.grid(row=9, column=1)

label_reserva = Label(ventana, text="Reserva:")
label_reserva.grid(row=10, column=0, sticky=W)
combo_reservas = Combobox(ventana)
combo_reservas.grid(row=10, column=1)

# Botón para agregar huésped
boton_agregar_huesped = Button(ventana, text="Agregar Huésped", command=agregar_huesped)
boton_agregar_huesped.grid(row=11, columnspan=2)

# Botón para consultar reservas disponibles
boton_consultar_disponibles = Button(ventana, text="Consultar Reservas Disponibles", command=consultar_reservas_disponibles)
boton_consultar_disponibles.grid(row=12, columnspan=2)

# Cerrar la conexión al cerrar la ventana
ventana.protocol("WM_DELETE_WINDOW", cerrar_conexion)

# Ejecutar la interfaz
ventana.mainloop()