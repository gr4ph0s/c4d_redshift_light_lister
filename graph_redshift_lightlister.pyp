# coding: utf8
import os
import c4d

# localimport-v1.7.3-blob-mcw79
import base64 as b, types as t, zlib as z; m=t.ModuleType('localimport')
blob = b'\
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\
XVw='
exec(z.decompress(b.b64decode(blob)), vars(m))
_localimport = m
localimport = getattr(m, "localimport")
del blob, b, t, z, m

with localimport('.') as importer:
    from src.Const import Const
    from src.Config.ConfigManager import ConfigManager
    from src.LightManager import LightManager
    from src.Creation.CreationRedshift import CreationRedshift
    from src.Interaction.InteractionRedshift import InteractionRedshift

const = Const()


class mainDialog(c4d.gui.GeDialog):
    def __init__(self):
        super().__init__()
        self.lostFocus = False
        self.got_focus = False
        self.to_update = False
        self.event_from_interaction = False
        self.lm = LightManager()
        self.creation = CreationRedshift()
        self.interaction = InteractionRedshift()
        self.redshift_light = []

    def CoreMessage(self, id, msg):
        if id == c4d.EVMSG_CHANGE:
            self.to_update = True

        return c4d.gui.GeDialog.CoreMessage(self, id, msg)

    def Message(self, msg, result):
        if msg.GetId() == c4d.BFM_GOTFOCUS:
            if self.lostFocus:
                self.lostFocus = False
                self.got_focus = True

        elif msg.GetId() == c4d.BFM_LOSTFOCUS:
            self.lostFocus = True

        elif msg.GetId() == c4d.BFM_SCROLLGROUP_SCROLLED:
            new_value = -msg.GetInt32(3)
            light_data = self.GetVisibleArea(const.GRP_TAB_REDSHIFT_SCROLL_LIGHT)
            name_data = self.GetVisibleArea(const.GRP_TAB_REDSHIFT_SCROLL_NAME)

            initial_name_y2 = name_data["y2"] - name_data["y1"]
            initial_light_y2 = light_data["y2"] - light_data["y1"]

            self.SetVisibleArea(const.GRP_TAB_REDSHIFT_SCROLL_NAME,
                                name_data["x1"], new_value,
                                name_data["x2"], initial_name_y2 + new_value
                                )

            self.SetVisibleArea(const.GRP_TAB_REDSHIFT_SCROLL_LIGHT,
                                light_data["x1"], new_value,
                                light_data["x2"], initial_light_y2 + new_value
                                )

        elif msg.GetId() == 1648576083:
            self.creation.refresh_redshift_light(self, self.redshift_light)

        return c4d.gui.GeDialog.Message(self, msg, result)

    def Timer(self, msg):
        if self.config.dataChanged:
            self.refreshLightData()
            self.config.dataChanged = False

        if self.got_focus and self.to_update and not self.event_from_interaction:
            self.got_focus = False
            self.to_update = False
            self.refreshLightData()

    def CreateLayout(self):
        self.doc = c4d.documents.GetActiveDocument()
        self.config = ConfigManager()
        self.redshift_light = self.lm.get_redshift_light()
        self.layers = self.lm.get_all_layers()

        self.SetTitle('Redshift Light Lister v' + str(const.VERSION))
        self.SetTimer(500)

        self.create_menu()

        self.create_rs_data()

        return True

    def create_menu(self):
        # Create the menu
        self.MenuFlushAll()

        # Options menu
        self.MenuSubBegin("Options")
        self.MenuAddString(const.UI_BTN_OPTION, "Options")
        self.MenuSubEnd()

        self.GroupEnd()

    def create_rs_data(self, refresh=False):
        if refresh:
            self.LayoutFlushGroup(const.GRP_MAIN)
        else:
            self.GroupBegin(const.GRP_MAIN, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 1)
            self.GroupBorderSpace(2, 5, 2, 0)

        if self.GroupBegin(const.GRP_TAB_REDSHIFT_GRP + 3, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 300, 200, "Redshift"):
            self.creation.create_redshift_light(self, self.config.redshiftConfig, self.redshift_light, self.layers)
        self.GroupEnd()

        self.GroupEnd()
        if refresh:
            self.LayoutChanged(const.GRP_MAIN)

    def Command(self, id, msg):
        if const.LIGHT_LISTER_REDSHIFT_START < id < const.LIGHT_LISTER_REDSHIFT_END:
            self.event_from_interaction = True

            self.doc.StartUndo()
            self.interaction.redshift_interaction(self, self.doc, id, msg, self.redshift_light, self.layers)
            self.doc.EndUndo()
            c4d.EventAdd()

            self.event_from_interaction = False

        elif id == const.UI_BTN_OPTION:
            self.config.Open(dlgtype=c4d.DLG_TYPE_ASYNC, defaultw=300, defaulth=150, xpos=-1, ypos=-1)

        self.event_from_interaction = False

        return True

    def refreshLightData(self):
        #store existing data
        save_scroll = [
            self.GetVisibleArea(const.GRP_TAB_REDSHIFT_SCROLL_NAME),
            self.GetVisibleArea(const.GRP_TAB_REDSHIFT_SCROLL_LIGHT)
        ]

        #refresh data
        self.doc = c4d.documents.GetActiveDocument()
        self.config.refresh()

        self.redshift_light = self.lm.get_redshift_light()
        self.layers = self.lm.get_all_layers()

        #redraw all light
        self.create_rs_data(True)

        #set scroll
        buffer_data = [
            const.GRP_TAB_REDSHIFT_SCROLL_NAME,
            const.GRP_TAB_REDSHIFT_SCROLL_LIGHT
        ]
        for i in range(len(save_scroll)):
            try:
                self.SetVisibleArea(buffer_data[i], save_scroll[i]["x1"], save_scroll[i]["y1"], save_scroll[i]["x2"], save_scroll[i]["y2"])
            except:
                pass


class UILauncher_Main(c4d.plugins.CommandData):
 dialog = None

 def Execute(self, doc):
    if self.dialog is None:
       self.dialog = mainDialog()
    return self.dialog.Open(dlgtype=c4d.DLG_TYPE_ASYNC, pluginid=const.PLUGIN_ID, defaultw=700, defaulth=450)
        
 def RestoreLayout(self, sec_ref):
    if self.dialog is None:
        self.dialog = mainDialog()
    return self.dialog.Restore(pluginid=const.PLUGIN_ID, secret=sec_ref)

class RedshiftLightListerTag(c4d.plugins.TagData):

    def Init(self, node):
        bc = c4d.BaseContainer()
        bc[0] = False

        node[const.PLUGIN_ID_TAG] = bc
        return True

    def CopyTo(self, dest, snode, dnode, flags, trn):
        bc = c4d.BaseContainer()
        bc[0] = False

        dnode[const.PLUGIN_ID_TAG] = bc
        return True


if __name__ == "__main__":
    dir, file = os.path.split(__file__)
    bmp = c4d.bitmaps.BaseBitmap()
    bmp.InitWith(os.path.join(dir, "easyLightLister.png"))
    c4d.plugins.RegisterCommandPlugin(  id=const.PLUGIN_ID,
                                        str="Redshift Light Lister",
                                        help="List all redshift lights in the scenes",
                                        info=0,
                                        dat=UILauncher_Main(), 
                                        icon=bmp)

    c4d.plugins.RegisterTagPlugin(id=const.PLUGIN_ID_TAG,
                                  str="TrsLightLister",
                                  g=RedshiftLightListerTag,
                                  description="TrsLightLister",
                                  icon=None,
                                  info=c4d.PLUGINFLAG_HIDE
                                  )