import json
import urllib.request
from termcolor import colored

print(colored('''                                                                                                                                                                                                                                                                                                                              
 _ # ______  # _ # _______ # _______ # _______ # _______ # _______ #
| |#(_____ \ #| |#(_______)#(_______)#(_______)#(_______)#(_______)#
| |# _____) )#| |# _     _ # _____   # _     _ # _   ___ # _______ #
| |#|  ____/ #| |#| |   | |#|  ___)  #| |   | |#| | (_  |#|  ___  |#
| |#| |      #| |#| |   | |#| |      #| |___| |#| |___) |#| |   | |#
|_|#|_|      #|_|#|_|   |_|#|_|      # \_____/ # \_____/ #|_|   |_|#
   ##         ##   ##         ##         ##         ##         ##         ## 
\n''', "green"))

print(colored("Coded BY Maari-Krish \n", "green"))
print("\n")
print(colored("[+] Ip Information...","red"))
ip = input(colored("Enter the ip address of the target: ", "magenta"))
print("Ipinfoga results for",ip)
api = "https://ipapi.co/"+ip+"/json/"
response = urllib.request.urlopen(api)
data = response.read()
value = json.loads(data)

print("\n")
print(colored("---------------------------------------------------------------------------------------------------------------", "green"))
print(colored("Ip address: " + value['ip'], "blue"))
print(colored("Version of IP: " + value['version'], "blue"))
print(colored("City: " + value['city'], "blue"))
print(colored("Region: " + value['region'], "blue"))
print(colored("Region Code: " + value['region_code'], "blue"))
print(colored("Country: " + value['country'], "blue"))
print(colored("Country Name: " + value['country_name'], "blue"))
print(colored("Country Code: " + value['country_code'], "blue"))
print(colored("Country Code ISO : " + value['country_code_iso3'], "blue"))
print(colored("Country Capital : " + value['country_capital'], "blue"))
print(colored("Continent : " + value['continent_code'], "blue"))
print(colored("Postal Code : " + value['postal'], "blue"))
print(colored("Timezone: " + value['timezone'], "blue"))
print(colored("Country Calling Code : " + value['country_calling_code'], "blue"))
print(colored("Currency : " + value['currency'], "blue"))
print(colored("Currency_name : " + value['currency_name'], "blue"))
print(colored("Languages : " + value['languages'], "blue"))
print(colored("ASN : " + value['asn'], "blue"))
print(colored("Org: " + value['org'], "blue"))
print(colored("---------------------------------------------------------------------------------------------------------------", "green"))
