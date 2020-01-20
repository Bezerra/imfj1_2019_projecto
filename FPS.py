# Import pygame into our program
import pygame
import pygame.freetype
import time
import constant
import random

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

    # Specify the rotation of the camera, and the velocity.
    angle = constant.ROT_ANGLE
    velocity = constant.SPEED_PLAYER
    movAxis = vector3(0,0,0)
    rotAxis = vector3(0,0,0)

    # Moves the camera back 2 units
    scene.camera.position -= vector3(0,0,2)

    # Create between 10-30 random cubes to be palced in the scene
    # I'm writing this on a plane, so I can't check the python documentation for the random function
    cubes = []
    amount = random.randint(constant.MIN_CUBES, constant.MAX_CUBES)

    for current in range(amount):
        cubes.append(Object3d("Cube" + str(current)))
        #rScale = random.random()*constant.RANDOM_SCALE
        cubes[current].scale = vector3(random.random()*constant.RANDOM_SCALE, random.random()*constant.RANDOM_SCALE, random.random()*constant.RANDOM_SCALE)
        cubes[current].position = vector3(random.random()*constant.RANDOM_POSITION, 0, random.random()*constant.RANDOM_POSITION)
        cubes[current].mesh = Mesh.create_cube((1, 1, 1))
        cubes[current].material = Material(color(random.random(), random.random(), random.random()), "Material"+str(current))
        scene.add_object(cubes[current])

        

    # Timer
    delta_time = 0
    prev_time = time.time()

    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    # Game loop, runs forever
    while (True):
        rotAxis = vector3(0, 0, 0)
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return

            # Checks for mouse movement
            if (event.type == pygame.MOUSEMOTION):
                mouseMov = pygame.mouse.get_rel()
                rotAxis = vector3(-mouseMov[1], -mouseMov[0], 0)
                

            # Checks for keys being pressed
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_u):
                    print(str(constant.Z_AXIS.to_np3()))
                    


                # Movement
                if (event.key == pygame.K_w):
                    facingAxis = scene.camera.get_facing()
                    movAxis += vector3.from_np(facingAxis)
                if (event.key == pygame.K_s):
                    facingAxis = scene.camera.get_facing()
                    movAxis -= vector3.from_np(facingAxis)
                if (event.key == pygame.K_a):
                    sideAxis = scene.camera.get_side()
                    movAxis -= vector3.from_np(sideAxis)
                if (event.key == pygame.K_d):
                    sideAxis = scene.camera.get_side()
                    movAxis += vector3.from_np(sideAxis)
                #movAxis.normalize()

            # Checks for keys being released
            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_ESCAPE):
                    return
                if (event.key == pygame.K_w):
                    facingAxis = scene.camera.get_facing()
                    movAxis -= vector3.from_np(facingAxis)
                if (event.key == pygame.K_s):
                    facingAxis = scene.camera.get_facing()
                    movAxis += vector3.from_np(facingAxis)
                if (event.key == pygame.K_a):
                    sideAxis = scene.camera.get_side()
                    movAxis += vector3.from_np(sideAxis)
                if (event.key == pygame.K_d):
                    sideAxis = scene.camera.get_side()
                    movAxis -= vector3.from_np(sideAxis)
                #movAxis.normalize()
            
        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))

        # Updates the scene
        # Moves the camera, considering the time passed (not linked to frame rate)
        mov = movAxis * velocity * delta_time
        scene.camera.position = mov + scene.camera.position

        # Rotates the object, considering the time passed (not linked to frame rate)
        q = from_rotation_vector((rotAxis * math.radians(angle) * delta_time).to_np3())
        scene.camera.rotation = q * scene.camera.rotation

        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()


# Run the main function
main()
