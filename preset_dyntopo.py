import bpy
from bl_operators.presets import AddPresetBase
from bl_ui.utils import PresetPanel


class PRESET_FOR_DYNTOPO_MT_dyntopo_preset(bpy.types.Menu):
    bl_label = "New Preset"
    preset_subdir = "PresetForDyntopo/dyntopo_preset"
    preset_operator = "script.execute_preset"
    draw = bpy.types.Menu.draw_preset


class PRESET_FOR_DYNTOPO_OT_dyntopo_preset_add(AddPresetBase, bpy.types.Operator):
    bl_idname = "preset_for_dyntopo.dyntopo_preset_add"
    bl_label = "Add Dyntopo Preset"
    preset_menu = "PRESET_FOR_DYNTOPO_MT_dyntopo_preset"

    preset_defines = ["sculpt = bpy.context.scene.tool_settings.sculpt"]

    preset_values = [
        "sculpt.constant_detail_resolution",
        "sculpt.detail_size",
        "sculpt.detail_percent",
        "sculpt.detail_refine_method",
        "sculpt.detail_type_method",
    ]

    preset_subdir = "PresetForDyntopo/dyntopo_preset"
