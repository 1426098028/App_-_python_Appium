
import time 
# 导入appium
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
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

# 使用 AppiumOptions 对象设置 driver  连接到Appium服务器
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=desired_caps)


# App操作
# 1.获取当前App界面的包名和界面名
print(f"当前App界面的包名:{driver.current_package},当前App界面的界面名:{driver.current_activity}")
time.sleep(3)
# 2.切换到打电话首页，获取对应包名和界面名
# mCurrentFocus=Window{7431d74 u0 com.android.dialer/com.android.dialer.main.impl.MainActivity}
# 2.1 切换到打电话，并且指定直接进入页面
driver.start_activity("com.android.dialer", "com.android.dialer.main.impl.MainActivity")
print(f"切换后App界面的包名:{driver.current_package},切换后App界面的界面名:{driver.current_activity}")
# 3.关闭打电话
driver.close_app()









# 等待时间
time.sleep(5)

# 关闭App
driver.quit()