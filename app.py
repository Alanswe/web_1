from logging import root
import os
from bottle import route,run, TEMPLATE_PATH,jinja2_view,static_file

TEMPLATE_PATH.append(os.path.join(os.path.dirname(__file__),'templates'))

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename,root='./static')

@route('/')
@jinja2_view('home.html')
def hola():
    return {'datos':[
        ('Alan',2,'Lunes'),
        ('Juan',3,'Martes'),
        ('Pepe',4,'Jueves')
        ]
        }
    #return {'Nombre': 'Alan','Fecha': '23/09/2022'}

run(host='localhost',port=8080,debug=True)