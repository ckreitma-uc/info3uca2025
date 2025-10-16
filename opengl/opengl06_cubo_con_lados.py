import sys
from OpenGL import GL
from OpenGL import GLU
from OpenGL import GLUT
"""
Para inteacción.
x,X
y,Y     "Corresponden al ojo
z,Z

i,I
o,O     Corresponden al look_at
p,P

n entre 0 y 5 Inhabilitar caras
"""

pantallax, pantallay = 800, 800

ojox, ojoy, ojoz = 0.8, 0.8, 3
look_x, look_y, look_z = 0.0, 0.0, 0.0
lado = 0.3
caras = [True, True, True, True, True, True]


def cara(vertices, color):
    GL.glColor(color[0], color[1], color[2], 1)
    GL.glBegin(GL.GL_QUADS)
    for v in vertices:
        GL.glVertex3fv(v)
    GL.glEnd()


def display():
    global ojox, ojoy, ojoz, look_x, look_y, look_z
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    # Selecciona la matriz de proyección
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()  # Inicializar la matriz.

    # Ángulo, ratio, near, far
    GLU.gluPerspective(35, pantallax / pantallay, 0.1, 10.0)

    # Seleccionar la matriz modelview
    GL.glMatrixMode(GL.GL_MODELVIEW)

    # Inicializar la matriz.
    GL.glLoadIdentity()

    # Desde, Hacia, Dirección arriba
    print(f'ojox={ojox}')
    GLU.gluLookAt(ojox, ojoy, ojoz, look_x, look_y, look_z, 0.0, 1.0, 0.0)

    Cube()


def ejes():
    # Eje x
    largo = 2
    GL.glBegin(GL.GL_LINES)
    GL.glColor3f(1, 0, 0)
    GL.glVertex3f(0, 0, 0)
    GL.glVertex3f(largo, 0, 0)

    GL.glColor3f(0, 1, 0)
    GL.glVertex3f(0, 0, 0)
    GL.glVertex3f(0, largo, 0)

    GL.glColor3f(0, 0, 1)
    GL.glVertex3f(0, 0, 0)
    GL.glVertex3f(0, 0, largo)

    GL.glEnd()


def Cube():
    vertices = []
    global lado
    global caras
    z = 0
    # Inferior izquierdo
    vertices.append((0, 0, z))
    # Inferior derecho
    vertices.append((lado, 0, z))
    # Superior derecho
    vertices.append((lado, lado, z))
    # Superior izquierdo
    vertices.append((0, lado, z))

    square = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
    )

    ejes()

    # Cara izquierda #rosada
    if caras[0]:
        GL.glPushMatrix()
        GL.glRotate(-90, 0, 1, 0)
        cara(vertices, (0.8, 0.2, 0.5))
        GL.glPopMatrix()

    # # Cara inferior #amarillo
    if caras[1]:
        GL.glPushMatrix()
        GL.glRotate(90, 1, 0, 0)
        cara(vertices, (0.7, 0.7, 0.1))
        GL.glPopMatrix()

    # # # Cara derecha #celeste
    if caras[2]:
        GL.glPushMatrix()
        GL.glTranslatef(lado, 0, 0)
        GL.glRotate(-90, 0, 1, 0)
        cara(vertices, (0.2, 0.4, 0.8))
        GL.glPopMatrix()

    # # Cara frontal #verde
    if caras[3]:
        GL.glPushMatrix()
        GL.glTranslatef(0, 0, lado)
        cara(vertices, (0.1, 0.7, 0.2))
        GL.glPopMatrix()

    # # Cara superior #lila
    if caras[4]:
        GL.glPushMatrix()
        GL.glTranslatef(0, lado, 0)
        GL.glRotate(90, 1, 0, 0)
        cara(vertices, (0.3, 0.1, 0.3))
        GL.glPopMatrix()

    # # Cara trasera #gris
    if caras[5]:
        cara(vertices, (0.4, 0.4, 0.4))

    GL.glFlush()


def buttons(key, x, y):
    global ojox, ojoy, ojoz
    global look_x, look_y, look_z
    delta = 0.1
    print(f'key={key} x={x} y={y}')
    # Ojo
    if key == b'x':
        ojox += delta
    if key == b'X':
        ojox -= delta
    if key == b'y':
        ojoy += delta
    if key == b'Y':
        ojoy -= delta
    if key == b'z':
        ojoz += delta
    if key == b'Z':
        ojoz -= delta
    if key == b'i':
        look_x += delta
    if key == b'I':
        look_x -= delta
    if key == b'o':
        look_y += delta
    if key == b'O':
        look_y -= delta
    if key == b'p':
        look_z += delta
    if key == b'P':
        look_z -= delta
    if key in [b'0', b'1', b'2', b'3', b'4', b'5', b'6']:
        caras[int(key)] = not caras[int(key)]

    GLUT.glutPostRedisplay()


def main():
    GLUT.glutInit(sys.argv)
    GLUT.glutInitDisplayMode(GLUT.GLUT_DOUBLE | GLUT.GLUT_RGB | GLUT.GLUT_DEPTH)
    GL.glDepthFunc(GL.GL_LESS)
    GLUT.glutInitWindowSize(pantallax, pantallay)
    GLUT.glutInitWindowPosition(0, 0)
    GLUT.glutInitDisplayMode(GLUT.GLUT_RGBA | GLUT.GLUT_DEPTH)
    GLUT.glutCreateWindow("Cubo 3D con rotación de caras")
    GLUT.glutDisplayFunc(display)
    GLUT.glutKeyboardFunc(buttons)
    GLUT.glutMainLoop()


main()
