from modeling.texture import Texture
from modeling.vao import VAO


class Mesh:
    def __init__(self, app):
        self.app = app
        self.vao = VAO(app.ctx)
        self.texture = Texture(app.ctx)

    def destroy(self):
        self.vao.destroy()
        self.texture.destroy()