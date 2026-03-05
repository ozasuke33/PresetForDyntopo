bl_info = {
    "name": "PresetForDyntopo",
    "author": "ozasuke",
    "description": "Preset for Dyntopo",
    "blender": (4, 2, 0),
    "version": (1, 0, 0),
    "location": "3D Vieport",
    "warning": "",
    "category": "Object",
}

import bpy

from .preset_dyntopo import *

classess = [
    PRESET_FOR_DYNTOPO_MT_dyntopo_preset,
    PRESET_FOR_DYNTOPO_OT_dyntopo_preset_add,
]


def preset_menu_dyntopo(self, context):
    layout = self.layout

    row = layout.row(align=True)
    row.menu(
        PRESET_FOR_DYNTOPO_MT_dyntopo_preset.__name__,
        text=PRESET_FOR_DYNTOPO_MT_dyntopo_preset.bl_label,
    )
    row.operator(
        PRESET_FOR_DYNTOPO_OT_dyntopo_preset_add.bl_idname, text="", icon="ADD"
    )
    row.operator(
        PRESET_FOR_DYNTOPO_OT_dyntopo_preset_add.bl_idname, text="", icon="REMOVE"
    ).remove_active = True


def register():
    for cls in classess:
        bpy.utils.register_class(cls)

    bpy.types.VIEW3D_PT_sculpt_dyntopo.prepend(preset_menu_dyntopo)


def unregister():
    for cls in reversed(classess):
        bpy.utils.unregister_class(cls)

    bpy.types.VIEW3D_PT_sculpt_dyntopo.remove(preset_menu_dyntopo)


if __name__ == "__main__":
    register()
