import json
import threading

import requests

payload = {
    'client_id' : 'bd6262cb04ed423d9ec4a2102f863d40',
    'client_secret' : 'e222d693767a4cd38d8fb09dfb0a52d5',
    'grant_type' : 'client_credentials'
} 

token = requests.post('https://api.richasy.cn/connect/token', data=payload)
token = token.json()

ver_type = token['token_type']
ver_token = token['access_token']
header = {
    'Authorization' : ver_type + ' ' + ver_token
}

def search_in_wm(name):
    url = 'https://api.richasy.cn/wfa/basic/pc/wm/' + name
    response = requests.get(url,headers=header)
    response = response.json()
    info = response['info']
    del info['tradingTax']
    return info

def vaild_print(name,ini_name):
    resul = search_in_wm(name)
    print('物品名称：'+ ini_name)
    print("理论售价："+ str(resul['advicePrice']))
    print("杜卡德金币："+ str(resul['ducats']))
    print("")

fil = open('D:\\Desk\\Coding\\Py\\Warframe_Relic\\json\\Dic.json','r',encoding='utf-8')
tab = json.loads(fil.read())
search_list = ['帕里斯 PRIME 弓弦', '月神 PRIME 枪机', '雷克斯 PRIME 蓝图','XP PRIME 蓝图']


for item in search_list:
    if item in tab:
        t = threading.Thread(target = vaild_print, args = (tab[item],item,))
        t.start()
    else:
        print('物品名称：'+ item)
        print('无结果')
        print("")
