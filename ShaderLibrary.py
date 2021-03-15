bl_info = {
    "name": "Shader Library",
    "author": "Vince",
    "version": (1, 0),
    "blender": (2, 98, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new shader to your Object",
    "warning": "",
    "doc_url": "",
    "category": "Add Shader",
}

import bpy

class ShaderMainPanel(bpy.types.Panel):
    bl_label = "Shader_Library"
    bl_idname = "SHADER_PT_PANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_cATEGORY = 'Shader Library'

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text= "Select a Shader to be added.")
        row.operator('shader.diamond_operator')
        
        
        
#Creates a custom operator for the diamond shader        
class SHADER_OT_DIAMOND(bpy.types.Operator):
    bl_label = "Diamond"
    bl_idname = 'shader.diamond_operator'
    
    def execute(self, context):
        #Create diamond shader
        material_diamond = bpy.data.materials.new(name= "Diamond")
        material_diamond.use_nodes = True    
        
        material_diamond.node_tree.nodes.remove(material_diamond.node_tree.nodes.get('Principled BSDF'))
        
        material_output = material_diamond.node_tree.nodes.get('Material Output')
        material_output.location = (-400, 0)
        # create nodes
        glass1_node =  material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass1_node.hide = True
        glass1_node.location = (-600, 0)
        glass1_node.inputs[0].default_value = (1, 0, 0, 1)
        glass1_node.inputs[2].default_value = 1.446
        glass1_node.select = False
        
        glass2_node =  material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass2_node.hide = True
        glass2_node.location = (-600, -150)
        glass2_node.inputs[0].default_value = (0, 1, 0, 1)
        glass2_node.inputs[2].default_value = 1.450
        glass2_node.select = False
        
        glass3_node =  material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass3_node.hide = True
        glass3_node.location = (-600, -300)
        glass3_node.inputs[0].default_value = (0, 0, 1, 1)
        glass3_node.inputs[2].default_value = 1.450
        glass3_node.select = False
        
        glass4_node =  material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass4_node.hide = True
        glass4_node.location = (-150, -150)
        glass4_node.inputs[0].default_value = (1, 1, 1, 1)
        glass4_node.inputs[2].default_value = 1.450
        glass4_node.select = False
        
        add1_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        add1_node.location = (-400, -50)
        add1_node.label = "Add 1"
        add1_node.hide = True
        add1_node.select = False
        
        add2_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        add2_node.location = (-100, 0)
        add2_node.label = "Add 2"
        add2_node.hide = True
        add2_node.select = False
        
        mix1_node = material_diamond.node_tree.nodes.new('ShaderNodeMixShader')
        mix1_node.location = (200, 0)
        mix1_node.select = False
        #create linkes between nodes
        material_diamond.node_tree.links.new(glass1_node.outputs[0], add1_node.inputs[0])
        material_diamond.node_tree.links.new(glass2_node.outputs[0], add1_node.inputs[1])
        material_diamond.node_tree.links.new(add1_node.outputs[0], add2_node.inputs[0])
        material_diamond.node_tree.links.new(glass3_node.outputs[0], add2_node.inputs[1])
        material_diamond.node_tree.links.new(add2_node.outputs[0], mix1_node.inputs[1])
        material_diamond.node_tree.links.new(glass4_node.outputs[0], mix1_node.inputs[2])
        material_diamond.node_tree.links.new(mix1_node.outputs[0], material_output.inputs[0])
        
        bpy.context.object.active_material = material_diamond
        
        return {'FINISHED'}
        
        
        
        
def register():
    bpy.utils.register_class(ShaderMainPanel)
    bpy.utils.register_class(SHADER_OT_DIAMOND)
    
    
def unregister():
    bpy.utils.unregister_class(ShaderMainPanel)
    bpy.utils.unregister_class(SHADER_OT_DIAMOND)
    
if __name__ == "__main__":
    register()