import requests
import re

target_url = "http://www.hqwallpapers.ru/nature/sklon/"
res = requests.get(target_url)


urls = re.findall(r'<img\s+.*?src="(.*?)".*?>', res.text)
print(urls)

for i, url in enumerate(urls):


        if url[:2] == '//':
            res = requests.get('http:' + str(url.split("?")[0]))
            print('http:' + str(url.split("?")[0]))
        else:
            res = requests.get(target_url[:-1] + str(url.split("?")[0]))
            print(target_url[:-1] + str(url.split("?")[0]))
        ext = url.split('.')[-1]

        if len(ext) > 3:
            ext = ""
        if len(res.content) > 500 and str(res.content).find(('html')) == -1:
            f = open('C:\\Users\\Юрий\\PycharmProjects\\1labaKMZI\\photo\\file_%s.%s' % (i, ext), 'wb')
            f.write(res.content)
            f.close()

