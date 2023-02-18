import requests
import argparse
import json
from colorama import Fore


def Lookup(target,all_result=False):

	sess = requests.Session()
	sess.headers.update({"User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3"})
	get = sess.get(f"http://ipwhois.app/json/{target}")		
	data = json.loads(get.text)


	if(all_result == False):
		if(data['success'] == True):
			
			return {
					"Ip":data['ip'],
					'IP type':data['type'],
					'Country':data['country'],
					'Country_code':data['country_code'],
					'Country_capital':data['country_capital'],
					'Region':data['region'],
					'City':data['city'],
					'Org':data['org'],
					'ISP':data['isp'],
					'Timezone':data['timezone'],
					'Latitude':data['latitude'],
					'Longitute':data['longitude'],
					'Google map': f"https://www.google.com/maps/place/{data['latitude']}+{data['longitude']}"
					}
		else:
			return {"Lookup failed":"Wrong url or ip address"}

	else:
		if(data["success"] == True):
			data.update({'Google map': f"https://www.google.com/maps/place/{data['latitude']}+{data['longitude']}"})
			return data
		else:
			return {"Lookup failed":"Wrong url or ip address"}			

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("target",help="Enter the url")
	parser.add_argument("-a","--all",help="show all details",action="store_true")

	args = parser.parse_args()

	if(args.target):
		
		if(args.all):
			lo = Lookup(args.target,True)
			print(Fore.RED+f"\tTarget : {args.target}")
			for k,v in lo.items():
				print(Fore.GREEN+k,Fore.WHITE+' : ',v)

		else:
			lo = Lookup(args.target,False)
			print(Fore.RED+f"\tTarget : {args.target}")
			for k,v in lo.items():
				print(Fore.GREEN+k,Fore.WHITE+' : ',v)


