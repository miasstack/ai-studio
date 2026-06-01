"""
Block Quest — Character Model Generator
Creates stylized low-poly placeholder characters for all 6 KidNation crew members.
Exports each as FBX to the Unity project.
Run: blender --background --python create_blockquest_characters.py
"""
import bpy
import bmesh
import mathutils
import os
import math

OUTPUT_DIR = os.path.expanduser("~/Desktop/BlockQuest/Assets/Prefabs/Characters")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Helpers ──────────────────────────────────────────────────────────────────

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for block in bpy.data.meshes:  bpy.data.meshes.remove(block)
    for block in bpy.data.materials: bpy.data.materials.remove(block)
    for block in bpy.data.armatures: bpy.data.armatures.remove(block)

def make_material(name, color, metallic=0.0, roughness=0.6):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get('Principled BSDF')
    bsdf.inputs['Base Color'].default_value = (*color, 1.0)
    bsdf.inputs['Metallic'].default_value = metallic
    bsdf.inputs['Roughness'].default_value = roughness
    return mat

def assign_mat(obj, mat):
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)

def add_sphere(name, loc, scale, mat=None):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=loc, segments=12, ring_count=8)
    obj = bpy.context.active_object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(scale=True)
    if mat: assign_mat(obj, mat)
    return obj

def add_capsule(name, loc, scale, mat=None):
    # Blender 5.x: use cylinder as capsule substitute
    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, location=loc, vertices=12)
    obj = bpy.context.active_object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(scale=True)
    if mat: assign_mat(obj, mat)
    return obj

def add_cylinder(name, loc, scale, mat=None, rot=(0,0,0)):
    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=1, location=loc,
        rotation=rot, vertices=8)
    obj = bpy.context.active_object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(scale=True)
    if mat: assign_mat(obj, mat)
    return obj

def add_cube(name, loc, scale, mat=None):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    obj = bpy.context.active_object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(scale=True)
    if mat: assign_mat(obj, mat)
    return obj

def parent_to(child, parent):
    child.parent = parent

def join_objects(objects):
    bpy.ops.object.select_all(action='DESELECT')
    for o in objects:
        o.select_set(True)
    bpy.context.view_layer.objects.active = objects[0]
    bpy.ops.object.join()
    return bpy.context.active_object

def add_armature(char_name, body_top_z, body_height):
    """Add a basic T-pose armature."""
    bpy.ops.object.armature_add(location=(0, 0, 0))
    arm_obj = bpy.context.active_object
    arm_obj.name = f"{char_name}_Armature"
    arm = arm_obj.data
    arm.name = f"{char_name}_Rig"

    bpy.ops.object.mode_set(mode='EDIT')
    bones = arm.edit_bones

    # Remove default bone
    for b in list(bones): bones.remove(b)

    hip_z = body_top_z - body_height * 0.5
    chest_z = body_top_z - body_height * 0.15
    neck_z = body_top_z + 0.05
    head_z = body_top_z + 0.35

    def add_bone(name, head, tail, parent=None):
        b = bones.new(name)
        b.head = mathutils.Vector(head)
        b.tail = mathutils.Vector(tail)
        if parent: b.parent = bones[parent]
        return b

    add_bone("Hips",        (0, 0, hip_z),    (0, 0, chest_z))
    add_bone("Spine",       (0, 0, chest_z),  (0, 0, neck_z), "Hips")
    add_bone("Neck",        (0, 0, neck_z),   (0, 0, head_z), "Spine")
    add_bone("Head",        (0, 0, head_z),   (0, 0, head_z + 0.3), "Neck")
    add_bone("UpperArm.L",  (0, 0, chest_z),  (0.4, 0, chest_z), "Spine")
    add_bone("LowerArm.L",  (0.4, 0, chest_z),(0.75, 0, chest_z), "UpperArm.L")
    add_bone("Hand.L",      (0.75, 0, chest_z),(0.9, 0, chest_z), "LowerArm.L")
    add_bone("UpperArm.R",  (0, 0, chest_z),  (-0.4, 0, chest_z), "Spine")
    add_bone("LowerArm.R",  (-0.4, 0, chest_z),(-0.75, 0, chest_z), "UpperArm.R")
    add_bone("Hand.R",      (-0.75, 0, chest_z),(-0.9, 0, chest_z), "LowerArm.R")
    add_bone("UpperLeg.L",  (0.15, 0, hip_z), (0.15, 0, hip_z - 0.45), "Hips")
    add_bone("LowerLeg.L",  (0.15, 0, hip_z - 0.45),(0.15, 0, hip_z - 0.9), "UpperLeg.L")
    add_bone("Foot.L",      (0.15, 0, hip_z - 0.9),(0.15, 0.2, hip_z - 0.95), "LowerLeg.L")
    add_bone("UpperLeg.R",  (-0.15, 0, hip_z),(-0.15, 0, hip_z - 0.45), "Hips")
    add_bone("LowerLeg.R",  (-0.15, 0, hip_z - 0.45),(-0.15, 0, hip_z - 0.9), "UpperLeg.R")
    add_bone("Foot.R",      (-0.15, 0, hip_z - 0.9),(-0.15, 0.2, hip_z - 0.95), "LowerLeg.R")

    bpy.ops.object.mode_set(mode='OBJECT')
    return arm_obj

