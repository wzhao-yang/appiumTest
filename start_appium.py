# coding=utf-8
import time

from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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
    driver.find_element_by_class_name('android.widget.EditText').send_keys('xxx')
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
    driver.find_element_by_xpath \
            (
            '//android.webkit.WebView[@content-desc="帐号密码登录"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.widget.EditText').send_keys(
        '1234567a')  # 输入密码
    driver.find_element_by_accessibility_id('登 录').click()  # 点击登录按钮
    print("===========登录成功=================")


# 在推荐页签内，找到首帖，进行点赞并发表评论；
def thumbs_up():
    # driver.find_element_by_accessibility_id('推荐').click()  # 点击推荐页签
    swipe_on('left')
    time.sleep(3)
    driver.find_element_by_id('com.baidu.tieba:id/img_agree').click()  # 点赞
    time.sleep(3)
    driver.find_element_by_id('com.baidu.tieba:id/thread_info_commont_img').click()  # 点击评论按钮
    time.sleep(3)
    # driver.find_element_by_id('com.baidu.tieba:id/pb_editor_tool_comment_reply_text').click()  # 点击文本框
    driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.baidu.tieba:id/pb_editor_tool_comment_reply_text")').click()  # 点击评论文本款
    time.sleep(3)
    driver.find_element_by_class_name("android.widget.EditText").send_keys("我来聊几句，不知道说什么呢？")

    time.sleep(3)
    driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.View').click()  # 点击文本框
    print('发表评论完成')
    time.sleep(3)
    swipe_on('down')
    time.sleep(1)
    swipe_on('up')
    swipe_on('left')


# 获取到tost信息
def get_tost():
    time.sleep(2)
    driver.find_element_by_id('android.widget.EditText').send_keys('xxxx')
    tost_element = ("xpath", "//*[contains(@text,'请输入密码')]")
    WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(tost_element))


if __name__ == '__main__':
    driver = get_driver()
    # # swipe_on('left')
    # # time.sleep(3)
    # # swipe_on('right')
    # time.sleep(3)
    # swipe_on('right')
    # time.sleep(3)
    # go_login()
    # time.sleep(15)
    # login()
    # time.sleep(10)
    thumbs_up()
    get_tost()
    # login_by_uiautomator()
