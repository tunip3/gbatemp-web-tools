import requests
r = requests.get("http://gbatemp.net")
xfsession = r.cookies['xf_session']
#print xf session token
print("xf session token is " + xfsession)
#set username
username=input("please enter your username\n")
#set password
password=input("please enter your password\n")
#set header
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
#set params
params={"login":username, "register":"0", "password": password, "remember":"1", "cookie_check":"1", "redirect":"/", "_xfToken":""}
#set cookies
cookies=dict(xf_session=xfsession, xf_enable_cache="1", crfgL0cSt0r="true", _ga="GA1.2.14475462.1538667976", euconsent="BOVHhwYOVHhwYABABAENBr-AAAAhuAAA",  __gads="ID=c1f6b24dfa446214:T=1538668034:S=ALNI_MaajT5zz4ql5gHqHaQ8jqL-5GGpoQ", _gid="GA1.2.1501190998.1541186218", pwUID="70609193592479", _fbp="fb.1.1541260226375.1257057508", playwirePageViews="11", _gat_gtag_UA_2061983_1="1", )
#create session
g = requests.post('https://gbatemp.net/login/login', cookies=cookies, headers=headers, params=params)
####get cookes
if "xf_user" in g.cookies:
    #get xf_user
    print("xf_user token is "+g.cookies['xf_user'])
    #get xf_session token
    print("new xf_session token is "+g.cookies['xf_session'])
else:
    print("invalid login")