def export_fbx(filepath, objects):
    bpy.ops.object.select_all(action='DESELECT')
    for o in objects: o.select_set(True)
    bpy.ops.export_scene.fbx(
        filepath=filepath,
        use_selection=True,
        global_scale=1.0,
        apply_unit_scale=True,
        bake_space_transform=True,
        mesh_smooth_type='FACE',
        use_mesh_modifiers=True,
        add_leaf_bones=False,
        path_mode='COPY',
        embed_textures=False,
    )
    print(f"Exported: {filepath}")

# ── Character Builders ────────────────────────────────────────────────────────

def build_jordan():
    """Jordan: Leader. Red leather jacket, box braids, confident stance."""
    clear_scene()
    skin   = make_material("Jordan_Skin",   (0.42, 0.28, 0.18))
    jacket = make_material("Jordan_Jacket", (0.85, 0.08, 0.08))
    jeans  = make_material("Jordan_Jeans",  (0.18, 0.27, 0.48))
    shoes  = make_material("Jordan_Shoes",  (0.75, 0.75, 0.78))
    hair   = make_material("Jordan_Hair",   (0.05, 0.03, 0.02))
    gold   = make_material("Jordan_Gold",   (1.0, 0.78, 0.0), metallic=0.9)

    # Body
    torso  = add_capsule("Jordan_Torso",  (0,0,1.10), (0.28,0.20,0.38), jacket)
    hips   = add_capsule("Jordan_Hips",   (0,0,0.68), (0.25,0.18,0.20), jeans)
    # Legs
    lleg   = add_capsule("Jordan_LLeg",   ( 0.14,0,0.30), (0.10,0.10,0.30), jeans)
    rleg   = add_capsule("Jordan_RLeg",   (-0.14,0,0.30), (0.10,0.10,0.30), jeans)
    lshoe  = add_sphere ("Jordan_LShoe",  ( 0.14,0.05,0.04),(0.11,0.15,0.07), shoes)
    rshoe  = add_sphere ("Jordan_RShoe",  (-0.14,0.05,0.04),(0.11,0.15,0.07), shoes)
    # Arms T-pose
    larm   = add_capsule("Jordan_LArm",   ( 0.45,0,1.12), (0.08,0.08,0.25), jacket)
    rarm   = add_capsule("Jordan_RArm",   (-0.45,0,1.12), (0.08,0.08,0.25), jacket)
    lhand  = add_sphere ("Jordan_LHand",  ( 0.70,0,1.12), (0.07,0.07,0.08), skin)
    rhand  = add_sphere ("Jordan_RHand",  (-0.70,0,1.12), (0.07,0.07,0.08), skin)
    larm.rotation_euler[2] =  math.radians(90)
    rarm.rotation_euler[2] = -math.radians(90)
    # Head
    head   = add_sphere ("Jordan_Head",   (0,0,1.68), (0.22,0.20,0.22), skin)
    # Box braids — 4 cylinders hanging down
    for i, x in enumerate([-0.10, -0.03, 0.03, 0.10]):
        braid = add_cylinder(f"Jordan_Braid{i}", (x, -0.04, 1.75), (0.025,0.025,0.25), hair)
        braid.location.z = 1.55
    # Gold chain
    chain  = add_cylinder("Jordan_Chain", (0,0.19,1.28), (0.05,0.01,0.05), gold,
                           rot=(math.radians(90),0,0))

    all_objs = [torso,hips,lleg,rleg,lshoe,rshoe,larm,rarm,lhand,rhand,head,chain]
    all_objs += [bpy.data.objects[f"Jordan_Braid{i}"] for i in range(4)]
    arm = add_armature("Jordan", 1.55, 1.10)
    return all_objs + [arm]

