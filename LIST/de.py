#Jangan ganti author , hargai creator cape loh buat nya

import requests,os,re

b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"
cyan = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



def german():
    global page
    res = requests.get('https://www.insecam.org/en/bycountry/DE/', headers=headers)
    findpage = re.findall('"?page=",\s\d+', res.text)[1]
    rfindpage = findpage.replace('page=", ', '')
    os.system('clear')
    print("{}        ____ ").format(r)
    print("   _[]_/____\__n_ ")
    print("  |_____.--.__()_|")
    print("  |TAM //# \\\ TAM|")
    print("{}  |FA  \\\__//  FA| ").format(w)
    print("  |NX   '--'   NX| ")
    print("{}  '--------------'----------{}------------------.  ").format(r,w)
    print("{}  | {}Author  : {}MrTamfanX {}   | {}INDO{}N{}{}ESIA     | ").format(r,w,r,w,r,ir,reset,w)
    print("{}  | {}Youtube : {}MrUncle.     {}| {}+62-857-7951-5200 {}|").format(r,w,w,w,lgray,w)
    print("{}  '------------------------------------{}-------'  ").format(r,w)
    print("{}       [ {}List page : {} {}]").format(r,w,rfindpage,r)
    run()
    
def run():
    try:
        page = input("\033[1;31m       [ \033[1;37mPage \033[1;31m]\033[1;37m> ")
        url = ("https://www.insecam.org/en/bycountry/DE/?page="+str(page))
        print ""
        res = requests.get(url, headers=headers)
        findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
        count = 1
        for _ in findip:
             hasil = findip[count]
             print ("{}[ {}{} {}]").format(r,w,hasil,r)
             count += 1
    except:
        print ""
        print r+"Terimakasih Buat Lu Semua Ngentod..."+w
