import bpy

positions = (0, 0, 0), (0, 3, 2), (4, 3, 6), (3, 5, 4), (7, -1, 3), (3, 20, 7), (4, 7, 2), (0, 3, 2), (0, 0, 0)
#start_pos = (0, 0, 0)

ob = bpy.data.objects["Sphere"]
#ob.location = start_pos
frame_num = 0

for position in positions:
#    ob.location = start_pos
    bpy.context.scene.frame_set(frame_num)
    ob.location = position
    ob.keyframe_insert(data_path="location", frame=frame_num)
    frame_num += 20