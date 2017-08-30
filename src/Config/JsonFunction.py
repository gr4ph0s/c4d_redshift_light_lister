import json
import os
import tempfile
import c4d

class JsonFunction(object):
    def isWrittableFolder(self, path):
        if not os.path.exists(path):
            return False

        test_path = os.path.join(path, "config_rs.test")
        can_write = False

        try:
            with open(test_path, 'w') as f:
                f.write("test")
                can_write = True
            os.remove(test_path)
        except:
            can_write = False

        return can_write

    def get_path(self):
        plugin_path = os.path.dirname(os.path.split(__file__)[0])
        temp_dir = os.path.join(tempfile.gettempdir(), "redshift_light_lister")

        if self.isWrittableFolder(plugin_path):
            return os.path.join(plugin_path, "config_rs.json")

        if self.isWrittableFolder(temp_dir):
            return os.path.join(temp_dir, "config_rs.json")

        c4d.gui.Message("Error don't have writting privilege")
        return None

    def loadJsonFile(self):
        config_path = self.get_path()
        buffer = None
        with open(config_path) as json_data:
            buffer = json.load(json_data)
        return buffer

    def saveJsonFile(self, jsonContent):
        config_path = self.get_path()
        with open(config_path, 'w') as f:
            f.write(json.dumps(jsonContent, ensure_ascii=False, indent=4))
        return self.loadJsonFile()