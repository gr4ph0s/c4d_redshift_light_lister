import json
import os
import tempfile
import c4d
import shutil

class JsonFunction(object):
    test_file = "config_redshift.test"
    config_file = "config_redshift.json"
    folder = "redshift_light_lister"

    def isWrittableFolder(self, path, temp=False):
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except:
                return False

        test_path = os.path.join(path, self.test_file)
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
        temp_dir = os.path.join(tempfile.gettempdir(), self.folder)

        if self.isWrittableFolder(plugin_path):
            return os.path.join(plugin_path, self.config_file)

        if self.isWrittableFolder(temp_dir, True):
            return os.path.join(temp_dir, self.config_file)

        c4d.gui.MessageDialog("Error don't have writting privilege")
        return None

    def loadJsonFile(self):
        config_path = self.get_path()
        buffer = None
        if not os.path.exists(config_path):
            shutil.copy(os.path.join(os.path.dirname(os.path.split(__file__)[0]), self.config_file), os.path.split(config_path)[0])


        with open(config_path) as json_data:
            buffer = json.load(json_data)
        return buffer

    def saveJsonFile(self, jsonContent):
        config_path = self.get_path()

        if not os.path.exists(config_path):
            shutil.copy(os.path.join(os.path.dirname(os.path.split(__file__)[0]), self.config_file), os.path.split(config_path)[0])

        with open(config_path, 'w') as f:
            f.write(json.dumps(jsonContent, ensure_ascii=False, indent=4))
        return self.loadJsonFile()