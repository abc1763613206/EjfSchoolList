import time
import requests
import json

headers={'User-Agent':'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36 MMWEBID/9938 MicroMessenger/7.0.3.1400(0x27000334) Process/tools NetType/WIFI Language/zh_CN' , 'X-Requested-With': 'com.tencent.mm'}

CityCodes={'0531','0533','0534','0535','0536','0537','0538','0539','0543','0546','0631','0632','0633','0634','0635','0636'}  
#Shandong Only?

url='http://www.ejf365.com/ESCHOOLWEB/neweschool/front/getSchoolList'


for Code in CityCodes:
	data={'selectCityCode':str(Code),'schoolType':''}
	print('Getting '+str(Code)+' ')
	response = requests.post(url=url,data=data,headers=headers)
	print(response.status_code)
	print(' \n')
	with open('./City/'+str(Code)+'.json', 'w') as f:
		f.write(response.text)
	time.sleep(1)
