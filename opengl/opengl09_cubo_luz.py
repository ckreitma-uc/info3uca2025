# OpenGL Cube with Different Colors and Two Lights
from OpenGL import GLUT
from OpenGL import GLU
from OpenGL import GL
import sys
import math

name = 'OpenGL Python Colored Cube with Two Lights'
rotation = 0.0


def main():
    GLUT.glutInit(sys.argv)
    GLUT.glutInitDisplayMode(GLUT.GLUT_DOUBLE | GLUT.GLUT_RGB | GLUT.GLUT_DEPTH)
    GLUT.glutInitWindowSize(800, 600)
    GLUT.glutCreateWindow(name)

    # Set clear color to black
    GL.glClearColor(0.0, 0.0, 0.0, 1.0)
    GL.glShadeModel(GL.GL_SMOOTH)
    GL.glEnable(GL.GL_CULL_FACE)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glEnable(GL.GL_LIGHTING)
    
    # Setup first light (white light from the front-left)
    light0Position = [5.0, 5.0, 5.0, 1.0]
    light0Diffuse = [0.8, 0.8, 0.8, 1.0]  # White light
    light0Specular = [1.0, 1.0, 1.0, 1.0]
    GL.glLightfv(GL.GL_LIGHT0, GL.GL_POSITION, light0Position)
    GL.glLightfv(GL.GL_LIGHT0, GL.GL_DIFFUSE, light0Diffuse)
    GL.glLightfv(GL.GL_LIGHT0, GL.GL_SPECULAR, light0Specular)
    GL.glEnable(GL.GL_LIGHT0)
    
    # Setup second light (colored light from the back-right)
    light1Position = [-3.0, -3.0, -5.0, 1.0]
    light1Diffuse = [0.4, 0.4, 0.8, 1.0]  # Blue-tinted light
    light1Specular = [0.5, 0.5, 1.0, 1.0]
    GL.glLightfv(GL.GL_LIGHT1, GL.GL_POSITION, light1Position)
    GL.glLightfv(GL.GL_LIGHT1, GL.GL_DIFFUSE, light1Diffuse)
    GL.glLightfv(GL.GL_LIGHT1, GL.GL_SPECULAR, light1Specular)
    GL.glEnable(GL.GL_LIGHT1)
    
    # Enable color material
    GL.glEnable(GL.GL_COLOR_MATERIAL)
    GL.glColorMaterial(GL.GL_FRONT, GL.GL_AMBIENT_AND_DIFFUSE)
    
    GLUT.glutDisplayFunc(display)
    GLUT.glutIdleFunc(idle)
    GLUT.glutKeyboardFunc(keyboard)
    
    GL.glMatrixMode(GL.GL_PROJECTION)
    GLU.gluPerspective(45.0, 800.0/600.0, 0.1, 100.0)
    GL.glMatrixMode(GL.GL_MODELVIEW)
    
    GLUT.glutMainLoop()
    return


def draw_colored_cube():
    """Draw a cube with different colors on each face"""
    GL.glBegin(GL.GL_QUADS)
    
    # Front face - Red
    GL.glColor3f(1.0, 0.0, 0.0)
    GL.glNormal3f(0.0, 0.0, 1.0)
    GL.glVertex3f(-1.0, -1.0, 1.0)
    GL.glVertex3f(1.0, -1.0, 1.0)
    GL.glVertex3f(1.0, 1.0, 1.0)
    GL.glVertex3f(-1.0, 1.0, 1.0)
    
    # Back face - Green
    GL.glColor3f(0.0, 1.0, 0.0)
    GL.glNormal3f(0.0, 0.0, -1.0)
    GL.glVertex3f(-1.0, -1.0, -1.0)
    GL.glVertex3f(-1.0, 1.0, -1.0)
    GL.glVertex3f(1.0, 1.0, -1.0)
    GL.glVertex3f(1.0, -1.0, -1.0)
    
    # Top face - Blue
    GL.glColor3f(0.0, 0.0, 1.0)
    GL.glNormal3f(0.0, 1.0, 0.0)
    GL.glVertex3f(-1.0, 1.0, -1.0)
    GL.glVertex3f(-1.0, 1.0, 1.0)
    GL.glVertex3f(1.0, 1.0, 1.0)
    GL.glVertex3f(1.0, 1.0, -1.0)
    
    # Bottom face - Yellow
    GL.glColor3f(1.0, 1.0, 0.0)
    GL.glNormal3f(0.0, -1.0, 0.0)
    GL.glVertex3f(-1.0, -1.0, -1.0)
    GL.glVertex3f(1.0, -1.0, -1.0)
    GL.glVertex3f(1.0, -1.0, 1.0)
    GL.glVertex3f(-1.0, -1.0, 1.0)
    
    # Right face - Magenta
    GL.glColor3f(1.0, 0.0, 1.0)
    GL.glNormal3f(1.0, 0.0, 0.0)
    GL.glVertex3f(1.0, -1.0, -1.0)
    GL.glVertex3f(1.0, 1.0, -1.0)
    GL.glVertex3f(1.0, 1.0, 1.0)
    GL.glVertex3f(1.0, -1.0, 1.0)
    
    # Left face - Cyan
    GL.glColor3f(0.0, 1.0, 1.0)
    GL.glNormal3f(-1.0, 0.0, 0.0)
    GL.glVertex3f(-1.0, -1.0, -1.0)
    GL.glVertex3f(-1.0, -1.0, 1.0)
    GL.glVertex3f(-1.0, 1.0, 1.0)
    GL.glVertex3f(-1.0, 1.0, -1.0)
    
    GL.glEnd()

def draw_triangule():
    GL.glBegin(GL.GL_TRIANGLE_STRIP)
    cant_segmentos = 16
    for i in range(cant_segmentos + 1):
        angle = 2 * 3.14159 / cant_segmentos * i  # i 16-ths of a full circle
        x = math.cos(angle)
        y = math.sin(angle)
        GL.glNormal3f(x, y, 0)  # Normal for both vertices at this angle.
        GL.glVertex3f(x, y, 1)  # Vertex on the top edge.
        GL.glVertex3f(x, y, -1)  # Vertex on the bottom edge.
    GL.glEnd()

def display():
    global rotation
    
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    GL.glLoadIdentity()
    
    # Position the camera
    GLU.gluLookAt(5.0, 5.0, 5.0,  # Eye position
                  0.0, 0.0, 0.0,  # Look at point
                  0.0, 1.0, 0.0)  # Up vector
    
    

    # Rotate the cube
    GL.glPushMatrix()
    GL.glRotatef(rotation, 1.0, 1.0, 1.0)    
    # Draw the colored cube
    draw_colored_cube()
    GL.glPopMatrix()

    # Rotate the triangle
    GL.glPushMatrix()
    GL.glRotatef(rotation, 1.0, 1.0, 1.0)
    GL.glTranslatef(3.0, 0.0, 0.0)
    draw_triangule()
    GL.glPopMatrix()


    GLUT.glutSwapBuffers()

def idle():
    """Animation function"""
    global rotation
    rotation += 0.5
    if rotation >= 360.0:
        rotation = 0.0
    GLUT.glutPostRedisplay()

def keyboard(key, x, y):
    """Handle keyboard input"""
    if key == b'\x1b':  # ESC key
        sys.exit()
    elif key == b' ':  # Space bar to toggle animation
        pass  # You can add pause functionality here


if __name__ == '__main__':
    main()
