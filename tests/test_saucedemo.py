import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    # Configuracion de Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    
    driver.quit()


def test_01_login(driver):
    # Abrir la página para inicio de sesión
    driver.get("https://www.saucedemo.com/")

    # Ingresar credenciales válidas
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    # Verificar que se haya iniciado sesión correctamente
    assert "inventory.html" in driver.current_url, f'Error: No se pudo iniciar sesión. URL actual: {driver.current_url}'