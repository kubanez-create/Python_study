import os
import tempfile

class File:

    
    def __init__(self, file_path):
        if os.path.exists(os.path.join(tempfile.gettempdir(), file_path)):
            print('we check first condition')
            self.file_path = file_path
        else:
            self.file_path = os.path.join(os.getcwd(), tempfile.gettempdir(), file_path)
            print('we executed second condition', file_path, type(file_path))

        
        



    def __enter__(self):
        return


    def __exit__(self):
        pass

    def __add__(self, obj):
        pass
