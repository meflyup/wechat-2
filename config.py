#coding=utf8

TOKEN = 'blacksheep'
APP_ID = 'wxcfd673e0cc02bfbd'
SECRET_KEY = '53d294ff8ab096a05f70aa02982edadd'
TULING_KEY = '0ecb5d6bca4d41fba0724bb04409cf4d'
ADMIN_OAUTH = 'admin_oauth'
WELCOME_WORD = u'''\
欢迎关注我的微信号！
回复下列内容获取对应信息：
目录： 获取文章目录的网址
帮助： 获取本信息
其他： 图灵机器人会陪你聊天'''
INDEX_URL = 'https://lonelyblacksheep.herokuapp.com//articles_list'
REPLY_DICT = {
    u'目录': '点这里-> ' + INDEX_URL,
    u'帮助': WELCOME_WORD,
    u'美女': 'image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=word=%C3%C0%C5%AE&ala=1&fr=ala&alatpl=cover&pos=0#z=0&pn=&ic=0&st=-1&face=0&s=0&lm=-1'
}
MENU = {}
ARTICLES_DIR = 'articles'
ARTICLES_NAME = 'articles.json'
BASE_URL = 'https://api.weixin.qq.com/cgi-bin'
