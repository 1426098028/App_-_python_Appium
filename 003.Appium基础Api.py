
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

# 将com.android.settings设为后抬
driver.background_app(10)

# 安装大麦App
# 1.检查App是否安装 is_app_installed('包名')
# 2.App安装 install_app('apk路径')
# 3.App卸载 remove_app('包名')
# mCurrentFocus=Window{b181bb8 u0 cn.damai/cn.damai.homepage.MainActivity}
if driver.is_app_installed("cn.damai"):
    print("大麦App已安装")
    driver.remove_app("cn.damai")
    print("大麦App已卸载")
else:
    print("大麦App未安装")
    driver.install_app(r"C:\Users\LzH\Desktop\App_自动化_python_Appium\damai_android_36166323781390.apk")
    print("大麦App已安装")














# 等待时间
time.sleep(5)

# 关闭App
driver.quit()