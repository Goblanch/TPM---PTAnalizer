from TPMPTAnalizer import TPMAnalizer
from colorama import Fore

def main():

    flags = ['PlayTime', 'hola']
    analizer = TPMAnalizer("C:/Users/gonza/OneDrive/Escritorio/TestResults", flags, ".txt")
    analizer.get_all_files_from_directory()
    analizer.set_flags(flags)
    #analizer.DebugPrintFiles()
    actionLog : str = analizer.check_files_extension()
    print(Fore.RED + actionLog)
    actionLog = analizer.analize_all_files()
    print(Fore.RED + actionLog)
    # Reset terminal color
    print(Fore.WHITE)

if __name__ == '__main__':
    main()