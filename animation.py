#this is my first script in blender yay!
import bpy
from mathutils import Vector

pos = Vector((0.5, 0.5, 0.5))
init_x = pos.x
init_y = pos.y
base = 4

for xcubes in range(base):
    bpy.ops.mesh.primitive_cube_add(size = 1, location = pos)
    pos.x += 1
    
pos.x = init_x

