from selenium import webdriver
import time
import unittest

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html')

   #判断是否登陆成功
    def is_login(self):
        # 通过查看能否获取到登陆后页面的元素判断是否登录成功
      try:
        t = self.driver.find_element_by_css_selector('#userMenu>a').text
        print(t)
        return t
      except:
          return ''

    #判断alert是否存在
    def is_alert_exist(self):
        try:
          time.sleep(2)
          alert = self.driver.switch_to.alert
          text = alert.text
          alert.accept()
          return text
        except:
          return ''

    #登录
    def login(self, username, userpswd):
        self.driver.find_element_by_id('account').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(userpswd)
        self.driver.find_element_by_id('submit').click()


    #用例一（正确的输入）
    def test_01(self):
        # 添加等待时间，是为了等待页面缓冲时间，等彻底跳到另一张页面，才开始定位元素
        time.sleep(3)

        #调用登录函数进行登录
        self.login('admin', 123456)

        time.sleep(3)
        t = self.is_login()
        print('获取登录的结果：%s', t)
        self.assertTrue(t == 'admin')

#清空cookies，退出登录
    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

#用例二（错误的输入）
    def test_02(self):
        time.sleep(3)

        #调用登录函数
        self.login('adminf', 123456)

        time.sleep(3)
        t = self.is_login()
        print('获取登录的结果：%s', t)
        self.assertTrue(1 == 2)#故意断言失败来进行截图

    def tearDown(self):
        self.is_alert_exist()
        # print('弹窗是否存在：%s', alert)


