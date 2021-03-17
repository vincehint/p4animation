import bpy
import math
import mathutils
from mathutils import Vector

#In the case where the object is already selected

#Name the object so we can work with it
#Sphere = bpy.data.objects["Sphere"]

##Changes the location of the object
#Sphere.delta_location = mathutils.Vector((2, 1, 1))

class MakeTetrahedron(bpy.types.Operator):
    bl_idname = "mesh.make_tetrahedron"
    bl_label = "Add Tetrahedron"
    
    def invoke(self, context, event):
        Vertices = [
                mathutils.Vector((0, -1 / math.sqrt(3),0)),
                mathutils.Vector((0.5, 1 / (2 * math.sqrt(3)), 0)),
                mathutils.Vector((-0.5, 1 / (2 * math.sqrt(3)), 0)),
                mathutils.Vector((0, 0, math.sqrt(2 / 3))),
            ]
            
        NewMesh = bpy.data.meshes.new("Tetrahedron")
        
        NewMesh.from_pydata (
                Vertices,
                [],
                [[0, 2, 1], [0, 1, 3], [1, 2, 3], [2, 0, 3]]
            )
        NewMesh.update()
        NewObj = bpy.data.objects.new("Tetrahedron", NewMesh)
        context.collection.objects.link(NewObj)
        return {"FINISHED"}

def register():
    bpy.utils.register_class(MakeTetrahedron)
    
def unregister():
    bpy.utils.unregister_class(MakeTetrahedron)
    
if __name__ == "__main__":
    register()