#create by WaRRiouR RuLeX BoYz DeViiL 
import os
os.system('xdg-open https://www.facebook.com/profile.php?id=100088143402548')
print("\033[1;32m[•] Follow My Facebook Account\033[0m")
import hashlib
import os, sys, re, requests, bs4, time, random, json, string
from bs4 import BeautifulSoup
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null')
try:
    import bs4
except ImportError:
    print ('\n [×] Modul Bs4 Not installed!...\n')
    os.system('pip install bs4')
def convert(cok):
    __for = 'datr=' + cok['datr'] + ';' + ('sb=' + cok['sb']) + ';' + ('fr=' + cok['fr']) + ';' + ('c_user=' + cok['c_user']) + ';' + ('xs=' + cok['xs'])
    return __for
def inbox(session):
    time.sleep(1)
    ses = requests.Session()
    __ = str(time.time()).replace('.', '')[:13]
    data = ses.get(f"https://10minutemail.net/address.api.php?sessionid={session}&_={str(__)}").json()
    if len(data["mail_list"]) !=1:
        address = data["mail_list"][0]["subject"]
        session = address.replace('FB-', '').replace('is your Facebook confirmation code', '')
        return session
ugen = []
for xd in range(5000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['5','6','7','8','9','10','11','12'])
    if b in ['5', '6', '7', '8', '9']:
        z=random.choice(['0', '1'])
        bv=b+'.'+z+'.'+z
    else:
        bv=b
    B=['GT-', 'SM-']
    c=random.choice(B)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    application_version = str(random.randint(111,396))+'.0.0.'+str(random.randrange(10,49))+'.'+str(random.randint(111,396))
    V=str(random.randrange(11,99))
    uas=f'{aa} {bv}; {c}{d}{e}{f} Build/{d}{f}{V}{f}; wv) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uas)
logo4 = """\033[1;37m
\033[1;37m----------------------------------------------------------------
\033[1;37m[\033[1;32m=\033[1;37m] .o88b. d8888b. d88888b  .d8b.  d888888b d88888b 
\033[1;37m[\033[1;32m=\033[1;37m]d8P  Y8 88  `8D 88'     d8' `8b `~~88~~' 88'     
\033[1;37m[\033[1;32m=\033[1;37m]8P      88oobY' 88ooooo 88ooo88    88    88ooooo 
\033[1;37m[\033[1;32m=\033[1;37m]8b      88`8b   88~~~~~ 88~~~88    88    88~~~~~ 
\033[1;37m[\033[1;32m=\033[1;37m]Y8b  d8 88 `88. 88.     88   88    88    88.     
\033[1;37m[\033[1;32m=\033[1;37m] `Y88P' 88   YD Y88888P YP   YP    YP    Y88888P
\033[1;37m----------------------------------------------------------------
\033[1;37m[\033[1;32m=\033[1;37m] Creater : DeviiL
\033[1;37m[\033[1;32m=\033[1;37m] GitHub  : DeViiLXD
\033[1;37m[\033[1;32m=\033[1;37m] Number  : +917668337116
\033[1;37m[\033[1;32m=\033[1;37m] Tool    : Auto Create Fb
\x1b[0;97m----------------------------------------------------------------\033[0m"""

def password_check():
    password_url = "https://pastebin.com/raw/aNh7GgVF"
    correct_password = requests.get(password_url).text.strip()
    
    while True:
        input_password = input('[+] Enter Password :: ')

        if input_password != correct_password:
            print("Incorrect password.")
            print("Password wrong and contact Admin")
            input("Press Enter to open WhatsApp and contact admin...")
            admin_message = "Hello Devil Sir. I'm asking for the Auto create fb account tool password."
            os.system(f'am start -a android.intent.action.VIEW -d "https://wa.me/+917668337116?text={admin_message}"')
            os.system('clear')
            print(logo4)
        else:
            break

