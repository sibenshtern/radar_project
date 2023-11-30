import glm


class Light:
    def __init__(self, position=(0, 0, 15), color=(1, 1, 1)):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        # intensities
        self.Ia = 0.4 * self.color  # ambient
        self.Id = 1 * self.color  # diffuse
        self.Is = 0.1 * self.color  # specular
