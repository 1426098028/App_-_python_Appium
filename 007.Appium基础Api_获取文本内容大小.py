
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
# 需求:打开手机《设置》应用，完成下面的步骤
# 1.获取搜索栏的信息并打印
driver.find_element(By.CLASS_NAME,"android.view.ViewGroup").click()
time.sleep(3)
search=driver.find_element(By.ID,"android:id/search_src_text")
print(f"文本内容：{search.text}")
# 2.计算出搜索栏的坐标和大小
print(f"坐标:{search.location},大小:{search.size}")

# 等待时间
time.sleep(3)

# 关闭App
driver.quit()