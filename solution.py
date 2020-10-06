import os
import tempfile

class File:

    
    def __init__(self, file_path):
        self.name = file_path
        if os.path.exists(os.path.join(os.path.abspath(os.getcwd()), self.name)):
            print('we check first condition')
            self.file_path = os.path.join(os.path.abspath(os.getcwd()), self.name)
        else:
            self.file_path = os.path.join(os.path.abspath(os.getcwd()), self.name)
            os.makedirs(self.file_path)
            with open(os.path.join(self.file_path, (self.name + '.txt')), 'w') as n:
                n.write('')
            print('we executed second condition', self.file_path,
            os.path.exists(file_path))

    def read(self):
        with open(os.path.join(self.file_path, (self.name + '.txt')), 'r') as f:
            print(f.readline())            
        
    def write(self):
        with open(self.file_path, 'w') as f:
            f.write()


    def __enter__(self):
        return


    def __exit__(self):
        pass

    def __add__(self, obj):
        pass

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        result = self.current ** 2
        self.current += 1
        return result

    def __str__(self):
        return '{} <{}>'.format(self.name, self.email)
