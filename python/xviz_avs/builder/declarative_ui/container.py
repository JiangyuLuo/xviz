from xviz_avs.builder.declarative_ui import *


class XVIZContainerBuilder(XVIZBaseUiBuilder):
    def __init__(self, name, layout=None, interactions=None, **kwargs):
        super().__init__(UI_TYPES.CONTAINER, **kwargs)
        self._name = name
        self._layout = layout
        self._interactions = interactions
        self._children = []

        self._validate()

    def _validate(self):
        if self._name is None:
            self._validateError('Panel must have a "name" set')

    def child(self, child):
        self._children.append(child)
        return child

    def get_ui(self):
        obj = super().get_ui()
        obj["name"] = self._name

        if len(self._children):
            obj["children"] = [child.get_ui() for child in self._children]

        if self._layout:
            obj["layout"] = self._layout

        if self._interactions:
            obj["interactions"] = self._interactions

        return obj
