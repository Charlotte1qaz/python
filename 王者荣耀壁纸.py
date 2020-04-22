import requests
import json
import time

start_time = time.time()


base_url = 'https://pvp.qq.com/web201605/js/herolist.json'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
response = requests.get(base_url,headers=headers)
data_str = response.text
#print(data_str)

#3.1转换数据类型
data_list = json.loads(data_str)    # --列表
#print(data_list)
#3.2解析数据

for data in data_list:
    #print(data)
    #提取图片所要得参数
    ename = data['ename']  #英雄编号
    cname = data['cname']  #英雄的名字
    try:
        skin_name = data['skin_name'].split('|')  #英雄的皮肤数量,切割皮肤的名字，计算出有多少皮肤
        #print(ename,cname,skin_name)
    except Exception as e:
        print(e)

    # http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/107/107-bigskin-7.jpg
    # http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/+英雄的编号+'/'+ 英雄的编号 + '-bigskin-' + '7' + '.jpg'

    for skin_num in range(1,len(skin_name) + 1):
        skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+ str(ename)+'/'+ str(ename) + '-bigskin-' + str(skin_num) + '.jpg'
        #print(skin_url)

        skin_data = requests.get(skin_url,headers=headers).content     #发送图片数据请求

        with open('picture\\' + cname + "-" + skin_name[skin_num - 1] + '.jpg', 'wb') as f:
            print('正在下载图片：', cname + "-" + skin_name[skin_num - 1])
            f.write(skin_data)


end_time = time.time()
all_time = end_time - start_time
print('共花费时间：',all_time,"秒")