def build_melli():
    """Melli: Curly big hair, pink bomber, hoop earrings."""
    clear_scene()
    skin   = make_material("Melli_Skin",   (0.55, 0.35, 0.22))
    jacket = make_material("Melli_Jacket", (0.95, 0.50, 0.65))
    jeans  = make_material("Melli_Jeans",  (0.20, 0.20, 0.22))
    shoes  = make_material("Melli_Shoes",  (0.95, 0.95, 0.95))
    hair   = make_material("Melli_Hair",   (0.25, 0.12, 0.05))
    gold   = make_material("Melli_Gold",   (1.0, 0.78, 0.0), metallic=0.9)

    torso  = add_capsule("Melli_Torso",   (0,0,1.10), (0.28,0.20,0.38), jacket)
    hips   = add_capsule("Melli_Hips",    (0,0,0.68), (0.25,0.18,0.20), jeans)
    lleg   = add_capsule("Melli_LLeg",    ( 0.14,0,0.30), (0.10,0.10,0.30), jeans)
    rleg   = add_capsule("Melli_RLeg",    (-0.14,0,0.30), (0.10,0.10,0.30), jeans)
    lshoe  = add_sphere ("Melli_LShoe",   ( 0.14,0.05,0.04),(0.11,0.14,0.07), shoes)
    rshoe  = add_sphere ("Melli_RShoe",   (-0.14,0.05,0.04),(0.11,0.14,0.07), shoes)
    larm   = add_capsule("Melli_LArm",    ( 0.45,0,1.12), (0.08,0.08,0.25), jacket)
    rarm   = add_capsule("Melli_RArm",    (-0.45,0,1.12), (0.08,0.08,0.25), jacket)
    lhand  = add_sphere ("Melli_LHand",   ( 0.70,0,1.12), (0.07,0.07,0.08), skin)
    rhand  = add_sphere ("Melli_RHand",   (-0.70,0,1.12), (0.07,0.07,0.08), skin)
    larm.rotation_euler[2] =  math.radians(90)
    rarm.rotation_euler[2] = -math.radians(90)
    head   = add_sphere ("Melli_Head",    (0,0,1.68), (0.21,0.19,0.21), skin)
    # Big curly hair — cluster of spheres
    hair_positions = [(0,0,1.95),(0.14,0,1.85),(-.14,0,1.85),(0,0.08,1.88),
                      (0.10,0.07,1.92),(-.10,0.07,1.92),(0,-0.05,1.82)]
    for i, p in enumerate(hair_positions):
        s = 0.15 if i==0 else 0.11
        add_sphere(f"Melli_Hair{i}", p, (s,s,s), hair)
    # Hoop earrings
    for x, name in [(0.20,"Melli_EarL"),(-0.20,"Melli_EarR")]:
        add_cylinder(name, (x,-0.04,1.62), (0.04,0.005,0.04), gold, rot=(math.radians(90),0,0))

    all_objs = [torso,hips,lleg,rleg,lshoe,rshoe,larm,rarm,lhand,rhand,head]
    all_objs += [bpy.data.objects[f"Melli_Hair{i}"] for i in range(7)]
    all_objs += [bpy.data.objects["Melli_EarL"], bpy.data.objects["Melli_EarR"]]
    arm = add_armature("Melli", 1.55, 1.10)
    return all_objs + [arm]

