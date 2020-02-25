import threading
import services.modifiers.Extractor as extractor

class Extract(threading.Thread):
    def __init__(self, ressource_path,extract_loc, override):
        threading.Thread.__init__(self)

        self.comp_ressource_loc = ressource_path
        self.extract_loc = extract_loc
        self.override_policy = override

    def run(self):
        extractor.extract(self.comp_ressource_loc, self.extract_loc, self.override_policy)
