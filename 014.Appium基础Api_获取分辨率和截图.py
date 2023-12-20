
import time 
# 导入appium
from appium import webdriver
from appium.options.common.base import AppiumOptions
from selenium.webdriver.common.by import By

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
# 获取分辨率
print(driver.get_window_size())

# 获取手机截图普通

print(driver.get_screenshot_as_file('截图.png'))

# 获取手机截图base64
print(driver.get_screenshot_as_base64())  



# # 等待时间
time.sleep(3)

# 关闭App
driver.quit()