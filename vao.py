from vbo import VBO
from shader_program import ShaderProgram


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        #self.vaos['laser'] = self.get_vao(
        #    program=self.program.programs['default'],
        #    vbo=self.vbo.vbos['laser']
        #)

        # cube vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cube']
        )

        # aircraft vao
        self.vaos['aircraft'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['aircraft']
        )

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attrib)])
        return vao

    def destroy(self):
        self.program.destroy()
        self.vbo.destroy()

