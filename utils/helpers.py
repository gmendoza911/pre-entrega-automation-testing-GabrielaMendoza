from selenium.webdriver.common.by import By


def login_helper(driver):
    # Ingresar a la página de SauceDemo
    driver.get("https://www.saucedemo.com/")

    # Completar usuario y contraseña
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Presionar el botón de Login
    driver.find_element(By.ID, "login-button").click()
    