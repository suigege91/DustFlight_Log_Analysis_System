import time

from tornado_mysql import pools
from tornado.gen import coroutine
from tornado.web import RequestHandler, authenticated, hashlib

templates_page_array = {
    'template_page_1': './index.html',
    'template_page_2': './home.html',
    'template_page_3': './data_require.html',
    'template_page_4': './display.html',
    'template_page_5': './console.html',
    'template_page_6': './login.html',
    'template_page_7': './regis.html',
}

pools.DEBUG = True
POOL = pools.Pool(dict(host='127.0.0.1', port=3306, user='root', passwd='1q2w3e4r!@#', db='DustFlight_LAS'),
                  max_idle_connections=2, max_recycle_sec=3)


class HomeHandler(RequestHandler):
    def get(self):
        self.render(templates_page_array['template_page_2'])


class ConsoleHandler(RequestHandler):
    def get(self):
        self.render(templates_page_array['template_page_5'])


class req(RequestHandler):
    def get_currnet_user(self):
        return self.get_secure_cookie('user_name')


class MainHandler(req):
    @authenticated
    async def get(self):
        user_name = self.current_user.decode('utf-8')
        self.render(
            templates_page_array['template_page_1'], user_name=user_name)

    async def post(self):
        return self.write('post')

    async def delete(self):
        return self.write('delete')


class UserLoginHandler(req):
    async def get(self):
        return self.render(templates_page_array['template_page_6'], title='User_Login_Form')

    @coroutine
    def post(self):
        user_name = self.get_argument('user_name')
        user_pass = self.get_argument('user_pass')
        auth_collection = user_name + user_pass
        after_after_encode_pass = hashlib.md5(
            auth_collection.encode()).hexdigest()
        cursor = yield POOL.execute('select password from user where name=(%s)', (user_name,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            current_password = result[0]
            if current_password == after_after_encode_pass:
                self.set_secure_cookie('user_name', user_name)
                print(self.current_user)
                return self.redirect('/index')
            else:
                return self.redirect('/login')
        else:
            return self.redirect('/login')


class UserLogoutHandler(req):
    async def get(self):
        logout = self.get_argument('logout', None)
        if logout == 'on':
            self.clear_cookie('user_name')
        return self.redirect('/index')


class UserRegisHandler(req):
    def get(self):
        return self.render(templates_page_array['template_page_7'])

    @coroutine
    def post(self):
        user_name = self.get_argument('user_name', None)
        user_pass = self.get_argument('user_pass', None)
        user_mail = self.get_argument('user_mail', None)
        user_tell = self.get_argument('user_tell', None)
        user_address = self.get_argument('user_address', None)
        auth_collection = user_name + user_pass
        after_encode_pass = hashlib.md5(auth_collection.encode()).hexdigest()
        cursor = yield POOL.execute(
            'INSERT INTO `user` (`id`, `name`, `password`, `email`, `tel`, `address`) VALUES (NULL, %s, %s, %s, %s, %s)',
            (user_name, after_encode_pass, user_mail, user_tell, user_address))
        cursor.close()
        return self.redirect('/login')


class DataRequireHandler(RequestHandler):
    def get(self):
        self.render(templates_page_array['template_page_3'])

    def post(self):
        title = self.get_argument('title', None)
        author = self.get_argument('author', None)
        content = self.get_argument('content', None)
        context = dict()
        if title and content:
            context['title'] = title
            context['author'] = author
            context['content'] = content
            context['date'] = time.time()
            print(context)
            query_collection = self.application.db.dustflight_las
            query_collection.insert(context)
            self.redirect(templates_page_array['template_page_4'])
        else:
            self.redirect(templates_page_array['template_page_3'])


class DisplayHandler(RequestHandler):
    def get(self):
        query_collection = self.application.db.dustflight_las
        result_data_array = query_collection.find_one()
        if result_data_array:
            self.render(templates_page_array['template_page_4'],
                        page_title=result_data_array['title'],
                        result_data_array=result_data_array,
                        )
        else:
            self.redirect(templates_page_array['template_page_3'])
