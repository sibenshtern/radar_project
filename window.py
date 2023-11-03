import time

import pygame as pg
import moderngl as mgl
import sys

from model import *
from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene

from radar import Radar
from objects.aircraft import Aircraft
from signal import Signal


class Window:
    def __init__(self, win_size=(1000, 800)):
        # init pygame modules
        pg.init()
        # window size
        self.WIN_SIZE = win_size
        # set opengl attr
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # create opengl context: double buffering provides two complete color buffers for use in drawing
        self.screen = pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
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
        # scene=
        self.scene = Scene(self, Radar(), [], [], 10000, self.time)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_o:
                self.scene.add_object(Aircraft_model(self, pos=(5, 5, 0)))
            if event.type == pg.KEYDOWN and event.key == pg.K_v:
                var = self.scene.objects[len(self.scene.objects) - 1]
                var.change_speed()
            if event.type == pg.KEYDOWN and event.key == pg.K_r:
                var = self.scene.objects[len(self.scene.objects) - 1]
                var.rotate()
            if event.type == pg.KEYDOWN and event.key == pg.K_i:
                self.scene.send_signals()

    def render(self):
        # clear framebuffer and color in specified normalized form: 0 ... 255 -> 0.0 ... 1.0
        self.ctx.clear(color=(0.08, 0.16, 0.18))

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
            [obj.update() for obj in self.scene.objects]
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(24)


if __name__ == '__main__':
    app = Window()
    app.run()
