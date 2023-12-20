
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

#需求:打开手机《设置》应用，完成下面的步骤
# 1.使用ID定位，获取所有resource-id 为 ”android:id/title” 的元素，并打印其文字内容
titles= driver.find_elements(By.ID, "android:id/title")
for title in titles:
    print(f"ID定位:{title.text}")
# 2.使用CLASS定位，获取所有cLass 为“android.widget.TextView”的元素，并打印其文字内容
TextViews=driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
for TextView in TextViews:
    print(f"CLASS定位:{TextView.text}")
# 3.使用XPATH定位，获取所有包含‘设’的元素，并打印其文字内容
Texts=driver.find_elements(By.XPATH, "//*[contains(@text,'设')]")
for Text in Texts:
    print(f"XPATH定位:{Text.text}")




# 等待时间
time.sleep(3)

# 关闭App
driver.quit()