
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

desired_caps.set_capability("unicodeKeyboard", True)

desired_caps.set_capability("resetKeyboard", True)

# 使用 AppiumOptions 对象设置 driver  连接到Appium服务器
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=desired_caps)


# App操作 
# scroll滑动(scroll("开始滑动元素","结束滑动元素"))
start_scroll=driver.find_element(By.XPATH, "//*[@text='存储']")
end_scroll=driver.find_element(By.XPATH, "//*[@text='网络和互联网']")
print(start_scroll,end_scroll)
driver.scroll(start_scroll,end_scroll)



time.sleep(10)


# drag_and_drop拖拽(drag_and_drop("开始拖拽元素","结束拖拽元素"))
drag_scroll=driver.find_element(By.XPATH, "//*[@text='安全和紧急情况']")
end_scroll=driver.find_element(By.XPATH, "//*[@text='存储']")
driver.drag_and_drop(drag_scroll,end_scroll)


# 等待时间
time.sleep(3)

# 关闭App
driver.quit()