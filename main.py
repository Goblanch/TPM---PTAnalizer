from TPMPTAnalyzer import TPMAnalyzer
from colorama import Fore
import PTAConfigfile

def main():

    flags = PTAConfigfile.flags
    file_extension = PTAConfigfile.file_extension
    files_directory = PTAConfigfile.files_directory
    output_dir = PTAConfigfile.output_dir

    analyzer = TPMAnalyzer(files_directory, output_dir, flags, file_extension)

    analyzer.get_all_files_from_directory()
    actionLog : str = analyzer.check_files_extension()
    print(Fore.RED + actionLog)
    actionLog = analyzer.analyze_all_files()
    print(Fore.RED + actionLog)

if __name__ == '__main__':
    main()