def build_nari():
    """Nari: Long blue-black ponytail, olive green jumpsuit, orange boots."""
    clear_scene()
    skin     = make_material("Nari_Skin",     (0.72, 0.55, 0.40))
    jumpsuit = make_material("Nari_Jumpsuit", (0.28, 0.35, 0.18))
    boots    = make_material("Nari_Boots",    (0.88, 0.45, 0.05))
    hair     = make_material("Nari_Hair",     (0.03, 0.03, 0.22))
    gold     = make_material("Nari_Gold",     (1.0, 0.78, 0.0), metallic=0.9)

    torso    = add_capsule("Nari_Torso",  (0,0,1.10), (0.27,0.19,0.38), jumpsuit)
    hips     = add_capsule("Nari_Hips",   (0,0,0.68), (0.24,0.17,0.20), jumpsuit)
    lleg     = add_capsule("Nari_LLeg",   ( 0.13,0,0.30), (0.095,0.095,0.30), jumpsuit)
    rleg     = add_capsule("Nari_RLeg",   (-0.13,0,0.30), (0.095,0.095,0.30), jumpsuit)
    lboot    = add_cylinder("Nari_LBoot", ( 0.13,0,0.06), (0.10,0.12,0.11), boots)
    rboot    = add_cylinder("Nari_RBoot", (-0.13,0,0.06), (0.10,0.12,0.11), boots)
    larm     = add_capsule("Nari_LArm",   ( 0.44,0,1.12), (0.08,0.08,0.24), jumpsuit)
    rarm     = add_capsule("Nari_RArm",   (-0.44,0,1.12), (0.08,0.08,0.24), jumpsuit)
    lhand    = add_sphere ("Nari_LHand",  ( 0.68,0,1.12), (0.07,0.07,0.07), skin)
    rhand    = add_sphere ("Nari_RHand",  (-0.68,0,1.12), (0.07,0.07,0.07), skin)
    larm.rotation_euler[2] =  math.radians(90)
    rarm.rotation_euler[2] = -math.radians(90)
    head     = add_sphere ("Nari_Head",   (0,0,1.65), (0.20,0.19,0.20), skin)
    # Long ponytail — cylinder hanging behind
    pony_base = add_sphere("Nari_PonyBase", (0,-0.18,1.80), (0.10,0.06,0.10), hair)
    ponytail  = add_cylinder("Nari_Ponytail", (0,-0.20,1.45), (0.055,0.055,0.40), hair)
    pony_tip  = add_sphere("Nari_PonyTip", (0,-0.22,1.10), (0.06,0.06,0.06), hair)
    # Top knot
    top_knot  = add_sphere("Nari_TopKnot", (0,0,1.88), (0.10,0.10,0.12), hair)
    # Gold hoops
    for x, name in [(0.19,"Nari_EarL"),(-0.19,"Nari_EarR")]:
        add_cylinder(name, (x,-0.04,1.59), (0.04,0.005,0.04), gold, rot=(math.radians(90),0,0))

    all_objs = [torso,hips,lleg,rleg,lboot,rboot,larm,rarm,lhand,rhand,head,
                pony_base,ponytail,pony_tip,top_knot,
                bpy.data.objects["Nari_EarL"], bpy.data.objects["Nari_EarR"]]
    arm = add_armature("Nari", 1.52, 1.10)
    return all_objs + [arm]