def approval():
    os.system('clear')

    try:
        uuid = hashlib.md5((str(os.geteuid()) + str(os.getlogin())).encode()).hexdigest()
    except AttributeError:  # os.geteuid() and os.getlogin() might not be available on all systems
        uuid = hashlib.md5(str(random.random()).encode()).hexdigest()
    
    id = '_'.join(uuid)

    try:
        httpCaht = requests.get('https://github.com/DEVILXWD/approval/blob/main/approval.txt').text.strip()
    except requests.RequestException as e:
        print(f"Error accessing approval file: {e}")
        sys.exit(1)

    if id in httpCaht:
        print('\033[1;92m Your Token is Successfully Approved')
        time.sleep(0.5)  # After approval, check the password
    else:
        eno = input(' [•] Your Name :: ') 
        print('----------------------------------------------------------------------')
        print(f' [•] Mr [{eno}] Your Token is not approved')
        print(f' [•] [{eno}] You Have to Take Approval first')
        print(' [•] Free users stay away ')
        print('----------------------------------------------------------------------')
        print(' [•] Tool Owner :: Mr. DeViiL')
        print(f' [•] [{eno}] Your Token is :: {id}')
        input(' [•] If You Want To Buy Then Press Enter')
        tks = f'Hello%20Devil%20!%20Please%20Approve%20My%20Token%20My%20token%20Is%20:{id}%20My%20Name%20is%20{eno}'
        os.system(f'am start https://wa.me/+917668337116?text={tks}')
        time.sleep(1)
        approval()

boy = ['Legend DeViiL', 'DeVil Here', 'Devil Don']
girl = ['Sajida Malik', 'Ayesha Khan', 'Nabeela Malik', 'Kinza Fatima', 'Arooj Khan', 'Muskan Khan', 'Ayesha Malik', 'Safina Malik', 'Nida Ali', 'Rimsha Ali', 'Aarushi Sharma', 'Aditi Patel', 'Ananya Singh', 'Anika Gupta', 'Anjali Verma', 'Anushka Mehta', 'Aradhya Kumar', 'Avni Joshi', 'Bhavna Kapoor', 'Chhavi Chauhan', 'Daksha Desai', 'Deepika Reddy', 'Diya Nair', 'Divya Iyer', 'Esha Malhotra', 'Gauri Das', 'Gayatri Sinha', 'Harini Saxena', 'Isha Thakur', 'Ishita Bhatt', 'Janvi Tiwari', 'Jhanvi Mishra', 'Juhi Rao', 'Kajal Bhatia', 'Kavya Agrawal', 'Khushi Kaur', 'Kriti Gill', 'Kritika Menon', 'Lavanya Pandey', 'Madhavi Yadav', 'Maithili Jha', 'Manvi Sharma', 'Meera Gupta', 'Mitali Singh', 'Naina Shah', 'Nandini Roy', 'Nidhi Sen', 'Nikita Chauhan', 'Palak Jain', 'Pallavi Batra', 'Pooja Ahuja', 'Prachi Kapoor', 'Preeti Sharma', 'Priya Singh', 'Priyanka Verma', 'Radhika Mehta', 'Rajni Nair', 'Rakhi Desai', 'Rashi Patel', 'Reema Sinha', 'Renuka Reddy', 'Rhea Iyer', 'Richa Thakur', 'Riddhi Bhatt', 'Rina Tiwari', 'Riya Mishra', 'Roshni Rao', 'Sakshi Bhatia', 'Saloni Agrawal', 'Sanjana Kaur', 'Sapna Gill', 'Sarika Menon', 'Seema Pandey', 'Shalini Yadav', 'Shambhavi Jha', 'Shanti Gupta', 'Sharmila Shah', 'Shikha Roy', 'Shilpa Sen', 'Shivani Chauhan', 'Shraddha Jain', 'Shruti Batra', 'Simran Ahuja', 'Smita Kapoor', 'Sneha Sharma', 'Sonia Singh', 'Sonika Verma', 'Soumya Mehta', 'Suhani Nair', 'Swati Desai', 'Tanvi Patel', 'Tanya Sinha', 'Trisha Reddy', 'Tulika Iyer', 'Urvashi Thakur', 'Vaani Bhatt', 'Vaishali Tiwari', 'Vandana Mishra', 'Vanya Rao', 'Vibha Bhatia', 'Vidhi Agrawal', 'Vidhya Kaur', 'Vinita Gill', 'Vishakha Menon', 'Yashasvi Pandey', 'Yashika Yadav', 'Yukti Jha', 'Zainab Gupta', 'Zoya Shah', 'Zara Roy', 'Fatima Noor', 'Mulli Hu', 'Aayesha Bigdel', 'Fatima Randi', 'Aayesha Chudgi', 'Bhagodi Fatima', 'Allah Lodi', 'Chikni Fatima', 'Halala Ayesha', 'Noor Nikammi', 'Usmani Khan', 'Asmina Hussen']
ok = []
cp = []
def menu():
    os.system('clear')
    approval()
    print (logo4)
    password_check()
    print (47*'-')
    print ('[1] Auto Create')
    print ('[2] Follow Owner Fb Account')
    print (47*'-')
    sel = input('Select Option : ')
    if sel in['1', '01']:
        create().start()
    elif sel in ['2', '02']:
        os.system("xdg-open https://www.facebook.com/profile.php?id=100088143402548")
        menu()
    elif sel in ['3', '03']:
        menu()
    else:
        print ('select valid option')
        time.sleep(3)
        menu()
