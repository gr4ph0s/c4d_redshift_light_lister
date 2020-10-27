# coding: utf8
import c4d
import operator

from .Const import Const

const = Const()


class LightManager(object):

    def get_bc_from_tag(self, light):
        tag = light.GetTag(const.PLUGIN_ID_TAG)
        if not tag:
            return False

        bc_tag = tag.GetData().GetContainer(const.PLUGIN_ID_TAG)
        if not bc_tag:
            return False

        if not bc_tag[0]:
            return False

        return bc_tag[1]

    def set_bc_tag(self, light, new_id):
        buffer_tag = light.GetTag(const.PLUGIN_ID_TAG)
        if not buffer_tag:
            buffer_tag = c4d.BaseTag(const.PLUGIN_ID_TAG)
            light.InsertTag(buffer_tag)

        bc_tag = buffer_tag.GetDataInstance().GetContainerInstance(const.PLUGIN_ID_TAG)
        bc_tag[0] = True
        bc_tag[1] = new_id

        c4d.EventAdd()

    def get_redshift_light(self):
        doc = c4d.documents.GetActiveDocument()
        redshift_lights = self.search_light_in_hierarchy(doc.GetFirstObject(), const.LIGHT_ID_REDSHIFT)
        buffer_redshift_light = list()
        new_redshift_light = list()
        for light in redshift_lights:
            buffer = dict()
            buffer["light"] = light
            old_id = self.get_bc_from_tag(light)
            if old_id is False:
                buffer["id"] = 0
                new_redshift_light.append(buffer)
            else:
                buffer["id"] = old_id
                buffer_redshift_light.append(buffer)

        for i, light in enumerate(new_redshift_light):
            light["id"] = len(buffer_redshift_light) + i + 1

        buffer_redshift_light += new_redshift_light
        buffer_redshift_light.sort(key=operator.itemgetter('id'))

        for i, light in enumerate(buffer_redshift_light):
            light["id"] = i
            self.set_bc_tag(light["light"], i)

        return buffer_redshift_light


    def search_light_in_hierarchy(self, op, light_type=c4d.Olight, buffer_all_lights=None):
        if buffer_all_lights is None:
            buffer_all_lights = list()

        while op:
            if op.CheckType(light_type):
                buffer_all_lights.append(op)
            self.search_light_in_hierarchy(op.GetDown(), light_type,  buffer_all_lights)
            op = op.GetNext()
        return buffer_all_lights

    def get_all_layers(self, layer=None, buffer_all_layers=[], first=True):
        if first:
            buffer_all_layers = list()
            doc = c4d.documents.GetActiveDocument()
            layer = doc.GetLayerObjectRoot().GetDown()

        while layer:
            buffer_all_layers.append(layer)
            self.get_all_layers(layer.GetDown(), buffer_all_layers, first=False)
            layer = layer.GetNext()

        return buffer_all_layers