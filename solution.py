import os
import tempfile

class File:
    count = 0

    
    def __init__(self, file_path):
        self.name = file_path
        if os.path.exists(self.name):
            self.file_path = os.path.join(os.path.abspath(os.getcwd()), self.name)
        else:
            self.file_path = os.path.join(os.path.abspath(os.getcwd()), self.name)
            with open((self.name), 'w') as n:
                n.write('')

    def read(self):
        with open((self.name), 'r') as f:
            row = f.readlines()
        return ''.join(row)            
        
    def write(self, st):
        with open((self.name), 'w') as f:
            f.write(st)
        return int(len(st))

    def __add__(self, obj):
        new_path = self.file_path + tempfile.gettempdir()[2:]
        new_obj = File(os.path.split(new_path)[1])
        with open((new_obj.name), 'w') as d:
            d.writelines([self.read(), obj.read()])
        return new_obj

    def __iter__(self):
        return self
    
    def __next__(self):
        with open((self.name), 'r') as d:
            res = d.readlines()

        if self.count == len(res):
            self.count = 0
            raise StopIteration
            
        
        result = res[self.count]
        self.count += 1
        return result

    def __repr__(self):
        return '{}'.format(self.file_path)