class create:

    def __init__(self):
        self.loop = 0
        self.gender = []

    def start(self):
        os.system('clear')
        print (logo4)
        print ('[1] Create Accounts For Boy')
        print ('[2] Create Accounts For Girl')
        print (47*'-')
        gen = input('Select Option :')
        print (47*'-')
        if gen in ['1', '01']:
            self.gender.append('boy')
        elif gen in ['2', '02']:
            self.gender.append('girl')
        else:
            self.gender.append('boy')
        print ('Example 1000, 2000, 5000, 10000')
        lim = int(input('LIMIT : '))
        os.system('clear')
        print (logo4)
        agent = random.choice(ugen)
        headers = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,hi-IN;q=0.8,hi;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'dpr=1.5303868055343628; sb=NuKVZuuo6-PwW8W74sZwM0I9; datr=NuKVZqgLqhyV94RqORFO-TNM; ps_n=1; ps_l=1; m_pixel_ratio=1.5303868055343628; wd=470x958; fr=03MTsywSmSapAxZki..BmleI2..AAA.0.0.Bmlyi6.AWXWtoHzxeo',
    'dpr': '1.8000000715255737',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X688B"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; Infinix X688B Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.134 Mobile Safari/537.36 GoogleApp/15.27.37.28.arm64',
    'viewport-width': '980',
}
        headers1 = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,hi-IN;q=0.8,hi;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'dpr=1.5303868055343628; sb=NuKVZuuo6-PwW8W74sZwM0I9; datr=NuKVZqgLqhyV94RqORFO-TNM; ps_n=1; ps_l=1; m_pixel_ratio=1.5303868055343628; wd=470x958; fr=03MTsywSmSapAxZki..BmleI2..AAA.0.0.Bmlyi6.AWXWtoHzxeo',
    'dpr': '1.8000000715255737',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X688B"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; Infinix X688B Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.134 Mobile Safari/537.36 GoogleApp/15.27.37.28.arm64',
    'viewport-width': '980',
}
        OO = '\033[0;97m'
        for x in range(lim):
            self.loop += 1
            sys.stdout.write(f'\r{OO}[DEVIL-XD] {OO}{self.loop}/{str(lim)} OK: {len(ok)}{OO} = CP: {len(cp)}{OO} '),
            sys.stdout.flush()
            if 'boy' in self.gender:
                name = random.choice(boy).split(' ')
                sex = '2'
            elif 'girl' in self.gender:
                name = random.choice(girl).split(' ')
                sex = '1'
            try:
                ses = requests.Session()
                buildses = user = "".join(random.SystemRandom().choice("qwertyuiopasdfghjklzxcvbnm0987654321") for i in range(26))
                create = ses.get(f"https://10minutemail.net/address.api.php?new=1&sessionid={buildses}&_={int(datetime.now().timestamp() * 1000)}").json()
                mail = {"mail": create["permalink"]["mail"], "session": create["session_id"]}
                email = mail['mail']
                session = mail['session']
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
            passw = name[0]+name[1]+str(random.randint(111,999))
            try:
                self.ses = requests.Session()
                a = self.ses.get('https://m.facebook.com/reg?_fb_noscript', headers=headers)
                loger = re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1)
                ref = BeautifulSoup(a.text, 'html.parser').find('form', {'action': True, "id":"mobile-reg-form", "method":"post"})
                bl = ['lsd', 'jazoest', 'cpp', 'reg_instance', 'submission_request']
                bz = ['reg_impression_id', 'ns']
                self.data = {}
                for v in ref('input'):
                    if v.get('name') in bl:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({'helper': ''})
                for v in ref('input'):
                    if v.get('name') in bz:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({
                    "zero_header_af_client": "",
                    "app_id": "103",
                    "logger_id": re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1),
                    "field_names[0]": "firstname",
                    "firstname": name[0],
                    "lastname": name[1],
                    "field_names[1]": "birthday_wrapper",
                    "birthday_day": str(random.randint(1,28)),
                    "birthday_month": str(random.randint(1,12)),
                    "birthday_year": str(random.randint(1992,2004)),
                    "age_step_input": "",
                    "did_use_age": "",
                    "field_names[2]": "reg_email__",
                    "reg_email__": email,
                    "field_names[3]": "sex",
                    "sex": sex,
                    "preferred_pronoun": "",
                    "custom_gender": "",
                    "field_names[]": "reg_passwd__",
                    "reg_passwd__": passw,
                    "submit": "Sign Up",
                    "name_suggest_elig": "false",
                    "was_shown_name_suggestions": "false",
                    "did_use_suggested_name": "false",
                    "use_custom_gender": "",
                    "guid": "",
                    "pre_form_step": "",
                })
                gett = self.ses.post('https://m.facebook.com'+ref['action'], headers=headers1, data=self.data)
                getts = self.ses.get('https://m.facebook.com/login/save-device/?login_source=account_creation&logger_id='+loger+'&app_id=103', headers=headers1)
                data1 = {}
                data2 = {}
                data3 = {}
                cok = self.ses.cookies.get_dict()
                if 'checkpoint' in getts.url:
                    cp.append(email+passw)
                     
                    open('/sdcard/DEVIL-CP.txt','a').write(+cok['c_user']+'|'+passw+'\n')
                dbl = ['fb_dtsg', 'jazoest', 'flow', 'next', 'nux_source']
                for x in BeautifulSoup(getts.text, 'html.parser').find_all('form', {'method': 'post'}):
                    if '/login/device-based/update-nonce/' in str(x):
                        for v in x('input'):
                            if v.get('name') in dbl:
                                try:
                                    data1.update({v.get('name'):v.get('value')})
                                except:
                                    pass
                        data1.update({'submit': 'OK'})
                        po = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data1)
                        for x in BeautifulSoup(po.text, 'html.parser').find_all('form', {'method': 'post'}):
                            if 'confirmation_event_location=cliff' in str(x):
                                for v in x('input'):
                                    if v.get('name') in dbl:
                                        try:
                                            data2.update({v.get('name'):v.get('value')})
                                        except:
                                            pass
                                code = inbox(session)
                                data2.update({'c': code, 'submit': 'Confirm'})
                                rex = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data2)
                                if 'checkpoint' in rex.url:
                                    cok = self.ses.cookies.get_dict()
                                    cp.append(email+passw)
                                    
                                    open('/sdcard/Devil-CP.txt','a').write(+cok['c_user']+'|'+passw+'\n')
                                else:
                                    coki = (";").join([ "%s=%s" % (key, value) for key, value in self.ses.cookies.get_dict().items() ])
                                    cok = self.ses.cookies.get_dict()
                                    print(f"\n\r\033[1;32m[✓] Account Created Done ✅\n[√] ID :: {cok['c_user']}\n[√] Password :: {passw}\n[√] Cookie :: {coki}\033[0;97m     ")
                                    open('/sdcard/DVIL-COOKIE.txt','a').write(+cok['c_user']+'|'+passw+ ' | ' +coki+'\n')
                                    open('/sdcard/DEVIL-OK.txt','a').write(+cok['c_user']+'|'+passw+'\n')
                                    ok.append(email+passw)
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
        print ('Process Has Been Completed')
        print (47*'-')
        print ('\033[1;32mTotal Ids > ok/' +str(len(ok)) + ' Cp/' + str(len(cp)))
        print (47*'-')
        input('back')
        menu()
menu()