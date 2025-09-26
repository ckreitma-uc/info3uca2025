import sys
from OpenGL import GL
from OpenGL import GLU
from OpenGL import GLUT

altura, ancho = 1500, 1500
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)


def inicializar():
    # Borrar la pantalla
    GL.glClearColor(1, 1, 1, 1)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    # Selecciona la matriz de proyección
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()  # Inicializar la matriz.

    # Ángulo, ratio, near, far
    GLU.gluPerspective(45, altura/ancho, 0.1, 50.0)

    # Seleccionar la matriz modelview
    GL.glMatrixMode(GL.GL_MODELVIEW)

    # Inicializar la matriz.
    GL.glLoadIdentity()

    GL.glTranslatef(0.0, 0.0, -5.0)

    # Ángulo,
    GL.glRotatef(10, 0.3, 0.3, 0.3)


def ejes():
    # Eje x
    GL.glBegin(GL.GL_LINES)
    GL.glColor3f(1, 0, 0)
    GL.glVertex3f(0, 0, 0)
    GL.glVertex3f(1, 0, 0)

    GL.glColor3f(0, 1, 0)
    GL.glVertex3f(0, 0, 0)
    GL.glVertex3f(0, 1, 0)

    GL.glColor3f(0, 0, 1)
    GL.glVertex3f(0, 0, 0)
    GL.glVertex3f(0, 0, 1)

    GL.glEnd()


def cubo():
    GL.glBegin(GL.GL_LINES)
    GL.glColor3f(0, 0, 0)
    for edge in edges:
        for vertex in edge:
            GL.glVertex3fv(vertices[vertex])
    GL.glEnd()


def actualizar():
    inicializar()
    ejes()
    cubo()
    GL.glFlush()


def main():
    GLUT.glutInit(sys.argv)
    GLUT.glutInitDisplayMode(GLUT.GLUT_SINGLE | GLUT.GLUT_RGB)
    GLUT.glutInitWindowSize(altura, ancho)
    GLUT.glutInitWindowPosition(0, 0)
    GLUT.glutCreateWindow("Cubo 3D sencillo con lineas")
    GLUT.glutDisplayFunc(actualizar)
    GLUT.glutMainLoop()


main()
