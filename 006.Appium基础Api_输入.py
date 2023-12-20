
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
# 1.点击”放大镜”
driver.find_element(By.ID,"com.android.settings:id/search_action_bar").click()
# 2.输入”hello”
time.sleep(2)
driver.find_element(By.CLASS_NAME,"android.widget.EditText").send_keys("hello")
# 3.暂停2秒
time.sleep(2)
# 4.清空所有文本内容(clear())
driver.find_element(By.CLASS_NAME,"android.widget.EditText").clear()
# 5.暂停5秒
time.sleep(5)
# 6.输入”你好”
driver.find_element(By.XPATH,"//*[@class='android.widget.EditText']").send_keys('你好')



# 等待时间
time.sleep(3)

# 关闭App
driver.quit()