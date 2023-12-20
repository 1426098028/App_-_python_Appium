
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

# 需求:打开手机《设警》应用，完成下面的步骤
# 1.使用ID定位，定位”放大镜”按钮，并点击  find_element(By.ID,'resource-id')
driver.find_element(By.ID, "com.android.settings:id/search_action_bar").click()
# 2.使用CLASS定位(find_element(By.CLASS_NAME,'class'))，定位”输入框”(send_keys)，输入”hello”
time.sleep(2)
driver.find_element(By.CLASS_NAME ,"android.widget.EditText").send_keys("hello")
# 3.使用XPATH定位(find_element(By.XPATH,"XPATH值"))，定位”返回”，并点击 android.widget.ImageButton
# XPATH值规则     
# //*[@属性名='属性值']
# //*[contains(@属性名='属性值')]
time.sleep(2)
driver.find_element(By.XPATH, "//*[@class='android.widget.ImageButton']").click()
# 4.使用NAME定位(find_element(By.ACCESSIBILITY_ID ,'content-desc'))，定位“放大镜”按钮，并点击
time.sleep(2)
driver.find_element(By.ACCESSIBILITY_ID, "向上导航").click()
# 5.等待3s，关闭app
# 等待时间
time.sleep(3)

# 关闭App
driver.quit()