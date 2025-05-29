from colorama import Fore, Style, init
init(autoreset=True)

print(Fore.CYAN + """
 __  __ _    _ ______ _   _ 
|  \/  | |  | |  ____| \ | |
| \  / | |  | | |__  |  \| |
| |\/| | |  | |  __| | . ` |
| |  | | |__| | |____| |\  |
|_|  |_|\____/|______|_| \_|

      ðŸ˜ˆ Mueen Cloning ðŸ˜ˆ
""" + Style.RESET_ALL)

print(Fore.GREEN + "Welcome to your personalized tool, Mueen!\n")


import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
import os
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    from MHB64 import main
    main()
elif bit == '32bit':
    from MHB32 import main
    main()
else:
    print('\n YOUR DEVICE IS NOT SUPPORT THIS TOOL')
    os.system('exit')
