# RAII and lazy initialization
class FileHandler:
    _file = None
    def __init__(self, path, mode):
        self._path = path
        self._mode = mode

    def _init(self):
        self._file = open(self._path, self._mode)

    def __str__(self):
        return self.read(-1)

    def read(self, n=-1):
        if (self._file == None):
            self._init()
            print("FileHandler: file {} initialized".format(self._path))
        contents = self._file.read(n)
        self._file.seek(0)
        return contents

    def write(self, s):
        if (self._file == None):
            self._init()
            print("FileHandler: file {} initialized".format(self._path))
        return self._file.write(s)

    def __del__(self):
        self._file.close()

class ReadFileHandler(FileHandler):
    def __init__(self, path):
        super().__init__(path, 'r')

class WriteFileHandler(FileHandler):
    def __init__(self, path):
        super().__init__(path, 'w')

# Factories
class FileHandlerFactory:
    def create(cls):
        return FileHandler()

class ReadFileHandlerFactory(FileHandlerFactory):
    def create(path):
        return ReadFileHandler(path)

class WriteFileHandlerFactory(FileHandlerFactory):
    def create(path):
        return WriteFileHandler(path)

# Builder and singleton
class FileBuilder:
    _instance = None

    @classmethod
    def get(cls):
        if cls._instance == None:
            cls._instance = cls()
        return cls._instance #if cls._instance != None else cls()

    def setPath(self, path):
        self._path = path

    def setMode(self, mode):
        self._mode = mode

    def build(self):
        return FileHandler(self._path, self._mode)


input_path = './in.txt'
file = FileHandler(input_path, 'r')

print("File {} created".format(input_path))
print("Attempting to read file contents...")
print(file)
print("Attempting to read file contents...")
print(file)
del file

try:
    print(file.read())
except:
    print('File has been already closed!')

file = WriteFileHandlerFactory.create(input_path)
file.write('Howdy there! This file is overwritten.')

file = ReadFileHandlerFactory.create(input_path)
print(file)

file_builder = FileBuilder.get()
file_builder.setPath(input_path)
file_builder.setMode('r')
file = file_builder.build()
print(file)

