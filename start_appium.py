# coding=utf-8
import time

from appium import webdriver


# 定义启动模拟器配置
def get_driver():
    capabilities = {
        "platformName": "Android",
        # "automationName":"UiAutomator2",
        # "appWaitActivity":"com.baidu.tieba.LogoActivity",
        "deviceName": "127.0.0.1:7555",
        "app": "C:\\Users\\pintec\\AppData\\Local\\Programs\\Appium\\testapk\\baidutieba.apk",
        "noReset": "true"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    time.sleep(15)
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


# 点击【关注】下[戳这登录]按钮，进行跳转至登录页面
def go_login():
    driver.find_element_by_id('com.baidu.tieba:id/tv_concern_login_and_see_more').click()


# 在登录页面输入手机号，并且点击【下一步】按钮
def login():
    # driver.find_element_by_accessibility_id('QQ').click()
    driver.find_element_by_class_name('android.widget.EditText').send_keys('15901084142')
    time.sleep(5)
    driver.find_element_by_class_name('android.widget.Button').click()  # 点击 下一步 按钮
    time.sleep(6)
    elements = driver.find_elements_by_class_name('android.widget.Button')  # 点击‘换个登录方式’按钮
    elements[1].click()  # 页面有多个button元素，通过下标得方式进行点击
    print("button个数:" + str(len(elements)))
    time.sleep(10)
    # driver.tap([(0,892), (576,955)])
    # driver.find_element_by_accessibility_id('帐号密码登录').click()
    webview = driver.contexts
    print(webview)  # 打印看看有几个webview
    for viw in webview:
        if 'NATIVE_APP' in viw:
            driver.switch_to.context(viw)
            # break
    driver.tap([(273, 920), (576, 955)])
    # driver.find_element_by_accessibility_id('帐号密码登录').click()
    # driver.find_element_by_xpath('//android.view.View[@text="帐号密码登录"]').click()
    # xp = driver.find_elements_by_xpath('//android.widget.Button[@content-desc="换个登录方式"]')
    # driver.find_element_by_xpath('//android.widget.Button[@content-desc="换个登录方式"]').click()
    # driver.find_element_by_xpath(
    # '//android.view.View[@resource-id="passFooter"]/../preceding-sibling::帐号密码登录').click()
    # driver.find_element_by_xpath('//android.webkit.WebView[@class="android.view.View"]/preceding-sibling::*[@index="1"]').click()
    driver.find_element_by_xpath \
            (
            '//android.webkit.WebView[@content-desc="帐号密码登录"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.widget.EditText').send_keys(
        '1234567a')  # 输入密码
    driver.find_element_by_accessibility_id('登 录').click()  # 点击登录按钮
    print("===========登录成功=================")


if __name__ == '__main__':
    driver = get_driver()
    # swipe_on('left')
    # time.sleep(3)
    # swipe_on('right')
    time.sleep(3)
    swipe_on('right')
    time.sleep(3)
    go_login()
    time.sleep(15)
    login()
    # login_by_uiautomator()
