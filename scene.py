from model import *

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        add(Cube(app))
        add(Cube(app, pos=(-2.5, 0, 0), rot=(45, 0, 0), scale=(1, 2, 1)))
        add(Cube(app, pos=(2.5, 0, 0), rot=(0, 0, 45), scale=(1, 1, 2)))

    def render(self):
        for obj in self.objects:
            obj.render()