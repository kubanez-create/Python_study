import os
import tempfile

class File:
    count = 0

    
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
        with open(os.path.join(self.file_path, (self.name + '.txt')), 'w') as f:
            f.write(st)
        return int(len(st))

    def __add__(self, obj):
        new_path = self.file_path + tempfile.gettempdir()[2:]
        new_obj = File(new_path)
        with open(os.path.join(new_obj.file_path, (new_obj.name + '.txt')), 'w') as d:
            d.writelines([self.read(), obj.read()])
        return new_obj

    def __iter__(self):
        return self
    
    def __next__(self):
        with open(os.path.join(self.file_path, (self.name + '.txt')), 'r') as d:
            res = d.readlines()

        if self.count >= len(res):
            raise StopIteration
        
        result = res[self.count]
        self.count += 1
        return result

    def __str__(self):
        return '{}'.format(self.file_path)
