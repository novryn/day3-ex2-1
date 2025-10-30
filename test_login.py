import time

def test_click_login_button(driver):
    time.sleep(3)
    driver.find_element(By.ID, "loginBtn").click()