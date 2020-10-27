import c4d

from ..Const import Const

const = Const()

class InteractionFunction(object):

    def selection_interaction(self, doc, ui_id, clicked_id, msg, c4d_lights, obj_type=const.OBJ):
        if obj_type == const.OBJ:
            txt_type = "light"
        else:
            txt_type = "tag"

        if ui_id <= clicked_id < ui_id + const.STEP:
            light_id = clicked_id - ui_id - 2
            if c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, c4d.BFM_INPUT_CHANNEL, msg):
                if msg[c4d.BFM_INPUT_QUALIFIER] & c4d.QCTRL:
                    doc.SetSelection(c4d_lights[light_id][txt_type], c4d.SELECTION_ADD)
                elif msg[c4d.BFM_INPUT_QUALIFIER] & c4d.QALT:
                    doc.SetSelection(c4d_lights[light_id][txt_type], c4d.SELECTION_SUB)
                else:
                    doc.SetSelection(c4d_lights[light_id][txt_type], c4d.SELECTION_NEW)

    def set_bc_tag(self, light, new_id):
        buffer_tag = light.GetTag(const.PLUGIN_ID_TAG)
        if not buffer_tag:
            return

        bc_tag = buffer_tag.GetDataInstance().GetContainerInstance(const.PLUGIN_ID_TAG)
        bc_tag[0] = True
        bc_tag[1] = new_id

    def order_interaction_up(self, dialog, doc, ui_id, clicked_id, rs_lights):
        if ui_id <= clicked_id < ui_id + const.STEP:
            light_id = clicked_id - ui_id - 2

            #Get current light and previous light
            current_light = rs_lights[light_id]
            previous_light = rs_lights[light_id-1]

            #Set current light order to -1
            current_light["id"] -= 1
            self.set_bc_tag(current_light["light"], current_light["id"])

            #Set previous light order to +1
            previous_light["id"] += 1
            self.set_bc_tag(previous_light["light"], previous_light["id"])

            #refresh ui
            dialog.refreshLightData()

    def order_interaction_down(self, dialog, doc, ui_id, clicked_id, rs_lights):
        if ui_id <= clicked_id < ui_id + const.STEP:
            light_id = clicked_id - ui_id - 2

            #Get current light and next light
            current_light = rs_lights[light_id]
            next_light = rs_lights[light_id+1]

            #Set current light order to +1
            current_light["id"] += 1
            self.set_bc_tag(current_light["light"], current_light["id"])

            #Set next light order to -1
            next_light["id"] -= 1
            self.set_bc_tag(next_light["light"], next_light["id"])

            #refresh ui
            dialog.refreshLightData()

    def order_interaction(self, dialog, doc, ui_id, clicked_id, rs_lights):
        if ui_id <= clicked_id < ui_id + const.STEP:
            light_id = clicked_id - ui_id - 2
            ui_data = dialog.GetInt32(clicked_id)

            ecart = 0
            new_value = 0

            if ecart > 0:
                for light in rs_lights[light_id+1:ui_data+1]:
                    if light_id != light["id"]:
                        light["id"] -= 1
                        new_value = light["id"]
                        self.set_bc_tag(light["light"], new_value)

            elif ecart < 0:
                for light in rs_lights[ui_data:light_id]:
                    if light_id != light["id"]:
                        light["id"] += 1
                        new_value = light["id"]
                        self.set_bc_tag(light["light"], new_value)

            rs_lights[light_id]["id"] = ui_data
            self.set_bc_tag(rs_lights[light_id]["light"], ui_data)

            dialog.refreshLightData()

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

    def enable_interaction(self, dialog, doc, ui_id, clicked_id, c4d_lights, obj_type=const.OBJ):
        if obj_type == const.OBJ:
            txt_type = "light"
        else:
            txt_type = "tag"

        if ui_id <= clicked_id < ui_id + const.STEP:
            light_id = clicked_id - ui_id - 2
            current_state = c4d_lights[light_id][txt_type][c4d.ID_BASEOBJECT_GENERATOR_FLAG]

            ui_data = dialog.FindCustomGui(clicked_id, c4d.CUSTOMGUI_BITMAPBUTTON)
            ui_data.SetToggleState(not bool(current_state))

            doc.AddUndo(c4d.UNDOTYPE_CHANGE, c4d_lights[light_id][txt_type])
            c4d_lights[light_id][txt_type][c4d.ID_BASEOBJECT_GENERATOR_FLAG] = not bool(current_state)

    def name_interaction(self, dialog, doc, ui_id, clicked_id, c4d_lights, obj_type=const.OBJ):
        if obj_type == const.OBJ:
            txt_type = "light"
        else:
            txt_type = "tag"

        if ui_id <= clicked_id < ui_id + const.STEP:
            light_id = clicked_id - ui_id - 2
            ui_data = dialog.GetString(clicked_id)

            doc.AddUndo(c4d.UNDOTYPE_CHANGE, c4d_lights[light_id][txt_type])
            c4d_lights[light_id][txt_type].SetName(ui_data)

    def long_interaction(self, dialog, doc, ui_id, clicked_id, c4d_lights, id_to_change, obj_type=const.OBJ):
        if obj_type == const.OBJ:
            txt_type = "light"
        else:
            txt_type = "tag"

        if ui_id <= clicked_id < ui_id + const.STEP:
            light_id = clicked_id - ui_id - 2
            ui_data = dialog.GetLong(clicked_id)

            doc.AddUndo(c4d.UNDOTYPE_CHANGE, c4d_lights[light_id][txt_type])
            c4d_lights[light_id][txt_type][id_to_change] = ui_data

    def bool_interaction(self, dialog, doc, ui_id, clicked_id, c4d_lights, id_to_change, obj_type=const.OBJ):
        if obj_type == const.OBJ:
            txt_type = "light"
        else:
            txt_type = "tag"

        if ui_id <= clicked_id < ui_id + const.STEP:
            light_id = clicked_id - ui_id - 2
            ui_data = dialog.GetBool(clicked_id)

            doc.AddUndo(c4d.UNDOTYPE_CHANGE, c4d_lights[light_id][txt_type])
            c4d_lights[light_id][txt_type][id_to_change] = ui_data

    def color_interaction(self, dialog, doc, ui_id, clicked_id, c4d_lights, id_to_change, obj_type=const.OBJ):
        if obj_type == const.OBJ:
            txt_type = "light"
        else:
            txt_type = "tag"

        if ui_id <= clicked_id < ui_id + const.STEP:
            light_id = clicked_id - ui_id - 2
            ui_data = dialog.GetColorField(clicked_id)["color"]

            doc.AddUndo(c4d.UNDOTYPE_CHANGE, c4d_lights[light_id][txt_type])
            c4d_lights[light_id][txt_type][id_to_change] = ui_data

    def float_interaction(self, dialog, doc, ui_id, clicked_id, c4d_lights, id_to_change, obj_type=const.OBJ):
        if obj_type == const.OBJ:
            txt_type = "light"
        else:
            txt_type = "tag"

        if ui_id <= clicked_id < ui_id + const.STEP:
            light_id = clicked_id - ui_id - 2
            ui_data = dialog.GetFloat(clicked_id)

            doc.AddUndo(c4d.UNDOTYPE_CHANGE, c4d_lights[light_id][txt_type])
            c4d_lights[light_id][txt_type][id_to_change] = ui_data

    def layer_interaction(self, dialog, doc, ui_id, clicked_id, c4d_lights, layers, obj_type=const.OBJ):
        if obj_type == const.OBJ:
            txt_type = "light"
        else:
            txt_type = "tag"

        if ui_id <= clicked_id < ui_id + const.STEP:
            light_id = clicked_id - ui_id - 2
            ui_data = dialog.GetLong(clicked_id)

            doc.AddUndo(c4d.UNDOTYPE_CHANGE, c4d_lights[light_id][txt_type])
            if not ui_data:
                c4d_lights[light_id][txt_type][c4d.ID_LAYER_LINK] = None
            else:
                c4d_lights[light_id][txt_type][c4d.ID_LAYER_LINK] = layers[ui_data-1]

    def long_interaction_corona(self, dialog, doc, ui_id, clicked_id, c4d_lights):

        if ui_id <= clicked_id < ui_id + const.STEP:
            light_id = clicked_id - ui_id - 2
            ui_data = dialog.GetLong(clicked_id)

            light_obj = c4d_lights[light_id]["light"]
            light_type = light_obj[c4d.CORONA_LIGHT_TYPE]
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, light_obj)
            if light_type == 0:
                light_obj[c4d.CORONA_LIGHT_AREA_SHAPE] = ui_data

            elif light_type == 1:
                light_obj[c4d.CORONA_LIGHT_SECTOR_SHAPE] = ui_data

            elif light_type == 2:
                light_obj[c4d.CORONA_LIGHT_OBJECT_SHAPE] = ui_data
