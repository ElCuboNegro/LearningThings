# features/steps/steps.py

from behave import given, when, then
from django.contrib.auth.models import User
from behave.api.pending_step import StepNotImplementedError
from usuarios.models import Usuario
from django.utils import timezone
import uuid

@given('que tengo un usuario sin username')
def step_impl(context):
    context.usuario = Usuario()  # Crea un nuevo usuario con nombre y género

@given('que tengo un usuario con un nombre parecido a un uuid')
def step_impl(context):
    context.usuario = Usuario(username=str(uuid.uuid4())[:8])  # Crea un usuario con un nombre que se parece a un uuid

@when('guardo el usuario')
def step_impl(context):
    try:
        context.usuario.save()  # Intenta guardar el usuario
    except Exception as e:
        context.exception = str(e)  # Guarda la excepción en el contexto

@then('el usuario debe ser creado con un nombre identico a su uuid')
def step_impl(context):
    assert context.usuario.username == str(context.usuario.id)  # Verifica que el username sea igual al ID del usuario

@then('el username debe ser NO NULL')
def step_impl(context):
    assert context.usuario.username is not None  # Verifica que el username no sea None

@then('el genero del usuario debe ser null')
def step_impl(context):
    assert context.usuario.genero is None  # Verifica que el género sea None

@then('la foto de perfil debe ser null')
def step_impl(context):
    assert context.usuario.foto_perfil is None  # Verifica que la foto de perfil sea None

@then('la fecha de creación debe ser la fecha actual')
def step_impl(context):
    assert context.usuario.fecha_creacion.date() == timezone.now().date()  # Verifica que la fecha de creación sea la actual

@then('la fecha de modificación debe ser la fecha actual')
def step_impl(context):
    assert context.usuario.fecha_modificacion.date() == timezone.now().date()  # Verifica que la fecha de modificación sea la actual

@then('la fecha de eliminación debe ser null')
def step_impl(context):
    assert context.usuario.fecha_eliminacion is None  # Verifica que la fecha de eliminación sea None

@then('el estado civil debe ser null')
def step_impl(context):
    assert context.usuario.estado_civil is None  # Verifica que el estado civil sea None

@then('la fecha de nacimiento debe ser null')
def step_impl(context):
    assert context.usuario.fecha_nacimiento is None  # Verifica que la fecha de nacimiento sea None

@then('el tipo de 16 personalidades A debe ser null')
def step_impl(context):
    assert context.usuario.tipo_personalidad_a is None  # Verifica que el tipo A sea None

@then('el tipo de 16 personalidades B debe ser null')
def step_impl(context):
    assert context.usuario.tipo_personalidad_b is None  # Verifica que el tipo B sea None

@then('el tipo de 16 personalidades C debe ser null')
def step_impl(context):
    assert context.usuario.tipo_personalidad_c is None  # Verifica que el tipo C sea None

@then('el tipo de 16 personalidades D debe ser null')
def step_impl(context):
    assert context.usuario.tipo_personalidad_d is None  # Verifica que el tipo D sea None

@then('la fecha del último evento debe ser null')
def step_impl(context):
    assert context.usuario.fecha_ultimo_evento is None  # Verifica que la fecha del último evento sea None

@then('el "spontime activo" debe ser false')
def step_impl(context):
    assert context.usuario.spontime_activo is False  # Verifica que el "spontime activo" sea False

@then('el "actividades spontime activo" debe ser un array vacío')
def step_impl(context):
    assert context.usuario.actividades_spontime_activo == []  # Verifica que las actividades sean un array vacío

@then('la reputación debe ser 0')
def step_impl(context):
    assert context.usuario.reputacion == 0  # Verifica que la reputación sea 0

@then('los gustos de actividades deben ser un array vacío')
def step_impl(context):
    assert context.usuario.gustos_actividades == []  # Verifica que los gustos de actividades sean un array vacío

@then(u'el username debe ser igual al ID del usuario')
def step_impl(context): 
    assert context.usuario.username == str(context.usuario.id)

@given(u'que tengo un usuario con el nombre "{nombre}" y el género "{genero}"')
def step_impl(context, nombre, genero):
    context.usuario = Usuario(user_first_name=nombre, genero=genero)
    context.usuario.save()

@then(u'el usuario debe ser creado con el nombre "{nombre}"')
def step_impl(context, nombre):
    assert context.usuario.user_first_name == nombre

@then(u'el genero del usuario debe ser "{genero}"')
def step_impl(context, genero):
    assert context.usuario.genero == genero

@given(u'Given que tengo un usuario con un nombre parecido a un uuid')
def step_impl(context):
    context.usuario = Usuario(username=str(uuid.uuid4())[:8])
    context.usuario.save()
    

@then('debería lanzar una excepción al guardar el usuario')
def step_impl(context):
    assert context.exception == "Guardado rechazado"  # Verifica que la excepción sea la esperada
