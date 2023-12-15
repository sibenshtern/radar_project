from modeling.shader_program import ShaderProgram
from modeling.vbo import VBO


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {
            'cube': self.get_vao(
                program=self.program.programs['default'],
                vbo=self.vbo.vbos['cube']
            ),
            'aircraft': self.get_vao(
                program=self.program.programs['default'],
                vbo=self.vbo.vbos['aircraft']
            ),
            'radar': self.get_vao(
                program=self.program.programs['default'],
                vbo=self.vbo.vbos['radar']
            )
        }

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program,
                                    [(vbo.vbo, vbo.format, *vbo.attrib)])
        return vao

    def destroy(self):
        self.program.destroy()
        self.vbo.destroy()

