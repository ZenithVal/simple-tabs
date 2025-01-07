import bpy
from . import tab_list
from . import panel


classes = (
    tab_list.TabList,
    panel.MainPanel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
