import pygame as pg
import moderngl as mgl


class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/test.png')
        self.textures[1] = self.get_texture(path='textures/grass.png')
        self.textures['aircraft'] = self.get_texture(
            #path='objects/WWII_Plane_Japan_Kawasaki_Ki-61_v1_L2.12b7c514a6-be0e-41be-b76d-35020244d960/14082_WWII_Plane_Japan_Kawasaki_Ki-61_diffuse_v1.jpg'
            path='objects/Cat/20430_cat_diff_v1.jpg'
        )

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        # texture.fill('red')
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
