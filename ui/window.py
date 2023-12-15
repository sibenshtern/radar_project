import os
import sys

import moderngl as mgl
import pygame as pg

from logic.radar import Radar
from modeling.camera import Camera
from modeling.light import Light
from modeling.mesh import Mesh
from modeling.scene import Scene


class Window:
    def __init__(self, qt_app, win_size=(1000, 800)):
        # init pygame modules
        pg.init()

        # window size
        self.WIN_SIZE = win_size
        self.qt_app = qt_app

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
        # pg.event.set_grab(True)
        # pg.mouse.set_visible(False)
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

        self.aircraft_index = 0

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN
                                         and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_o:
                self.qt_app.create_object_dialog()
            if event.type == pg.KEYDOWN and event.key == pg.K_v:
                self.qt_app.open_change_speed()
            if event.type == pg.KEYDOWN and event.key == pg.K_c:
                self.qt_app.open_centerfold()
            if event.type == pg.KEYDOWN and event.key == pg.K_h:
                self.qt_app.open_change_height()
            if event.type == pg.KEYDOWN and event.key == pg.K_i:
                self.scene.show_signals = not self.scene.show_signals
            if event.type == pg.KEYDOWN and event.key == pg.K_p:
                self.scene.signals.extend(
                    self.scene.radar.emitter.send_signals(self.scene.time)
                )
            if event.type == pg.KEYDOWN and event.key == pg.K_t:
                self.scene.show_trajectories = not self.scene.show_trajectories
            if event.type == pg.KEYDOWN and event.key == pg.K_m:
                if self.scene.is_simulation:
                    self.qt_app.stop_simulation()
                else:
                    self.qt_app.start_simulation()
            if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                self.scene.objects[self.aircraft_index].tex_id = 'aircraft'
                self.aircraft_index = (self.aircraft_index - 1) % len(
                    self.scene.objects)
                self.scene.objects[
                    self.aircraft_index].tex_id = 'selected_aircraft'
            if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                self.scene.objects[self.aircraft_index].tex_id = 'aircraft'
                self.aircraft_index = (self.aircraft_index + 1) % len(
                    self.scene.objects)
                self.scene.objects[
                    self.aircraft_index].tex_id = 'selected_aircraft'

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
    os.mkdir("log")
    app = Window()
    app.run()
