from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time
import os

folder_name = "screenshots"
os.makedirs(folder_name, exist_ok=True)

#การเปิดหน้าเว็บโดยไม่ปิดเอง
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

try :
    driver.get("http://localhost:3000/")
    driver.find_element(By.LINK_TEXT,"สมัครสมาชิก").click()

    signup = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'สมัครบัญชีของคุณ')]"))).text.strip()
    assert signup == "สมัครบัญชีของคุณ"
    print("✅ Check the success words")

    dropdown = Select(driver.find_element(By.XPATH,"//form/select"))
    dropdown.select_by_visible_text("กลุ่มงานบริการด้านปฐมภูมิและองค์รวม")

    internal = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//form/p[2]"))).text
    assert internal == "ระบบจะกำหนดบทบาท: บุคลากรภายใน (INTERNAL)"
    print("✅ internal sign-up message displayed correctly")

    driver.find_element(By.XPATH, "//input[@placeholder='name']").send_keys("นภัส ศิริกาญจน์")
    driver.find_element(By.XPATH,"//input[@placeholder='+66']").send_keys("0859875625")
    driver.find_element(By.XPATH,"//input[@placeholder='example@gmail.com']").send_keys("napass.sirikarn@gmail.com")
    driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("napass1234")
    driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("napass1234")
    time.sleep(2)

    driver.find_element(By.XPATH,"//form/button").click()
    time.sleep(5)

    driver.save_screenshot(os.path.join(folder_name, "TC_INSignUp_01.png"))
    time.sleep(1)    

finally:
    driver.quit()