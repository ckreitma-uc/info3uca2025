import sys
from OpenGL import GL
from OpenGL import GLU 
from OpenGL import GLUT 

altura, ancho = 1800, 1800
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


def Cube():
    # Borrar la pantalla
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    # Selecciona la matriz de proyección
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()  # Inicializar la matriz.

    # Ángulo, ratio, near, far
    GLU.gluPerspective(45, altura/ancho, 0.1, 100.0)

    # Seleccionar la matriz modelview
    GL.glMatrixMode(GL.GL_MODELVIEW)

    # Inicializar la matriz.
    GL.glLoadIdentity()

    GL.glTranslatef(0.0, 0.0, -20)

    # Ángulo,
    #GL.glRotatef(45, 0, 0, 1)
    GL.glBegin(GL.GL_LINES)
    for edge in edges:
        for vertex in edge:
            GL.glVertex3fv(vertices[vertex])
    GL.glEnd()
    GL.glFlush()


def main():
    GLUT.glutInit(sys.argv)
    GLUT.glutInitDisplayMode(GLUT.GLUT_SINGLE | GLUT.GLUT_RGB)
    GLUT.glutInitWindowSize(altura, ancho)
    GLUT.glutInitWindowPosition(0, 0)
    GLUT.glutCreateWindow("Cubo 3D sencillo con lineas")
    GLUT.glutDisplayFunc(Cube)
    GLUT.glutMainLoop()


main()
