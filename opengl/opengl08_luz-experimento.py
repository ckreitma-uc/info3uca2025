# https://openglsamples.sourceforge.net/teapot_py.html
from OpenGL import GLUT
from OpenGL import GLU
from OpenGL import GL
import sys

name = 'OpenGL Python Teapot'


def main():
    GLUT.glutInit(sys.argv)
    GLUT.glutInitDisplayMode(GLUT.GLUT_DOUBLE | GLUT.GLUT_RGB | GLUT.GLUT_DEPTH)
    GLUT.glutInitWindowSize(400, 400)
    GLUT.glutCreateWindow(name)

    GL.glClearColor(0., 0., 1., 1.)
    GL.glShadeModel(GL.GL_SMOOTH)
    GL.glEnable(GL.GL_CULL_FACE)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glEnable(GL.GL_LIGHTING)
    lightZeroPosition = [2 * -20., 2 * 2., 2 * -2., 1.]
    lightZeroColor = [1, 1., 1., 1.0]  # green tinged
    GL.glLightfv(GL.GL_LIGHT0, GL.GL_POSITION, lightZeroPosition)
    GL.glLightfv(GL.GL_LIGHT0, GL.GL_DIFFUSE, lightZeroColor)
    GL.glLightf(GL.GL_LIGHT0, GL.GL_CONSTANT_ATTENUATION, 0.1)
    GL.glLightf(GL.GL_LIGHT0, GL.GL_LINEAR_ATTENUATION, 0.05)
    GL.glEnable(GL.GL_LIGHT0)
    GLUT.glutDisplayFunc(display)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GLU.gluPerspective(40., 1., 1., 40.)
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GLU.gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)
    # GL.glPushMatrix()
    GLUT.glutMainLoop()
    return


def display():

    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    GL.glPushMatrix()
    color = [1.0, 1., 1., 1.]
    GL.glMaterialfv(GL.GL_FRONT, GL.GL_DIFFUSE, color)
    # GL.glRotatef(180, 1, 0, 0)
    # GL.glRotatef(-45, 0, 1, 0)
    GLUT.glutSolidTeapot(1, 1, 1)

    GL.glPopMatrix()
    # GL.glFlush()
    GLUT.glutSwapBuffers()

    return


if __name__ == '__main__':
    main()
