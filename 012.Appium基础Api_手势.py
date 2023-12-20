
import time 
# 导入appium
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

# 创建 AppiumOptions 对象
desired_caps = AppiumOptions()
# 手机平台
desired_caps.set_capability("platformName", "Android")
# 手机版本号
desired_caps.set_capability("platformVersion", "14")

# 手机设备名
desired_caps.set_capability("deviceName", "emulator-5554")

# App包名
desired_caps.set_capability("appPackage", "com.android.settings")

# App界面名
desired_caps.set_capability("appActivity", ".Settings")

desired_caps.set_capability("unicodeKeyboard", True)

desired_caps.set_capability("resetKeyboard", True)

# 使用 AppiumOptions 对象设置 driver  连接到Appium服务器
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=desired_caps)


# App操作 
# 创建手势实例    .perform()   作用执行手势
touch_action=TouchAction(driver)

# 轻敲(touch_action.tap(元素或者坐标点).perform())  
WLAN_El=driver.find_element(By.XPATH,"//*[@text='网络和互联网']")
touch_action.tap(WLAN_El).perform()

time.sleep(3)
driver.find_element(By.XPATH,"//*[@text='互联网']").click()
time.sleep(3)


# 长按(touch_action.long_press(元素或者坐标点).perform())
con_el=driver.find_element(By.XPATH,"//*[@text='AndroidWifi']")
touch_action.long_press(con_el).perform()



# 按下(touch_action.press(元素))和抬起(touch_action.release())       可以模拟轻敲和长按手势
FX_el=driver.find_element(By.XPATH,"//*[@text='分享']")
touch_action.press(FX_el).perform()
print('按下')
time.sleep(10)
touch_action.press(FX_el).release().perform()
print('抬起')
time.sleep(1)

# 移动(touch_action.move_to(元素或者坐标点))
touch_action.press(x=248,y=1668).wait(1000).move_to(x=963,y=1668).wait(1000).release().perform()


# 返回
driver.press_keycode(4)
time.sleep(10)



# # 等待时间
time.sleep(3)

# 关闭App
driver.quit()