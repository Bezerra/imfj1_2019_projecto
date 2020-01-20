# Project Report

## Student:
- Pedro Albuquerque Bezerra
   - 21900974
   - github.com/bezerra #TODO

## Part 1:
- In this part, I duplicated the sample.py file and renamed it viewer.py.
- I first modified the viewer.py to include events to key down and key up
- The default angle and axis were changed to 0, so it would only move or rotate after user input.
- I created a new file constants.py,  so I could more easily change constant values, like axis, velocity, and angle.
- After making the camera controls, I edited the mesh,py file to include 2 new methods: one to draw a pyramid, beacuse it's a simple shape, and one to fraw triangles, which are common in 3D objects.
- After drawing the pyramids on screen, I tried to make a method to load the information from a file, which I made from a .obj.
- This method failed, even when using the same vertexes as the pyraimid that was working. After some time, I gave up on this method, but it is still on the code, in case you can give me some feedback.

## Part 2:
- Part 2 is way harder, and I wasn't honestly expecting to be able to do it all.
- First, I duplicated again the viewer.py, and named it FPS.py.
- I changed the camera controls to just move the camera in the X and Z axis
- After moving the camera, I made a new environment, from randomized cubes
- To rotate the camera, I get the relative movement from the mouse, and use the coordinates as the rotation matrix.
- This rotation Axis is reset each iteration, otherwise the camera would continue rotating even without mouse movement.
- After rotating, I realized the movement didn't work anymore, since I was using the World Axis, instead of the camera ones. I created to new methos in the camera.py, to get a facing and a side vector, to use isntead of the Z and X axis for the movement.
- To render only the objects in front of the camera, I used the dot product between two vectors: the camera Facing vector, and the difference between the camera and the object.
- This last function is not working properly, but I was tired of seeing the cubes being rendered when the camera was inside or very near them, so I'm calling it progress.
- I plan to render them based on the distance, by creating a dictionary in the style {obj: distance to camera}, and them sorting them by the distance and drawing them. But, at the time of writing this, I'm on a plane, and I can't remember how exactly dictionaries work, so I'll have to do this after landing, if I have the time.