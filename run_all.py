import unittest
import HTMLTestRunner
# 用例的路径
casePath = 'D:\\python\\pycharm\\PyCharm 2019.1\\pycharm_project\\web_auto\\testcase'
rule = 'test*.py'
discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern=rule)
#print(discover)

if __name__ == '__main__':
    reportPath = 'D:\\python\\pycharm\\PyCharm 2019.1\\pycharm_project\\web_auto\\report\\ ' + 'report1.html'
    fp = open(reportPath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='报告的title')
    runner.run(discover)
