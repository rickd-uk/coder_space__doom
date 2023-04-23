
class WADReader:
    def __init__(self, wad_path):
        self.wad_file = open(wad_path, 'rb')

    def close(self):
        self.wad_file.close()
