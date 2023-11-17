import glm
import pygame as pg

FOV = 50    # deg
NEAR = 0.1
FAR = 100
SPEED = 0.01
SENSITIVITY = 0.05


class Camera:
    def __init__(self, app, position=(0, 0, 3), yaw=90, pitch=0):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 0, 1)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 1, 0)
        self.yaw = yaw
        self.pitch = pitch
        self.roll = -10
        # view matrix
        self.m_view = self.get_view_matrix()
        # projection matrix
        self.m_proj = self.get_projection_matrix()

    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        # pg.mouse.set_pos(500, 800)
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY
        self.pitch = max(-89, min(89, self.pitch))

    def update_camera_vectors(self):
        yaw, pitch, roll = glm.radians(self.yaw), glm.radians(self.pitch), glm.radians(self.roll)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        # roll_mat = glm.rotate(glm.mat4(1.0), roll, self.forward)

        self.forward = glm.mat3(1, 0, 0, 0, 0, 1, 0, -1, 0) * glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 0, 1)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))
        # self.up = glm.mat3(roll_mat) * self.up

    def update(self):
        self.move()
        self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()

    def move(self):
        velocity = SPEED * self.app.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.position += self.forward * velocity
        if keys[pg.K_s]:
            self.position -= self.forward * velocity
        if keys[pg.K_a]:
            self.position -= self.right * velocity
        if keys[pg.K_d]:
            self.position += self.right * velocity
        if keys[pg.K_q]:
            self.position += self.up * velocity
        if keys[pg.K_e]:
            self.position -= self.up * velocity

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)