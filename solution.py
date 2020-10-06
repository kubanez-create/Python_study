import os
import tempfile

class File:

    
    def __init__(self, file_path):
        self.name = file_path
        if os.path.exists(os.path.join(os.path.abspath(os.getcwd()), self.name)):
            self.file_path = os.path.join(os.path.abspath(os.getcwd()), self.name)
        else:
            self.file_path = os.path.join(os.path.abspath(os.getcwd()), self.name)
            os.makedirs(self.file_path)
            with open(os.path.join(self.file_path, (self.name + '.txt')), 'w') as n:
                n.write('')

    def read(self):
        with open(os.path.join(self.file_path, (self.name + '.txt')), 'r') as f:
            row = f.readline()
        return row            
        
    def write(self, st):
        with open(os.path.join(self.file_path, (self.name + '.txt')), 'a') as f:
            f.write(st)

    def __add__(self, obj):
        new_path = os.path.join(self.file_path, tempfile.gettempdir())
        return File(new_path)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        result = self.current ** 2
        self.current += 1
        return result

    def __str__(self):
        return '{}'.format(self.file_path)
