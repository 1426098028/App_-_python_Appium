
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
# 打开通知栏   (open_notifications())
driver.open_notifications()

# 关闭通知栏
driver.press_keycode(4)




# # 等待时间
time.sleep(3)

# 关闭App
driver.quit()