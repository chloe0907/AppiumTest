from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        # desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['appActivity'] = '.common.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        current_price = float(self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text)
        assert current_price > 200
        # print(self.driver.page_source)
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/title_container"]/android.widget.TextView[2]').click()
        locator = (MobileBy.XPATH, '//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]')

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/title_container").childSelector(text("股票"))').click()
        alibaba_price = self.driver.find_element(MobileBy.XPATH, )
        print(alibaba_price)
        sleep(3)

    def test_test_attr(self):
        search_element = self.driver.find_element_by_id('com.xueqiu.android:id/tv_search')
        print(search_element.text)
        print(search_element.location)
        print(search_element.size)

        if search_element.is_enabled():
            search_element.click()
            self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
            alibaba_element = self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]')
            if alibaba_element.is_displayed():
                print("搜索成功")
            else:
                print("搜索失败")


    def test_touchaction(self):

        actions = TouchAction(self.driver)
        window_size = self.driver.get_window_size()
        width = window_size['width']
        height = window_size['height']
        x1 = width * 0.5
        y_start = height * 0.8
        y_end = height * 0.2
        print(x1, y_start, y_end)
        actions.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()
        sleep(3)

    def test_uiautomator(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码登录")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("12345")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("12345")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

        # 根据父节点，定位子节点
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/title_container").childSelector(text("股票"))').click()

    def test_scroll(self):
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/title_text").text("推荐")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).'
                                                        'instance(0)).scrollIntoView(new UiSelector().'
                                                        'text("雪球股票").instance(0));')

    if __name__ == '__main__':
        pytest.main()