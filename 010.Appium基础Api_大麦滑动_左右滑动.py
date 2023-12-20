
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
desired_caps.set_capability("appPackage", "cn.damai")

# App界面名
desired_caps.set_capability("appActivity", "cn.damai.homepage.MainActivity")

# 不重置app
desired_caps.set_capability('noReset', True)

# 使用unicode输入
desired_caps.set_capability('unicodeKeyboard', True)

# 隐藏键盘
desired_caps.set_capability('resetKeyboard', False)

# 使用 AppiumOptions 对象设置 driver  连接到Appium服务器
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=desired_caps)


# 1.点击演唱会
driver.find_element(By.ID,"cn.damai:id/bricks_ball_icon").click()

# 2.模拟手机滑动频道(900,300 ,300,300) ，找到，食品母婴”频道，并点击(左右滑动)
# 方法一
# driver.swipe(1256,380,50,380,200)

# 方法二
Layout=driver.find_element(By.ID,"cn.damai:id/horScrollView")
print(Layout.location,Layout.size)
size=Layout.size
start_y=size.get("width")*0.75
end_y=size.get("width")*0.25
height=size.get("height")/2+Layout.location.get("y")
print(start_y,height,end_y,height)
driver.swipe(start_y,height,end_y,height)
driver.swipe(start_y,height,end_y,height)
driver.swipe(start_y,height,end_y,height)

# 等待时间
time.sleep(3)

# 3.点击儿童亲子
LinearLayout=driver.find_element(By.XPATH,"(//android.widget.LinearLayout[@class='android.widget.LinearLayout'])[48]").find_elements(By.CLASS_NAME,"android.widget.LinearLayout")
for Linear in LinearLayout:
    print(Linear.find_element(By.ID,"cn.damai:id/tv_title").text)
    if Linear.find_element(By.ID,"cn.damai:id/tv_title").text=='儿童亲子':
        Linear.find_element(By.ID,"cn.damai:id/tv_title").click()
        break

# 关闭App
driver.quit()