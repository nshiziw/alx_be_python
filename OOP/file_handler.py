class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')     #open the file for reading

    def read_data(self):
        return self.file.read()
    
    def __del__(self):
        self.file.close()   #close the file when the object is destroyed

# create an object for fileHandler
file_obj = FileHandler('sample.txt')
print(file_obj.read_data())

# Object is no longer needed, it will be garbage collected, and __del__ method will be called automatically to close the file