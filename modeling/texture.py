import moderngl as mgl
import pygame as pg


class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {
            0: self.get_texture(path='./textures/img.png'),
            1: self.get_texture(path='./textures/grass_t.jpg'),
            'aircraft': self.get_texture(
                path='./textures/Aircraft_Texture.png'
            ),
            'selected_aircraft': self.get_texture(
                path='./textures/Aircraft_Texture_negate.png'
            ),
            'radar': self.get_texture(
                path='./textures/img.png'
            )
        }

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        # mipmaps
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        # AF
        texture.anisotropy = 32.0
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]
