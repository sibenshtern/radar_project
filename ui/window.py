import pygame as pg
import moderngl as mgl
import sys

from modeling.model import AircraftModel
from modeling.camera import Camera
from modeling.light import Light
from modeling.mesh import Mesh
from modeling.scene import Scene

from logic.radar import Radar


class Window:
    def __init__(self, win_size=(1000, 800)):
        # init pygame modules
        pg.init()

        # window size
        self.WIN_SIZE = win_size

        # set opengl attr
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,
                                    pg.GL_CONTEXT_PROFILE_CORE)

        # create opengl context: double buffering provides two complete color
        # buffers for use in drawing
        self.screen = pg.display.set_mode(self.WIN_SIZE,
                                          flags=pg.OPENGL | pg.DOUBLEBUF)

        # mouse settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        # detect and use existing opengl context
        self.ctx = mgl.create_context()

        # self.ctx.front_face = 'cw'
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)

        # create an object to help track time
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        # light
        self.light = Light()
        # camera
        self.camera = Camera(self)
        # mesh
        self.mesh = Mesh(self)
        self.scene = Scene(self, Radar(), [], [], 10000,
                           self.time)

        self.__aircraft_index = 0

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN
                                         and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_o:
                self.scene.add_object(
                    AircraftModel(self, pos=(5, 0, 10), rot=(0, 0, -90),
                                  scale=(0.2, 0.2, 0.2),
                                  name=f'aircraft #{self.__aircraft_index}')
                )
                self.__aircraft_index += 1
            if event.type == pg.KEYDOWN and event.key == pg.K_v:
                var = self.scene.objects[len(self.scene.objects) - 1]
                var.change_speed()
            if event.type == pg.KEYDOWN and event.key == pg.K_c:
                var = self.scene.objects[len(self.scene.objects) - 1]
                var.centerfold()
            if event.type == pg.KEYDOWN and event.key == pg.K_h:
                var = self.scene.objects[len(self.scene.objects) - 1]
                var.change_height()
            if event.type == pg.KEYDOWN and event.key == pg.K_r:
                var = self.scene.objects[len(self.scene.objects) - 1]
                var.rotate()
            if event.type == pg.KEYDOWN and event.key == pg.K_i:
                self.scene.show_signals = not self.scene.show_signals
            if event.type == pg.KEYDOWN and event.key == pg.K_p:
                self.scene.signals.extend(
                    self.scene.radar.emitter.send_signals(self.scene.time)
                )
            if event.type == pg.KEYDOWN and event.key == pg.K_t:
                self.scene.show_trajectories = not self.scene.show_trajectories
            if event.type == pg.KEYDOWN and event.key == pg.K_m:
                self.scene.is_simulation = not self.scene.is_simulation

    def render(self):
        # clear framebuffer and color in
        # specified normalized form: 0 ... 255 -> 0.0 ... 1.0
        self.ctx.clear(color=(0.302, 0.5451, 0.9412, 0.5))

        # render scene
        self.scene.render()

        # swap buffers
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()

            self.camera.update()
            self.scene.update()
            self.render()
            self.delta_time = self.clock.tick(24)


if __name__ == '__main__':
    app = Window()
    app.run()
