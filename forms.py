from wtforms import Form, StringField
from wtforms import SearchField,IntegerField,PasswordField,FloatField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField("Matricula",[
        validators.DataRequired(message="E que rollo, no lo dejes vacio W"),
        validators.NumberRange(min=100, max=1000, message="Papi hablo en chino o que? Nomas entre 100 y 1000")
    ])
    nombre=StringField("Nombre",[
        validators.DataRequired(message="E que rollo, no lo dejes vacio W"),
        validators.Length(min=3, max=10, message="Eso no es un nombre patron")
    ])
    apa=StringField("Apaterno",[
        validators.DataRequired(message="E que rollo, no lo dejes vacio W"),
        validators.Length(min=3, max=10, message="Eso no es un apellido jefe no diga mmds")
    ])
    ama=StringField("Amaterno",[
        validators.DataRequired(message="E que rollo, no lo dejes vacio W"),
        validators.Length(min=3, max=10, message="Eso no es un apellido jefe no diga mmds")
    ])
    email=EmailField("Correo",[
        validators.DataRequired(message="E que rollo, no lo dejes vacio W"),
        validators.email(message="Eso no es un correo padrino, metele @ y .com minimo")
    ])