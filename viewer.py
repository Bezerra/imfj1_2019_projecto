# Import pygame into our program
import pygame
import pygame.freetype
import time
import constant

from scene import *
from object3d import *
from mesh import *
from material import *
from color import *


# Define a main function, just to keep things nice and tidy
def main():
    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res_x = 640
    res_y = 480

    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    # Create a scene
    scene = Scene("TestScene")
    scene.camera = Camera(False, res_x, res_y)

    # Moves the camera back 2 units
    scene.camera.position -= vector3(0,0,2)

    # Create a cube and place it in a scene, at position (0,0,0)
    # This cube has 1 unit of side, and is red
    obj1 = Object3d("TestObject")
    obj1.scale = vector3(1, 1, 1)
    obj1.position = vector3(0, -1, 0)
    obj1.mesh = Mesh.create_cube((1, 1, 1))
    obj1.material = Material(color(1,0,0,1), "TestMaterial1")
    scene.add_object(obj1)

    # Create a second object, and add it as a child of the first object
    # When the first object rotates, this one will also mimic the transform
    obj2 = Object3d("ChildObject")
    obj2.position += vector3(0, 0.75, 0)
    obj2.mesh = Mesh.create_cube((0.5, 0.5, 0.5))
    obj2.material = Material(color(0,1,0,1), "TestMaterial2")
    obj1.add_child(obj2)

    #initialize axis, angle, and velocity
    angle = 0
    axis = vector3(0,0,0)
    velocity = 0

    # Timer
    delta_time = 0
    prev_time = time.time()

    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return

            # Checks for keys being pressed
            elif (event.type == pygame.KEYDOWN):
                # Rotation
                if (event.key == pygame.K_LEFT):
                    axis = constant.Y_AXIS
                    angle = constant.ROT_ANGLE
                if (event.key == pygame.K_RIGHT):
                    axis = constant.Y_AXIS
                    angle = -constant.ROT_ANGLE
                if (event.key == pygame.K_UP):
                    axis = constant.X_AXIS
                    angle = constant.ROT_ANGLE
                if (event.key == pygame.K_DOWN):
                    axis = constant.X_AXIS
                    angle = -constant.ROT_ANGLE
                if (event.key == pygame.K_PAGEUP):
                    axis = constant.Z_AXIS
                    angle = constant.ROT_ANGLE
                if (event.key == pygame.K_PAGEDOWN):
                    axis = constant.Z_AXIS
                    angle = -constant.ROT_ANGLE

                # Movement
                if (event.key == pygame.K_w):
                    axis = constant.Y_AXIS
                    velocity = constant.VELOCITY
                if (event.key == pygame.K_s):
                    axis = constant.Y_AXIS
                    velocity = -constant.VELOCITY
                if (event.key == pygame.K_a):
                    axis = constant.X_AXIS
                    velocity = constant.VELOCITY
                if (event.key == pygame.K_d):
                    axis = constant.X_AXIS
                    velocity = -constant.VELOCITY
                if (event.key == pygame.K_q):
                    axis = constant.Z_AXIS
                    velocity = constant.VELOCITY
                if (event.key == pygame.K_e):
                    axis = constant.Z_AXIS
                    velocity = -constant.VELOCITY

            # Checks for keys being released
            elif (event.type == pygame.KEYUP):
                if (event.key == pygame.K_ESCAPE):
                  return
                if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or \
                    event.key == pygame.K_UP or event.key == pygame.K_DOWN or \
                        event.key == pygame.K_PAGEDOWN or event.key == pygame.K_PAGEUP):
                    axis = vector3(0, 0, 0)
                    angle = 0
                if (event.key == pygame.K_a or event.key == pygame.K_d or \
                    event.key == pygame.K_s or event.key == pygame.K_w or \
                        event.key == pygame.K_q or event.key == pygame.K_e):
                    axis = vector3(0, 0, 0)
                    velocity = 0

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))

        # Updates the scene
        # Moves the camera, considering the time passed (not linked to frame rate)
        mov = axis * velocity * delta_time
        scene.camera.position = mov + scene.camera.position

        # Rotates the object, considering the time passed (not linked to frame rate)
        q = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3())
        obj1.rotation = q * obj1.rotation

        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()


# Run the main function
main()
