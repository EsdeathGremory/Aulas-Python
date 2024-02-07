class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print('\033[48;5;196m' + ' ' * 50 + '\033[0m')
print(bcolors.OKBLUE + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
print('\033[48;5;196m' + ' ' * 50 + '\033[0m')
print('\033[94;41m' + "Text with blue foreground and yellow background" + '\033[0m')


