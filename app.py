#!/usr/bin/env python  
# encoding: utf-8  
""" 
@Created by Notepad++ in the school on 2018/3/2 - 15:37 
@Gnome: Live and learn! 
@Author: 葛绪涛 
@Nickname: wordGe
@Contact: 690815818@qq.com  QQ:690815818 
@Site: http:// higexutao.blog.163.com 
@File: app.py 
"""

from tornado import web, options, ioloop, httpserver


class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")

    def post(self, *args, **kwargs):
        # print(self.request.files)
        # 提取 index.html name是file的内容
        file = self.request.files.get('file')[0]
        # 这是读取index.html name是username的值快速读取
        # 使用到的是get_query_argument
        # username = self.get_query_argument("username", "wordGe")
        print(type(file))
        # print(username)
        # print(file)
        with open("test.png","wb") as f:
            f.write(file['body'])


# 设置模板路径(html)，静态文件路径(js,css)
settings = {
    'template_path': 'template',
    'static_path': 'static',
}
application = web.Application([
    (r"/", MainPageHandler),
], **settings)

if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()
