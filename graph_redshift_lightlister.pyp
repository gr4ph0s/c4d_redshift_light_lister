# coding: utf8
import os
import c4d

# localimport-v1.5_b64_lw=99
if bool(1):
    exec("""import base64 as b, zlib as z; s={}; blob=b"\
    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";exec(z.decompress(b.b64decode(blob)), s);localimport=s["localimport"]; del blob, b, z, s;""")

with localimport('.') as importer:
    from src.Const import Const
    from src.Config.ConfigManager import ConfigManager
    from src.LightManager import LightManager
    from src.Creation.CreationRedshift import CreationRedshift
    from src.Interaction.InteractionRedshift import InteractionRedshift

const = Const()

class mainDialog(c4d.gui.GeDialog):
    def __init__(self):
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
        for i in xrange(len(save_scroll)):
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