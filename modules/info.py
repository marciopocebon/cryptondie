from termcolor import colored
from time import sleep

def banner():
    print(colored('''
                /(        )`
                \ \___   / |
                /- _  `-/  '
               (/\/ \ \   /\\
               / /   | `    \\
               O O   ) /    |
               `-^--'`<     '
              (_.)  _  )   /
               `.___/`    /
                 `-----' /
    <----.     __ / __   \\
    <----|====O)))==) \) /====
    <----'    `--' `.__,' \\
                 |        |
                  \       /
             ______( (_  / \______
           ,'  ,-----'   |        \\
           `--{__________)        \/

Author: zer0dx
Github: github.com/zer0dx
Blog:   https://zer0dx.github.io
''', "yellow"))

    sleep(3)

help_message = '''
    --key       key used to encrypt and decrypt files
    --dir       Home directory for the attack, default is /
    --encrypt   Encrypt all files
    --decrypt   Decrypt all files
    --verbose   Active verbose mode, default is False
    '''

def log(msg):
    info = colored("[+]INFO: ", "yellow")
    msg = colored(msg, "green")

    print("{0}{1}".format(info, msg))
