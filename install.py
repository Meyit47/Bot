import sys, time, os


def m(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

os.system("clear")
print("""
      ██████╗░░█████╗░██████╗░██╗░░██╗
      ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
      ██║░░██║███████║██████╔╝█████═╝░
      ██║░░██║██╔══██║██╔══██╗██╔═██╗░
      ██████╔╝██║░░██║██║░░██║██║░╚██╗
      ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝

      ██████╗░░█████╗░████████╗
      ██╔══██╗██╔══██╗╚══██╔══╝
      ██████╦╝██║░░██║░░░██║░░░
      ██╔══██╗██║░░██║░░░██║░░░
      ██████╦╝╚█████╔╝░░░██║░░░
      ╚═════╝░░╚════╝░░░░╚═╝░░░
      ░ ░\x1b[00m\033[041m TERMUX TELEGRAM BOT MEYİT \033[00m\x1b[1;00m░░
        ░ ░   ░   ░    ░ ░   ░    ░   ░   ░\x1b[00m
""")
m('\x1b[00m\033[041m Malzemeleri otomatik olarak yükleyin  \033[00m')
m('\x1b[00m\033[041m Kurulumu tamamlamadan Termux'tan çıkmayın!!  \033[00m')
os.system("pkg update -y")
os.system("pkg upgrade -y")
os.system("pkg install nano")
os.system("pkg install python -y")
os.system("pkg install python2 -y")
os.system("pkg install nodejs -y")
os.system("pkg install libwebp -y")
os.system("pkg install ffmpeg -y")
os.system("npm install")
os.system("npm audit fix")
os.system("npm install axios")
os.system("npm install telegram@3.32")
m('\x1b[00m\033[041m Telegram Botunu Başlatmak...  \033[00m')
os.system("clear")
os.system("python start.py")
m("DONE")
