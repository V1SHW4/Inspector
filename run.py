import requests
import os
os.system('clear')
print("""\33[33m▀█▀ █▀▀▄ █▀▀ █▀▀█ █▀▀ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ 
░█─ █──█ ▀▀█ █──█ █▀▀ █── ──█── █──█ █▄▄▀ 
▄█▄ ▀──▀ ▀▀▀ █▀▀▀ ▀▀▀ ▀▀▀ ──▀── ▀▀▀▀ ▀─▀▀""")
print("___________________________________________________")
print("         \33[35m TOOL CREATED BY CEO xRO & Pappu")
print("          CEO AND TERMUX ACADEMY")
print("          Powered by THE F SOCIETY")
print("          Special Thanks to Kavidu Sri(spy)")
print("__________________________________________________")
link=input("Enter Site Link>>")
print()
print("[1]Inspect Website\n[2]Download Image Code\n[3]Check Status Code\n[4]Get site details\n[5]Cookie Tracker\n[6]Check Available Requests\n[7]Full details about data\n[8]Check Encoding")
choice=input(  "Enter your Choice>>" )
if choice=="1":
	try:
		r=requests.get(link)
		print(r.text)
	except:
		print("Sorry,An Error occured")
if choice=="2":
		try:
			r=requests.get(link)
			with open( file.png , wb ) as f:
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
if choice== 5 :
	try:
		cookie_tracker={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; U; nl; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01"}
		xro=requests.get(link,headers=cookie_tracker)
		print(xro.cookies)
	except:
		print("Sorry,cannot receive information..")
if  choice=="6":
	try:
		r=requests.get(link)
		print(dir(r))
	except:
		print("Sorry,an error occured")
if choice=="7":
	try:
		r=requests.get(link)
		print(help(r))
	except:
		print("Sorry,no info received")
if choice=="8":
	try:
		r=requests.get(link)
		print(r.encoding)
	except:
		print("Permission Denied")
print()
print(".......Thanks For Using......")
