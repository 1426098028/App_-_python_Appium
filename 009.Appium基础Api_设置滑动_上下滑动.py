
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

# 练习一: 打开手机《设置》应用，完成下面的步骤
# 1.模拟手指从(100，1500)，滑动到《100，500)的位置(上下滑动)

time.sleep(3)
# 方法一
# driver.swipe(100, 1500, 100, 500, duration=500)

# 方法二
size=driver.get_window_size()
width=size.get("width")/2
start_y=size.get("height")*0.75
end_y=size.get("height")*0.25
driver.swipe(width,start_y,width,end_y)

# 等待时间
time.sleep(3)

# 关闭App
driver.quit()