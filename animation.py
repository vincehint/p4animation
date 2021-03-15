#this is my first script in blender yay!
import bpy
from math import sin,cos,radians
#from mathutils import Vector

#pos = Vector((0.5, 0.5, 0.5))
#init_x = pos.x
#init_y = pos.y
#base = 4

#for xcubes in range(base):
#    bpy.ops.mesh.primitive_cube_add(size = 1, location = pos)
#    pos.x += 2
#    
#pos.x = init_x

#def fibonnaci(a):
#    x = 0
#    y = 1
#    z = 1
#    while x < a:
#        x, y = y, x + y
for j in range(0,91,5):
    bpy.ops.mesh.primitive_uv_sphere_add()
    for i in range(0, 361, 6):
    #    bpy.ops.mesh.primitive_cube_add(location=(15*cos(radians(i)),15*sin(radians(i)),4*sin(radians(i*6))))
        obj = bpy.context.object
        obj.location = 15*cos(radians(i+j)),15*sin(radians(i+j)),4*sin(radians(i*6+j))
    
    obj.keyframe_insert(data_path="location", frame=i)