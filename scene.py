from camera import *

class Scene:
    def __init__(self, name):
        self.name = name
        self.camera = Camera(True, 640, 480)
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def render(self, screen):
        camera_matrix = self.camera.get_camera_matrix()
        projection_matrix = self.camera.get_projection_matrix()

        clip_matrix = camera_matrix @ projection_matrix

        toDraw = [] #TODO
        # dict dist:obj
        # sort by dist

        for obj in self.objects:
            d = obj.position - self.camera.position
            if(d.x >= obj.scale.x/2 or d.z >= obj.scale.z/2):
                d.normalize()
                dProduct = d.dot(vector3.from_np(self.camera.get_facing()).normalized())
                if(dProduct > math.cos(self.camera.fov)):
                    obj.render(screen, clip_matrix)

