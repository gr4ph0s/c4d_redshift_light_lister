import c4d

from ..Const import Const
from .ConfigManagerRedshift import ConfigManagerRedshift

const = Const()

class ConfigManager(c4d.gui.GeDialog, ConfigManagerRedshift):
    def __init__(self):
        self.jsonContent = self.loadJsonFile()
        self.redshiftConfig = self.jsonContent["redshift"]
        self.dataChanged = False

    def refresh(self):
        self.jsonContent = self.loadJsonFile()
        self.redshiftConfig = self.jsonContent["redshift"]
        self.dataChanged = False

    def Command(self, id, msg):
        if id == const.UI_OPTION_END_OK:
            self.generateRedshiftjson(self)
            self.jsonContent = self.saveJsonFile(self.jsonContent)
            self.dataChanged = True
            self.Close()

        if id == const.UI_OPTION_END_CANCEL:
            self.Close()

        return True

    def CreateLayout(self):
        #Redshift
        self.SetTitle('Config')
        if self.GroupBegin(const.GRP_TAB_REDSHIFT_GRP, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 1, 500, "Redshift", inith=200):
            if self.ScrollGroupBegin(const.GRP_TAB_REDSHIFT_SCROLL_OPT, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, c4d.SCROLLGROUP_VERT, 0, 0):
                if self.GroupBegin(const.GRP_OPT_TAB_REDSHIFT, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 1, 500, "Redshift"):
                    self.createRedshiftCheckBox(self)
                self.GroupEnd()
            self.GroupEnd()
        self.GroupEnd()

        if self.GroupBegin(const.LIGHT_LISTER_REDSHIFT_OPTIONS_START, c4d.BFH_CENTER | c4d.BFV_CENTER, 100, 100):
            self.GroupBorderSpace(30, 5, 0, 2)

            self.AddButton(const.UI_OPTION_END_OK, c4d.BFH_CENTER | c4d.BFV_TOP, 0, 20, "Ok ")
            self.AddButton(const.UI_OPTION_END_CANCEL, c4d.BFH_CENTER | c4d.BFV_TOP, 0, 20, "Cancel")

        self.GroupEnd()

        return True
