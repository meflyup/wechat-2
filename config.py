#coding=utf8

TOKEN = 'blacksheep'
APP_ID = 'wxcfd673e0cc02bfbd'
SECRET_KEY = '53d294ff8ab096a05f70aa02982edadd'
TULING_KEY = '0ecb5d6bca4d41fba0724bb04409cf4d'
ADMIN_OAUTH = 'admin_oauth'
WELCOME_WORD = u'''\
欢迎关注我的微信号！
点击右上角的小人，查看历史消息
回复下列内容获取对应信息：
目录： 获取文章目录的网址
帮助： 获取本信息
其他： 图灵机器人会陪你聊天'''
INDEX_URL = 'https://lonelyblacksheep.herokuapp.com//articles_list'
REPLY_DICT = {
    u'目录': '点这里-> ' + INDEX_URL,
    u'帮助': WELCOME_WORD,
    u'美女': 'http://image.baidu.com/search/wiseala?tn=wiseala&ie=utf8&word=%E7%BE%8E%E5%A5%B3&needpersonalized=0&haspersonalized=0&fr=alawise&pos=1&stdstl=2&tp=weaken'
}
MENU = {}
ARTICLES_DIR = 'articles'
ARTICLES_NAME = 'articles.json'
BASE_URL = 'https://api.weixin.qq.com/cgi-bin'
