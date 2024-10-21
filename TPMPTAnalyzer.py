from os import listdir

# ERROR TYPES
FLAG_ERROR = "[LOG] FLAG ERROR -> "
EXTENSION_ERROR = "[LOG] FILE FORMAT ERROR: directory contains files with different extension"
FILE_OPEN_ERROR = "[LOG] [OPEN FILE] FILE COULD NOT BE OPENED"
ZERO_ERROR = "[LOG] [COMPUTE DATA] ZERO DIVISION ERROR"

class TPMAnalyzer:
    def __init__(self, directory, flags, extension) -> None:
        self.directory: str = directory
        self.filesList: list[str] = []
        self.flags: list[str] = flags
        self.extension: str = extension

        self.current_flag_index = 0
        self.data: list[float] = []
        self.data_counters: list[int] = []
        self.data_result: list[float] = []

        self.initialize_data()


    def initialize_data(self) -> None:
        for x in self.flags:
            self.data.append(0)
            self.data_counters.append(0)
            self.data_result.append(0)

    # Gets all files from directory and saves them in fileList array
    def get_all_files_from_directory(self) -> None:
        self.filesList = listdir(self.directory)

    # Sets input flags to flags array
    def set_flags(self, flags) -> None:
        self.flags = flags

    # Check if all files from directory have the desired extension
    def check_files_extension(self) -> str:
        for file in self.filesList:
            if file.find(self.extension) == -1:
                return EXTENSION_ERROR
            
        return "[LOG] [CHECK EXTENSION] SUCCESS"
    
    # Open all files and read data
    def analyze_all_files(self) -> str:
        for file in self.filesList:
            output_log = self.__analyze_file(file)
            if output_log == FLAG_ERROR or output_log == FILE_OPEN_ERROR:
                return output_log

        self.__compute_data()
        self.__generate_output_file()

        return "[LOG] [ANALYZE ALL FILES] SUCCESS"

    # Open one file and read data
    def __analyze_file(self, file_name) -> str:
        try:
            # Open file
            file_route = self.directory + "/" + file_name
            file = open(file_route, 'r')
            
            # Read line and get flag
            txt_line = file.readline()
            while txt_line != '':
                line_flag = self.__get_line_flag(txt_line, self.current_flag_index)
                line_data = self.__get_line_data(txt_line, self.current_flag_index)
                self.__add_data(float(line_data), self.current_flag_index)
                self.current_flag_index += 1

                txt_line = file.readline()

            self.current_flag_index = 0          

            file.close()
            return "[LOG] [OPEN FILE] SUCCESS"
        
        except IOError:
            return FILE_OPEN_ERROR


    def __compute_data(self) -> str:
        for i in range(len(self.flags)):
            try:
                self.data_result[i] = self.data[i] / self.data_counters[i]
            except ZeroDivisionError:
                return ZERO_ERROR

        return "[LOG] [COMPUTE DATA] SUCCESS"

    def __generate_output_file(self) -> None:
        file = open("/Users/goblanch/Desktop/TypingMonke/UTILS/TPM-PTAnalizer/TPM---PTAnalizer/TestFiles/PTOutput.txt", 'w')
        content: str = ""
        for i in range(len(self.flags)):
            content = content + self.flags[i] + ": " + str(self.data_result[i]) + "\n"

        file.write(content)
        file.close()

    def __get_line_flag(self, txt_line: str, flag_index):
        first_index = txt_line.find(self.flags[flag_index])
        return txt_line[first_index:len(self.flags[flag_index]) + 1]
    
    def __get_line_data(self, txt_line: str, flag_index):
        return txt_line[len(self.flags[flag_index]) + 2:len(txt_line)]
        
    def __add_data(self, data: float, index: int) -> None:
        self.data[index] += data
        self.data_counters[index] += 1

    def debug_print_files(self):
        for file in self.filesList:
            print(file)