def build_salome():
    """Salome: Red curly puffs, green eyes, red jacket."""
    clear_scene()
    skin   = make_material("Salome_Skin",   (0.85, 0.65, 0.52))
    jacket = make_material("Salome_Jacket", (0.82, 0.08, 0.08))
    jeans  = make_material("Salome_Jeans",  (0.22, 0.30, 0.50))
    shoes  = make_material("Salome_Shoes",  (0.92, 0.92, 0.92))
    hair   = make_material("Salome_Hair",   (0.72, 0.22, 0.05))

    torso  = add_capsule("Salome_Torso",  (0,0,1.05), (0.26,0.19,0.36), jacket)
    hips   = add_capsule("Salome_Hips",   (0,0,0.65), (0.23,0.17,0.19), jeans)
    lleg   = add_capsule("Salome_LLeg",   ( 0.13,0,0.28), (0.09,0.09,0.28), jeans)
    rleg   = add_capsule("Salome_RLeg",   (-0.13,0,0.28), (0.09,0.09,0.28), jeans)
    lshoe  = add_sphere ("Salome_LShoe",  ( 0.13,0.05,0.04),(0.10,0.13,0.07), shoes)
    rshoe  = add_sphere ("Salome_RShoe",  (-0.13,0.05,0.04),(0.10,0.13,0.07), shoes)
    larm   = add_capsule("Salome_LArm",   ( 0.42,0,1.07), (0.075,0.075,0.23), jacket)
    rarm   = add_capsule("Salome_RArm",   (-0.42,0,1.07), (0.075,0.075,0.23), jacket)
    lhand  = add_sphere ("Salome_LHand",  ( 0.65,0,1.07), (0.065,0.065,0.07), skin)
    rhand  = add_sphere ("Salome_RHand",  (-0.65,0,1.07), (0.065,0.065,0.07), skin)
    larm.rotation_euler[2] =  math.radians(90)
    rarm.rotation_euler[2] = -math.radians(90)
    head   = add_sphere ("Salome_Head",   (0,0,1.60), (0.20,0.19,0.20), skin)
    # Two curly puffs on top
    lpuff  = add_sphere ("Salome_LPuff",  ( 0.13,0,1.85), (0.12,0.12,0.12), hair)
    rpuff  = add_sphere ("Salome_RPuff",  (-0.13,0,1.85), (0.12,0.12,0.12), hair)
    # Extra curls on each puff
    for i, (x, z) in enumerate([(0.18,1.82),(0.08,1.92),(-0.18,1.82),(-0.08,1.92)]):
        add_sphere(f"Salome_Curl{i}", (x,0,z), (0.07,0.07,0.07), hair)

    all_objs = [torso,hips,lleg,rleg,lshoe,rshoe,larm,rarm,lhand,rhand,head,lpuff,rpuff]
    all_objs += [bpy.data.objects[f"Salome_Curl{i}"] for i in range(4)]
    arm = add_armature("Salome", 1.48, 1.05)
    return all_objs + [arm]

def build_arjun():
    """Arjun: South Asian, pompadour, maroon KN vest, white shirt."""
    clear_scene()
    skin  = make_material("Arjun_Skin",  (0.50, 0.32, 0.20))
    vest  = make_material("Arjun_Vest",  (0.45, 0.05, 0.12))
    shirt = make_material("Arjun_Shirt", (0.95, 0.95, 0.95))
    pants = make_material("Arjun_Pants", (0.92, 0.90, 0.88))
    shoes = make_material("Arjun_Shoes", (0.42, 0.08, 0.12))
    hair  = make_material("Arjun_Hair",  (0.04, 0.03, 0.03))

    torso = add_capsule("Arjun_Torso",  (0,0,1.12), (0.27,0.19,0.38), vest)
    # Shirt visible under vest as inner layer
    shirt_inner = add_capsule("Arjun_ShirtInner", (0,0,1.12), (0.26,0.21,0.36), shirt)
    hips  = add_capsule("Arjun_Hips",   (0,0,0.68), (0.24,0.17,0.20), pants)
    lleg  = add_capsule("Arjun_LLeg",   ( 0.13,0,0.30), (0.095,0.095,0.30), pants)
    rleg  = add_capsule("Arjun_RLeg",   (-0.13,0,0.30), (0.095,0.095,0.30), pants)
    lshoe = add_sphere ("Arjun_LShoe",  ( 0.13,0.05,0.04),(0.10,0.14,0.07), shoes)
    rshoe = add_sphere ("Arjun_RShoe",  (-0.13,0.05,0.04),(0.10,0.14,0.07), shoes)
    larm  = add_capsule("Arjun_LArm",   ( 0.44,0,1.14), (0.08,0.08,0.25), shirt)
    rarm  = add_capsule("Arjun_RArm",   (-0.44,0,1.14), (0.08,0.08,0.25), shirt)
    lhand = add_sphere ("Arjun_LHand",  ( 0.69,0,1.14), (0.07,0.07,0.07), skin)
    rhand = add_sphere ("Arjun_RHand",  (-0.69,0,1.14), (0.07,0.07,0.07), skin)
    larm.rotation_euler[2] =  math.radians(90)
    rarm.rotation_euler[2] = -math.radians(90)
    head  = add_sphere ("Arjun_Head",   (0,0,1.68), (0.21,0.19,0.21), skin)
    # Pompadour — tall swept-back cylinder on top front
    pompa = add_cylinder("Arjun_Pompa", (0.04,-0.04,1.90), (0.12,0.08,0.14), hair,
                         rot=(math.radians(15),0,0))

    all_objs = [torso,shirt_inner,hips,lleg,rleg,lshoe,rshoe,larm,rarm,lhand,rhand,head,pompa]
    arm = add_armature("Arjun", 1.55, 1.12)
    return all_objs + [arm]

