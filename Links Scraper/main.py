#python -m pip install bs4 --user
#python -m pip install requests --user
#python -m pip install lxml --user

import requests
from bs4 import BeautifulSoup

def main():
	url = input("Enter URL to SCRAPE:").strip()
	try:
		f = open("Data.txt", "w")
	except IOError as e:
		print(f"FAILED to open file.\nERROR:{e}")
	else:
		req = requests.get(url)
		soup = BeautifulSoup(req.content, 'lxml')
		aTags = soup.find_all("a")
		for a in aTags:
			href = a["href"]
			if href[0:4] == 'http':
				f.write(href.strip()+'\n'+50*'-'+'\n')
			elif href[0] == '/':
				f.write(url + href.strip()+'\n'+50*'-'+'\n')
		f.close()

if __name__ == "__main__":
	main()