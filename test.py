#ref: http://docs.python-requests.org/en/master/user/advanced/#header-ordering
import requests


#################################
# download file from web.cmgsh.tp.edu.tw
# para:
# url: base url, would be "http://web.cmgsh.tp.edu.tw/news/u_news_v2.asp" 
# id: catagory id like:{DDE74934-8EF8-4DDA-9E7E-550EA3C62484}
# newsid: 10005
#
def dlFile(url,id,newsid):
	#url post 的網址
	url2 = "http://web.cmgsh.tp.edu.tw/ylbin/filedown.asp?filename=filename1"

	#http request 我成功了！需要加上referer 還有cookie
	payload = { 'id' : id, 'newsid' : newsid }
	
	r = requests.get(url, params=payload)
	#print(r.url)
	print(r.html)
	head = r.headers['set-cookie']
	
	header = {'cookie': head, 'referer':r.url,}
	#抓檔案
#	r2 = requests.get(url2, headers=header, stream=True)
#	if(r2.headers['Content-Length'] != '304'):
#		print (r2.url)
#		#print (r2.headers)
#		return True
#	else:
#		return False
#	#with open('tt.pdf', 'wb') as f:
#		#f.write(r2.content)


##################################
# main 
#
base = "http://web.cmgsh.tp.edu.tw/news/u_news_v2.asp"
id = "{DDE74934-8EF8-4DDA-9E7E-550EA3C62484}"
#newsid = input()
# 最新公告{DDE74934-8EF8-4DDA-9E7E-550EA3C62484}
#dlFile(base,id,newsid)
counter=0
for i in range(1,10000):
	print(i)
	if(dlFile(base,id,i)):
		counter+=1
#		print(counter)

#print(counter)
# asdrfasdfasdfa 
