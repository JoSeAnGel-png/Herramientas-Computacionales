# Herramientas Computacionales - Paint Game

## Descripcion

Este repositorio contiene una version extendida del juego "Paint" de la
libreria freegames (Grant Jenks), un programa de dibujo interactivo
hecho con la libreria turtle de Python.

El usuario da clic en dos puntos de la pantalla: el primer clic marca
el punto de inicio, y el segundo clic dibuja la figura seleccionada
(linea, cuadrado, circulo, rectangulo o triangulo) entre esos dos puntos.
Con las teclas K/W/G/B/R se cambia el color de relleno.

## Cambios realizados

- **Commit 1:** Estado inicial del proyecto, tal como se descarga de
  freegames (Grant Jenks), sin modificaciones.
- **Commit 2:** Se implemento la funcion `rectangle()`, que dibuja un
  rectangulo usando ancho y alto independientes.
- **Commit 3:** Se implemento la funcion `triangle()`, que dibuja un
  triangulo equilatero usando 3 lados iguales con giros de 120 grados.
- **Commit 4:** Se agregaron docstrings y comentarios a las funciones
  `rectangle()` y `triangle()`, siguiendo el estandar de documentacion
  del Instituto.
- **Pull Request de [NOMBRE DE TU COMPAÑERO]:** se agrego un color
  nuevo y la funcion `circle()`.

## Como ejecutarlo

1. Crear un ambiente virtual: `python3 -m venv venv`
2. Activarlo: `source venv/bin/activate`
3. Instalar freegames: `pip install freegames`
4. Correr el juego: `python3 paint.py`

## Controles

- Clic + clic: dibuja la figura seleccionada
- Teclas l / s / c / r / t: cambia entre linea / cuadrado / circulo /
  rectangulo / triangulo
- Teclas K / W / G / B / R (con Shift): cambia el color
- Tecla u: deshace el ultimo dibujo