def build_bjorn():
    """Bjorn: Blonde shaggy hair, orange scarf, cream hoodie, cargo pants."""
    clear_scene()
    skin   = make_material("Bjorn_Skin",   (0.90, 0.72, 0.58))
    hoodie = make_material("Bjorn_Hoodie", (0.93, 0.91, 0.85))
    pants  = make_material("Bjorn_Pants",  (0.52, 0.48, 0.38))
    shoes  = make_material("Bjorn_Shoes",  (0.85, 0.83, 0.78))
    hair   = make_material("Bjorn_Hair",   (0.90, 0.75, 0.25))
    scarf  = make_material("Bjorn_Scarf",  (0.90, 0.42, 0.05))

    torso  = add_capsule("Bjorn_Torso",  (0,0,1.12), (0.29,0.21,0.38), hoodie)
    hips   = add_capsule("Bjorn_Hips",   (0,0,0.68), (0.26,0.19,0.20), pants)
    lleg   = add_capsule("Bjorn_LLeg",   ( 0.14,0,0.30), (0.10,0.10,0.30), pants)
    rleg   = add_capsule("Bjorn_RLeg",   (-0.14,0,0.30), (0.10,0.10,0.30), pants)
    lshoe  = add_sphere ("Bjorn_LShoe",  ( 0.14,0.05,0.04),(0.11,0.15,0.08), shoes)
    rshoe  = add_sphere ("Bjorn_RShoe",  (-0.14,0.05,0.04),(0.11,0.15,0.08), shoes)
    larm   = add_capsule("Bjorn_LArm",   ( 0.46,0,1.14), (0.08,0.08,0.25), hoodie)
    rarm   = add_capsule("Bjorn_RArm",   (-0.46,0,1.14), (0.08,0.08,0.25), hoodie)
    lhand  = add_sphere ("Bjorn_LHand",  ( 0.71,0,1.14), (0.07,0.07,0.08), skin)
    rhand  = add_sphere ("Bjorn_RHand",  (-0.71,0,1.14), (0.07,0.07,0.08), skin)
    larm.rotation_euler[2] =  math.radians(90)
    rarm.rotation_euler[2] = -math.radians(90)
    head   = add_sphere ("Bjorn_Head",   (0,0,1.68), (0.21,0.20,0.21), skin)
    # Shaggy hair — several overlapping spheres at different heights
    hair_pts = [(0,0,1.90),(0.12,0.02,1.85),(-0.12,0.02,1.85),
                (0.08,-0.08,1.82),(-0.08,-0.08,1.82),(0,0.10,1.82)]
    for i, p in enumerate(hair_pts):
        add_sphere(f"Bjorn_Hair{i}", p, (0.12,0.10,0.10), hair)
    # Orange scarf loop around neck
    scarf_obj = add_cylinder("Bjorn_Scarf", (0,0,1.42), (0.20,0.20,0.06), scarf,
                              rot=(0,0,0))

    all_objs = [torso,hips,lleg,rleg,lshoe,rshoe,larm,rarm,lhand,rhand,head,scarf_obj]
    all_objs += [bpy.data.objects[f"Bjorn_Hair{i}"] for i in range(6)]
    arm = add_armature("Bjorn", 1.55, 1.12)
    return all_objs + [arm]

# ── Main ─────────────────────────────────────────────────────────────────────

characters = [
    ("Jordan", build_jordan),
    ("Melli",  build_melli),
    ("Nari",   build_nari),
    ("Salome", build_salome),
    ("Arjun",  build_arjun),
    ("Bjorn",  build_bjorn),
]

for name, builder in characters:
    print(f"\n[BlockQuest] Building {name}...")
    objects = builder()
    filepath = os.path.join(OUTPUT_DIR, f"{name}.fbx")
    export_fbx(filepath, objects)
    print(f"[BlockQuest] ✓ {name}.fbx exported")

print("\n[BlockQuest] All 6 characters exported to:")
print(f"  {OUTPUT_DIR}")
print("[BlockQuest] Done.")
