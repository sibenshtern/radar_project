import glm

from objects.aircraft import Aircraft
from coordinates.vectors import Vector3D
from coordinates import Coordinates3D

from objects.maneuvers import CenterFold, ChangeSpeed, ChangeHeight


class BaseModel:
    def __init__(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0),
                 scale=(1, 1, 1)):
        self.app = app
        self.position = pos
        self.rot = glm.vec3(*(glm.radians(a) for a in rot))
        self.scale = scale
        self.vao = app.mesh.vao.vaos[vao_name]
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.program = self.vao.program
        self.camera = self.app.camera

    def update(self): ...

    def get_model_matrix(self):
        m_model = glm.mat4()
        # translate
        m_model = glm.translate(m_model, tuple(self.position))
        # rotate
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        # scale
        m_model = glm.scale(m_model, self.scale)
        return m_model

    def render(self):
        self.update()
        self.vao.render()


class Cube(BaseModel):
    def __init__(self, app, vao_name='cube', tex_id=0, pos=(0, 0, 0),
                 rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use()
        self.program['m_model'].write(self.m_model)
        self.program['m_view'].write(self.app.camera.m_view)
        self.program['camPos'].write(self.app.camera.position)

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.program['m_proj'].write(self.app.camera.m_proj)
        self.program['m_view'].write(self.app.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)


class AircraftModel(BaseModel, Aircraft):
    def __init__(self, app, vao_name='aircraft', tex_id='aircraft',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(1, 0.5, 1),
                 speed=(-0.05, 0, 0), name='aircraft'):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        Aircraft.__init__(self, name, Coordinates3D(*pos), Vector3D(*speed),
                          Vector3D(0, 0, 0))
        self.on_init()

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.program['m_proj'].write(self.app.camera.m_proj)
        self.program['m_view'].write(self.app.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)

    def update(self):
        self.texture.use()
        self.program['m_model'].write(self.m_model)
        self.program['m_view'].write(self.app.camera.m_view)
        self.program['camPos'].write(self.app.camera.position)
        Aircraft.update(self)

        self.m_model = self.get_model_matrix()

    def change_speed(self):
        change_speed = ChangeSpeed(240, self, Vector3D(-0.1, 0.1, 0))
        self.make_maneuver(change_speed)

    def centerfold(self):
        centerfold = CenterFold(240, self)
        self.make_maneuver(centerfold)

    def change_height(self):
        change_height = ChangeHeight(240, self, 15)
        self.make_maneuver(change_height)

    def rotate(self):
        self.rot = glm.vec3(self.rot.x + 45, self.rot.y + 0, self.rot.z + 0)
