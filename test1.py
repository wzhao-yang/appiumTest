# coding=utf-8
import time

from appium import webdriver


# 定义启动模拟器配置
def get_driver():
    capabilities = {
        "platformName": "Android",
        # "automationName":"UiAutomator2",
        "deviceName": "127.0.0.1:7555",
        "app": "C:\\Users\\pintec\\AppData\\Local\\Programs\\Appium\\testapk\\baidutieba.apk",
        "noReset": "true"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    time.sleep(30)
    return driver


# 获取手机浏览器的宽和高
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width, height


# 向左滑动
def swipe_left():
    x1 = get_size()[0] / 10 * 9  # print("宽的9/10：" + str(x1))
    y1 = get_size()[1] / 2  # print("高的1/2：" + str(y1))
    x = get_size()[0] / 10  # print("宽的1/10：" + str(x))
    driver.swipe(x1, y1, x, y1)


# 向右滑动
def swipe_right():
    x1 = get_size()[0] / 10
    y1 = get_size()[1] / 2
    x = get_size()[0] / 10 * 9
    driver.swipe(x1, y1, x, y1)


# 向上滑动
def swipe_up():
    x1 = get_size()[0] / 2
    y1 = get_size()[1] / 10 * 9
    x = get_size()[0] / 10
    driver.swipe(x1, y1, x, y1)


# 向下滑动
def swipe_down():
    x1 = get_size()[0] / 2
    y1 = get_size()[1] / 10
    y = get_size()[1] / 10 * 9
    driver.swipe(x1, y1, x1, y)


# 获取方向
def swipe_on(direction):
    if direction == 'up':
        swipe_up()
    elif direction == 'down':
        swipe_down()
    elif direction == 'left':
        swipe_left()
    else:
        swipe_right()


driver = get_driver()
swipe_on('left')
time.sleep(6)
swipe_on('right')
time.sleep(6)
swipe_on('down')
time.sleep(6)
swipe_on('up')
time.sleep(6)
print("滑屏结束")
time.sleep(5)
print("测试下")

