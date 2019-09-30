# -*- coding:utf-8 -*-
import requests

if __name__ == '__main__':
    url = 'http://h.hiphotos.baidu.com/image/pic/item/37d3d539b6003af3057ef951382ac65c1038b63e.jpg'
    img = requests.get(url=url).content
    with open('pic.jpg','wb') as f:
        f.write(img)
        print('下载完成')

    print('')
    input('请按任意键退出...')