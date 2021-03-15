bl_info = {
    "name" : "Object Addon",
    "author" : "Vince",
    "version" : (1,0),
    "blender" : (2,92,0),
    "location" : "View3d > Tool",
    "warning" : "",
    "wikie_url" : "",
    "category" : "Add Mesh",
    
}


import bpy







class TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My 1st Addon"
    
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.4
        row = layout.row()
        row.label(text= "Add An Object", icon= 'CUBE') 
        row = layout.row() 
        row.operator("mesh.primitive_cube_add", icon= 'CUBE')   
        row = layout.row() 
        row.operator("mesh.primitive_uv_sphere_add", icon= "SPHERE") 
        row = layout.row()
        row.operator("object.text_add", icon= 'FILE_FONT', text = "Font Button")
        
        
class PanelA(bpy.types.Panel):
    bl_label = "Scale"
    bl_idname = "PT_PanelA"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My 1st Addon"
    bl_parent_id = "PT_TestPanel"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.label(text= "Select an option to scale your object.", icon= "FONT_DATA")
        row = layout.row()
        row.operator("transform.resize")
        row = layout.row()
        layout.scale_y = 1.4
        col = layout.column()
        col.prop(obj, "scale")
        
        
class PanelB(bpy.types.Panel):
    bl_label = "Specials"
    bl_idname = "PT_PanelB"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My 1st Addon"
    bl_parent_id = "PT_TestPanel"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.4
        row = layout.row()
        row.label(text= "Select a Special Option", icon= "COLOR_BLUE")
        row = layout.row()
        row.operator("object.shade_smooth")
        row = layout.row()
        row.operator("object.subdivision_set")
        row = layout.row()
        row.operator("object.modifier_add")
        
def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)

def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(PanelB)
    
if __name__ == "__main__":
    register()