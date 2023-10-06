import sys

from OpenGL import GL as gl
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from PySide6.QtOpenGLWidgets import QOpenGLWidget


class MyWidget(QOpenGLWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5, OpenGL 3.3")
        self.resize(700, 400)

    def initializeGL(self):
        gl.glClearColor(0.0, 0.0, 0.0, 1)

    def iterate(self):
        gl.glViewport(0, 0, 500, 500)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()

    def square(self):
        gl.glColor3f(1.0, 0.0, 3.0)
        gl.glBegin(gl.GL_QUADS)
        gl.glVertex2f(100, 100)
        gl.glVertex2f(200, 100)
        gl.glVertex2f(200, 200)
        gl.glVertex2f(100, 200)
        gl.glEnd()

    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glLoadIdentity()
        self.iterate()
        self.square()


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_UseDesktopOpenGL)
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
