import os
from bottle import route,run, TEMPLATE_PATH,jinja2_view,static_file,request,redirect
import sqlite3

TEMPLATE_PATH.append(os.path.join(os.path.dirname(__file__),'templates'))

BASE_DATOS = os.path.join(os.path.dirname(__file__),'personas.db') # en sqlite, una base de datos es un fichero


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename,root='./static')

@route('/')
@jinja2_view('home.html')
def hola():
    # return {'datos':[
    #     ('Alan',1,'Lunes'),
    #     ('Juan',2,'Martes'),
    #     ('Pepe',3,'Jueves')
    #     ]
    #     }
    cnx = sqlite3.connect(BASE_DATOS)
    consulta = "select id,nombre,apellidos,dni from persona"
    cursor = cnx.execute(consulta)
    filas = cursor.fetchall()#obtener todas fila para procesarla, trae todas las filas
    cnx.close()#cerrar siempre la consulta
    return {"datos": filas}

    #return {'Nombre': 'Alan','Fecha': '23/09/2022'}

@route('/editar')
@route('/editar/<id:int>')
@jinja2_view('formulario.html')
def mi_form(id=None):#none para que sea opcional
    if 'id' is None:
        return {}
    else:
        cnx = sqlite3.connect(BASE_DATOS)
        consulta = "select id,nombre,apellidos,dni from persona where id = ?"
        cursor = cnx.execute(consulta,(id,))#la coma dice que es una tupla (id,)
        filas = cursor.fetchone()##obtener una fila para procesarla
        cnx.close()
        return {'datos': filas}

@route('/guardar',method='POST')
def guardar():
    # checoche = []
    # nombre = request.POST.usuario
    # correo = request.POST.correo
    # clave1 = request.POST.clave1
    # cars = request.POST.cars
    # num_ratio = request.POST.num_ratio
    # if 'vehiculo' in request.POST:
    #     vehiculos = request.POST.dict['vehiculo']

    # if 'vehiculo' in request.POST:
    #     vehiculos = request.POST.getlist('vehiculo')

    # vehiculo = list(request.POST.vehiculo)

    # if 'checoches1' in request.POST:
    #     checoche.append(request.POST.checoches1)
    # if 'checoches2' in request.POST:
    #     checoche.append(request.POST.checoches2)
    # if 'checoches3' in request.POST:
    #     checoche.append(request.POST.checoches3)

    # ----------------------------------- formulario 2
    nombre = request.POST.nombre
    apellidos = request.POST.apellidos
    dni = request.POST.dni

    cnx = sqlite3.connect(BASE_DATOS)
    id = request.POST.id
    if id == '':#Alta nueva
        consulta = "INSERT into persona (nombre,apellidos,dni) values(?,?,?)"
        cnx.execute(consulta,(nombre,apellidos,dni))
    else:
        consulta = "update persona set nombre = ?, apellidos = ?, dni = ? where id = ?"
        cnx.execute(consulta,(nombre,apellidos,dni,id))
    
    cnx.commit()#es para guardar
    cnx.close()#cerrar siempre la consulta
    redirect('/')

run(host='localhost',port=8080,debug=True)
