from os import listdir

# ERROR TYPES
FLAG_ERROR = "[LOG] FLAG ERROR -> "
EXTENSION_ERROR = "[LOG] FILE FORMAT ERROR: directory contains files with diferent extension"
FILE_OPEN_ERROR = "[LOG] [OPEN FILE] FILE COULD NOT BE OPENED"

class TPMAnalizer:
    def __init__(self, directory, flags, extension) -> None:
        self.directory : str = directory
        self.filesList : list[str]
        self.flags : list[str] = flags
        self.extension : str = extension

        self.current_flag_index = 0
        self.data : list[float] = []

        for x in self.flags:
            self.data.append(0)


    # Gets all files from directory and saves them in fileList array
    def get_all_files_from_directory(self) -> None:
        self.filesList = listdir(self.directory)

    # Sets input flags to flags array
    def set_flags(self, flags) -> None:
        self.flags = flags

    # Check if all files from directory have the desired extendsion
    def check_files_extension(self) -> str:
        for file in self.filesList:
            if file.find(self.extension) == -1:
                return EXTENSION_ERROR
            
        return "[LOG] [CHECK EXTENSION] SUCCESS"
    
    # Open all files and read data
    def analize_all_files(self) -> str:
        for file in self.filesList:
            output_log = self.analize_file(file)
            if output_log == FLAG_ERROR or output_log == FILE_OPEN_ERROR:
                return output_log

        return "[LOG] [ANALIZE ALL FILES] SUCCESS"

    # Open one file and read data
    def analize_file(self, fileName) -> str:
        try:
            # Open file
            fileRoute = self.directory + "/" + fileName
            file = open(fileRoute, 'r')
            
            # Read line and get flag
            txtline = file.readline()
            while txtline != '':
                line_flag = self.get_line_flag(txtline, self.current_flag_index)
                # Check if flag is correct
                if line_flag != self.flags[self.current_flag_index] and txtline != '':
                    file.close()
                    return FLAG_ERROR
                
                line_data = self.get_line_data(txtline, self.current_flag_index)
                self.add_data(float(line_data), self.current_flag_index)
                self.current_flag_index += 1
                txtline = file.readline()
  
            self.current_flag_index = 0          

            file.close()
            return "[LOG] [OPEN FILE] SUCCESS"
        
        except IOError:
            return FILE_OPEN_ERROR
        
        
    def get_line_flag(self, txtline:str, flagIndex):
        first_index = txtline.find(self.flags[flagIndex])
        return txtline[first_index:len(self.flags[flagIndex])+1]
    
    def get_line_data(self, txtline:str, flagIndex):
        return txtline[len(self.flags[flagIndex]) + 2:len(txtline)]
        
    def add_data(self, data:float, index:int) -> None:
        self.data[index] += data

    def debug_print_files(self):
        for file in self.filesList:
            print(file)