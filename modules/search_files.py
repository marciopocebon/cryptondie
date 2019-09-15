import os
import os.path

class SearchDirThree():
    def __init__(self, init_directory):
        self.init_directory = init_directory
        self.list_directory = []

    '''    
    def search_all_directory(self):
        current_directory = os.listdir(self.init_directory)
        for directory in current_directory:
            if os.path.isdir(os.path.join(self.init_directory, directory)):
                self.list_directory.append(directory)
    '''
    
    def search_all_files(self):
        all_files = []

        #search all files in directory three
        for root, directorys, files in os.walk(self.init_directory):
            for file in files:
                all_files.append(os.path.join(root, file))

        return all_files
