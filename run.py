import os
os.system('clear')
print("""\33[33m█ █▄░█ █▀ █▀█ █▀▀ █▀▀ ▀█▀ █▀█ █▀█
█ █░▀█ ▄█ █▀▀ ██▄ █▄▄ ░█░ █▄█ █▀▄""")
print("___________________________________________________")
print("         \33[35m TOOL CREATED BY CEO xRO & Pappu")
print("          CEO AND TERMUX ACADEMY")
print("__________________________________________________")
import requests
link=input("Enter Site Link>>")
print()
print("[1]Inspect Website\n[2]Download Image Code\n[3]Check Status Code\n[4]Get site details\n[5]Check Json Data")
choice=input('Enter your Choice>>')
if choice=="1":
	try:
		r=requests.get(link)
		print(r.text)
	except:
		print("Sorry,An Error occured")
if choice=="2":
		try:
			r=requests.get(link)
			with open('file.png','wb') as f:
				f.write(r.content)
		except:
			print("Sorry, unsupported url")
if choice =="3":
			r=requests.get(link)
			print(r.status_code)
if choice=="4":
			try:
				r=requests.get(link)
				print(r.headers)
			except:
				print("Sorry, request denied")
print()
print(".......Thanks For Using......")
			
