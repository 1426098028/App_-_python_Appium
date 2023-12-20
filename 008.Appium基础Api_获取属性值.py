
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
# 1.获取所有 resource-id 为android:id/title”的元素
titles=driver.find_elements(By.ID, "android:id/title")
# 2.使用 get attribute 获取这些元素的 enabled、text、content-desc、resource-id、class的属性值
for title in titles:
    enabled=title.get_attribute('enabled')
    text=title.get_attribute('text')
    content_desc=title.get_attribute('name')
    resourceId=title.get_attribute('resourceId')
    className=title.get_attribute('className')
    print(f"获取属性值：{enabled},{text},{content_desc},{resourceId},{className}")

# 等待时间
time.sleep(3)

# 关闭App
driver.quit()