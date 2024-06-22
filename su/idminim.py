import bpy

class MyOperator(bpy.types.Operator):
    bl_idname = "object.my_operator"
    bl_label = "My Operator"

    def execute(self, context):
        # Operator logic goes here
        return {'FINISHED'}

# Register the class
bpy.utils.register_class(MyOperator)
