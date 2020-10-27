# coding: utf8
import c4d
import os

from ..Const import Const

const = Const()


class CreationFunction(object):

    def __get_bmp_option(self, path, size):
        #On init un bitmap ave l'image
        temp = c4d.bitmaps.BaseBitmap()
        if temp.InitWith(path)[0] != c4d.IMAGERESULT_OK:
            return False

        #On init un bmp pour resize l'image
        bmp = c4d.bitmaps.BaseBitmap()
        if bmp.Init(int(size/6.5), int(size/6.5), temp.GetBt()) != c4d.IMAGERESULT_OK:
            return False
        bmp.AddChannel(True, True)

        temp.ScaleBicubic(bmp, 0, 0, temp.GetBw()-1, temp.GetBh()-1, 0, 0, bmp.GetBw()-1, bmp.GetBh()-1)

        return bmp

    def __is_last(self, current_id, list):
        if current_id == len(list)-1:
            return True

        return False

    def __is_first(self, current_id, list):
        if current_id == 0:
            return True

        return False

    def get_vector_from_rgb(self, rgb):
        return c4d.Vector(rgb['r'], rgb['g'], rgb['b']) ^ c4d.Vector(1.0 / 255)

    def create_bitmap(self, dialog, ui_id, x, y, state):
        disable_icon = c4d.RESOURCEIMAGE_OBJECTMANAGER_STATE1
        enable_icon = c4d.RESOURCEIMAGE_OBJECTMANAGER_STATE2

        bc = c4d.BaseContainer()
        bc.SetLong(c4d.BITMAPBUTTON_BORDER, c4d.BORDER_NONE)
        bc.SetBool(c4d.BITMAPBUTTON_BUTTON, True)
        bc.SetBool(c4d.BITMAPBUTTON_TOGGLE, True)
        bc.SetLong(c4d.BITMAPBUTTON_ICONID1, disable_icon)          #Off state:         H
        bc.SetLong(c4d.BITMAPBUTTON_ICONID2, enable_icon)             #On State:          H
        myBitButton = dialog.AddCustomGui(ui_id, c4d.CUSTOMGUI_BITMAPBUTTON, "Button",
                                        c4d.BFH_CENTER | c4d.BFV_CENTER, x, y, bc)

        myBitButton.SetToggleState(state)

    def create_min_max_button(self, dialog, ui_id_grp, ui_id_up, ui_id_down, lights_list):
        if dialog.GroupBegin(ui_id_down, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 1, const.STEP):
            size = 71
            dialog.AddStaticText(ui_id_down + 1, c4d.BFH_SCALEFIT | c4d.BFV_TOP, 0, 10, "", c4d.BORDER_NONE)
            dialog.AddSeparatorH(0)


            for i in range(len(lights_list)):
                if dialog.GroupBegin(ui_id_grp + i + 2, c4d.BFH_SCALEFIT | c4d.BFV_TOP, 1, 2, "", c4d.BFV_GRIDGROUP_EQUALROWS):
                    dialog.GroupSpace(1, 1)

                    bc_img = c4d.BaseContainer()
                    bc_img.SetBool(c4d.BITMAPBUTTON_BUTTON, True)
                    path = ""
                    bg_color = self.get_vector_from_rgb(dialog.GetColorRGB(c4d.COLOR_BGGADGET))


                    if self.__is_first(i, lights_list):
                        dialog.GroupBorderSpace(0, 11, 0, 0)
                    else:
                        dialog.GroupBorderSpace(0, 0, 0, 0)
                        path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),'res', 'up.png')

                        custom_gui_up = dialog.AddCustomGui(ui_id_up + i + 2, c4d.CUSTOMGUI_BITMAPBUTTON, "Button", c4d.BFH_CENTER | c4d.BFV_TOP, 0, 0, bc_img)
                        bmp = self.__get_bmp_option(path, size)
                        custom_gui_up.SetImage(bmp)

                    if not self.__is_last(i, lights_list):
                        path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),'res', 'down.png')

                        custom_gui_down = dialog.AddCustomGui(ui_id_down + i + 2, c4d.CUSTOMGUI_BITMAPBUTTON, "Button", c4d.BFH_CENTER | c4d.BFV_BOTTOM, 0, 0, bc_img)
                        bmp = self.__get_bmp_option(path, size)
                        custom_gui_down.SetImage(bmp)

                dialog.GroupEnd()


        dialog.GroupEnd()

    def create_enable(self, dialog, ui_id, light_list):
        if dialog.GroupBegin(ui_id, c4d.BFH_LEFT | c4d.BFV_SCALEFIT, 1, const.STEP):
            dialog.AddStaticText(ui_id + 1, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 10, "", c4d.BORDER_NONE)
            dialog.AddSeparatorH(0)
            for i in range(len(light_list)):
                self.create_bitmap(dialog, ui_id + i + 2, 16, 16, light_list[i]["light"][c4d.ID_BASEOBJECT_GENERATOR_FLAG])
        dialog.GroupEnd()

    def create_button(self, dialog, ui_id, column_name, button_text=None, lights_list=list()):
        if dialog.GroupBegin(ui_id, c4d.BFH_LEFT | c4d.BFV_SCALEFIT, 1, const.STEP):
            dialog.AddStaticText(ui_id + 1, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 10, column_name, c4d.BORDER_NONE)
            dialog.AddSeparatorH(0)
            for i in range(len(lights_list)):
                dialog.AddButton(ui_id + i + 2, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 13, button_text)
        dialog.GroupEnd()

    def create_cycle_button(self, dialog, ui_id, column_name, cycle_data, obj_type=const.OBJ, lights_list=None, id_to_read=None, layers=None):
        if obj_type == const.OBJ:
            txt_type = "light"
        else:
            txt_type = "tag"

        if dialog.GroupBegin(ui_id, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 1, const.STEP):
            dialog.AddStaticText(ui_id + 1, c4d.BFH_SCALEFIT|c4d.BFV_TOP, 0, 10, column_name, c4d.BORDER_NONE)
            dialog.AddSeparatorH(0)
            for i in range(len(lights_list)):
                dialog.AddComboBox(ui_id + i + 2, c4d.BFH_SCALEFIT|c4d.BFV_TOP, 0, 13, False)
                for data in cycle_data:
                    dialog.AddChild(ui_id + i + 2, int(data["id"]), str(data["text"]))

                if lights_list and id_to_read:
                    dialog.SetLong(ui_id + i + 2, int(lights_list[i][txt_type][id_to_read]))

                elif lights_list and id_to_read is None:
                    active_layer = lights_list[i][txt_type][c4d.ID_LAYER_LINK]
                    for y in range(len(layers)):
                        if active_layer == layers[y]:
                            dialog.SetLong(ui_id + i + 2, int(y + 1))

        dialog.GroupEnd()

    def create_edit_string(self, dialog, ui_id, column_name, obj_type=const.OBJ, lights_list=None, refresh=False):
        if obj_type == const.OBJ:
            txt_type = "light"
        else:
            txt_type = "tag"

        if refresh:
            dialog.LayoutFlushGroup(ui_id)
        else:
            dialog.GroupBegin(ui_id, c4d.BFH_LEFT | c4d.BFV_SCALEFIT, 1, const.STEP)

        dialog.AddStaticText(ui_id + 1, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 10, column_name, c4d.BORDER_NONE)
        dialog.AddSeparatorH(0)
        for i in range(len(lights_list)):
            dialog.AddEditText(ui_id + i + 2, c4d.BFH_SCALEFIT | c4d.BFV_TOP, 0, 13)

            if lights_list:
                dialog.SetString(ui_id + i + 2, str(lights_list[i][txt_type].GetName()))
        dialog.GroupEnd()

        if refresh:
            dialog.LayoutChanged(ui_id)

    def create_checkbox(self, dialog, ui_id, column_name, obj_type=const.OBJ, lights_list=None, id_to_read=None):
        if obj_type == const.OBJ:
            txt_type = "light"
        else:
            txt_type = "tag"

        if dialog.GroupBegin(ui_id, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 1, const.STEP):
            dialog.AddStaticText(ui_id + 1, c4d.BFH_SCALEFIT|c4d.BFV_TOP, 0, 10, column_name, c4d.BORDER_NONE)
            dialog.AddSeparatorH(0)
            for i in range(len(lights_list)):
                dialog.AddCheckbox(ui_id + i + 2, c4d.BFH_CENTER | c4d.BFV_TOP, 0, 16, "")

                if lights_list:
                    dialog.SetBool(ui_id + i + 2, bool(lights_list[i][txt_type][id_to_read]))
        dialog.GroupEnd()

    def create_color_field(self, dialog, ui_id, column_name, obj_type=const.OBJ, lights_list=None, id_to_read=None):
        if obj_type == const.OBJ:
            txt_type = "light"
        else:
            txt_type = "tag"

        if dialog.GroupBegin(ui_id, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 1, const.STEP):
            dialog.AddStaticText(ui_id + 1, c4d.BFH_SCALEFIT|c4d.BFV_TOP, 0, 10, column_name, c4d.BORDER_NONE)
            dialog.AddSeparatorH(0)
            for i in range(len(lights_list)):
                dialog.AddColorField(ui_id + i + 2, c4d.BFH_CENTER|c4d.BFV_TOP, 40, 15)

                buffer_vector = lights_list[i][txt_type][id_to_read]
                if not isinstance(buffer_vector, c4d.Vector):
                    buffer_vector = c4d.Vector()
                if lights_list:
                    dialog.SetColorField(ui_id + i + 2, buffer_vector, 1, 1, c4d.DR_COLORFIELD_NO_BRIGHTNESS)

        dialog.GroupEnd()

    def create_number_edit(self, dialog, ui_id, column_name, mode=0, obj_type=const.OBJ, lights_list=None, id_to_read=None, min=0, max=100000, step=1):
        if obj_type == const.OBJ:
            txt_type = "light"
        else:
            txt_type = "tag"

        if dialog.GroupBegin(ui_id, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 1, const.STEP):
            dialog.AddStaticText(ui_id + 1, c4d.BFH_SCALEFIT|c4d.BFV_TOP, 0, 10, column_name, c4d.BORDER_NONE)
            dialog.AddSeparatorH(0)
            for i in range(len(lights_list)):
                dialog.AddEditNumberArrows(ui_id + i + 2, c4d.BFH_SCALEFIT | c4d.BFV_TOP, 0, 16)

                data = lights_list[i][txt_type][id_to_read]
                if not data:
                    continue

                if lights_list:
                    if mode == const.PERCENT_MODE:
                        dialog.SetPercent(ui_id + i + 2, float(data), min, max, step)
                    elif mode == const.METER_MODE:
                        dialog.SetMeter(ui_id + i + 2, float(data), min, max, step)
                    elif mode == const.FLOAT_MODE:
                        dialog.SetFloat(ui_id + i + 2, float(data), min, max, step)
                    elif mode == const.DEGREE_MODE:
                        dialog.SetDegree(ui_id + i + 2, float(data), min, max, step)
                    else:
                        dialog.SetFloat(ui_id + i + 2, float(data), min, max, step)
        dialog.GroupEnd()
