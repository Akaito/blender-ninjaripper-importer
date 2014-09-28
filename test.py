import bpy
#import mathutils
#from mathutils import Vector

import re

'''
def createMeshFromPrimitive(name, origin):
    bpy.ops.mesh.primitive_cube_add()

    ob = bpy.context.object
    ob.name = name
    ob.show_name = True
    me = ob.data
    me.name = name+'Mesh'
    return ob
'''


def create_new_object(vert_coords, edges, faces):
    # Create, position, and link new model/mesh
    me = bpy.data.meshes.new('RippedMesh')
    ob = bpy.data.objects.new('RippedModel', me)
    ob.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(ob)
    bpy.context.scene.objects.active = ob
    ob.select = True

    # Fill mesh with verts, edges, faces
    me.from_pydata(vert_coords, edges, faces)
    me.update(calc_edges=True)


def import_ninja_ripdump(filename, origin_pos):
    f = open(filename, mode='r')
    l = f.readline()
    print(l)
    if 'RIPDUMP 1.1' not in l:
        print('Bad file!')
        return

    vert_pattern = re.compile('([0-9]{6}):.* ([-0-9.]+) .* ([-0-9.]+) .* ([-0-9.]+) .* ([-0-9.]+) .* ([-0-9.]+) .* ([-0-9.]+) .* ([-0-9.]+) .* ([-0-9.]+) .* ([-0-9.]+) .* ([-0-9.]+)$')
    face_pattern = re.compile('([0-9]{6}):.* (\d+) (\d+) (\d+)$')

    vert_coords = []
    vert_norms = []
    vert_tex_coords = []
    faces = []

    for l in f.readlines():
        # Try to read vertex
        m = vert_pattern.match(l)
        if m:
            vert_coords.append((
                float(m.group(2)),
                float(m.group(3)),
                float(m.group(4))
            ))
            vert_norms.append((
                float(m.group(5)),
                float(m.group(6)),
                float(m.group(7))
            ))
            vert_tex_coords.append((
                float(m.group(8)),
                float(m.group(9))
            ))
            continue
        # Try to read face
        m = face_pattern.match(l)
        if m:
            faces.append([
                int(m.group(2)),
                int(m.group(3)),
                int(m.group(4))
            ])
            continue
    # end for each line in file

    create_new_object(vert_coords, [], faces)
    return


if __name__ == "__main__":
    import_ninja_ripdump(
        filename="E:/Program Files (x86)/Guild Wars 2/_Ripper/frames/frame00/mesh0005.rip.txt",
        origin_pos=(0, 0, 0)
    )
    print('import done')
