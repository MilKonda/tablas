import pymysql
from tkinter import Tk,ttk,Label,Button

def vaciartabla():
      filas=tabla.get_children()
      for f in filas:
            tabla.delete(f)

def buscar():
    genbusc=comboOneTwoPunch.get()
    cursor.execute("SELECT titulo,genero,duracion,anio FROM peliculas where genero=%s",(genbusc,))
    pelis2=cursor.fetchall()
    vaciartabla()
    for p in pelis2:
            tabla.insert("","end",values=p)



con=pymysql.connect(host="db4free.net",user="alumnopython",password="programacionpython",db="practicasql")
cursor=con.cursor()
cursor.execute("SELECT titulo,genero,duracion,anio FROM peliculas")
pelis=cursor.fetchall()
cursor.execute("SELECT DISTINCT genero FROM peliculas")
genero=cursor.fetchall()

ven=Tk()
ven.config(width=600, height=500)
ven.title("Peliculas")
tabla=ttk.Treeview(ven)
tabla["columns"]=["titulo","genero","duracion","aniostreno"]
tabla.column("#0", width=0)
tabla.column("titulo", width=120)
tabla.column("genero", width=100)
tabla.column("duracion", width=80, anchor="center")
tabla.column("aniostreno", width=80)
tabla.heading("titulo",text="Título", anchor="center")
tabla.heading("genero", text="Genero",anchor="w")
tabla.heading("duracion", text="Duración", anchor="e")
tabla.heading("aniostreno", text="Año", anchor="center")
tabla.place(x=10,y=10)

# This is the section of code which creates a button
Button(ven, text='Buscar', bg='#F0F8FF', font=('arial', 12, 'normal'), command=buscar).place(x=210, y=350)

# This is the section of code which creates the a label
Label(ven, text='Generos :', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=10, y=355)

# This is the section of code which creates a combo box
comboOneTwoPunch= ttk.Combobox(ven, values=genero, font=('arial', 12, 'normal'), width=10)
comboOneTwoPunch.place(x=90, y=355)
#comboOneTwoPunch.current(1)

#for p in pelis:
#    tabla.insert("","end",values=p)
#tabla.insert("","end",values=pelis)




ven.mainloop()