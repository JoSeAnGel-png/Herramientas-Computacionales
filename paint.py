"""Paint, for drawing shapes.

Programa interactivo de dibujo usando la libreria turtle.
El usuario da clic en dos puntos de la pantalla: el primer clic marca
el punto de inicio, y el segundo clic dibuja la figura seleccionada
entre esos dos puntos.
"""

from turtle import *
from freegames import vector


def line(start, end):
    """Draw line from start to end.

    Args:
        start (vector): punto inicial (x, y) donde comienza la linea.
        end (vector): punto final (x, y) donde termina la linea.
    """
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end.

    Args:
        start (vector): esquina inicial del cuadrado.
        end (vector): esquina opuesta del cuadrado.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end.

    Args:
        start (vector): punto inicial.
        end (vector): punto final.
    """
    pass  # TODO


def rectangle(start, end):
    """Draw rectangle from start to end.

    Ancho = end.x - start.x, alto = end.y - start.y.

    Args:
        start (vector): esquina inicial del rectangulo.
        end (vector): esquina opuesta (diagonal) del rectangulo.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()


def triangle(start, end):
    """Draw triangle from start to end.

    Dibuja un triangulo equilatero usando end.x - start.x como
    longitud de cada lado. Gira 120 grados entre cada lado.

    Args:
        start (vector): vertice inicial del triangulo.
        end (vector): punto que define la longitud del lado.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    forward(end.x - start.x)
    left(120)
    forward(end.x - start.x)
    left(120)
    forward(end.x - start.x)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape.

    Args:
        x (float): coordenada X del clic del usuario.
        y (float): coordenada Y del clic del usuario.
    """
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key.

    Args:
        key (str): la llave del diccionario state a modificar.
        value: el nuevo valor a guardar en esa llave.
    """
    state[key] = value


state = {'start': None, 'shape': line}

setup(420, 420, 370, 0)
onscreenclick(tap)
listen()

onkey(undo, 'u')

onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')

onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

done()
