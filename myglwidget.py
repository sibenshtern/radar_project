# This Python file uses the following encoding: utf-8
import pygame.Color as color

from PySide6.QtOpenGLWidgets import QOpenGLWidget

class MyGLWidget(QOpenGLWidget):
    def __init__(self):
        super().__init__()

    def initializeGL():

        # Set up the rendering context, load shaders and other resources, etc.:
        f = QOpenGLContext.currentContext().functions()
        f.glClearColor(color("#98f5ff"))

    def resizeGL(w, h):

        # Update projection matrix and other size related settings:
        m_projection.setToIdentity()
        m_projection.perspective(45.0f, w / float(h), 0.01f, 100.0f)

    def paintGL():
        f = QOpenGLContext.currentContext().functions()
        f.glClear(GL_COLOR_BUFFER_BIT)


# if __name__ == "__main__":
#     pass
