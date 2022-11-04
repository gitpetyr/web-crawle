import bs4
#from selenium import webdriver
#from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib.request
import requests
import chardet,time,_thread as thread
global l,u,weds
l=[]
#weds=webdriver.Chrome()
def htmlnt(url,keep):
	try:
		for i in l:
			if i==url:
				return 0
		if "javascript" in url:
			return 0
		if not("http" in url):
			return 0
		print(url)
		l.append(url)
		resp = urllib.request.urlopen(url)
		r=requests.get(url)
		h=resp.read()
		#weds.get(url)
		c = chardet.detect(h)
		h=h.decode(c["encoding"])
		#print(c)
		#print(h)
		'''
		p=""
		p=url[:]
		p=list(p)
		p=p[8:]
		pa=""
		for i in range(0,len(p)):
			if p[i]=='/':
				p[i]='.'
		for i in p:
			pa=pa+i
		open("/Users/petyr/Desktop/htmltree/"+pa,"w").write(h)
		'''
		#print("\n\n\n")

		d=r.text
		s=BeautifulSoup(d,"html.parser")
		for i in s.find_all('a'):
			#time.sleep(1)
			htmlnt(urljoin(url,i.get("href")),keep)

		#time.sleep(1)
	except :
		return 0

u=""#url
htmlnt(u,False)



