import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager




@pytest.fixture(scope="module")
def driver():
    # Configuracion de Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
   
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

def test_02_verificar_catalogo(driver):
    
    page_title = driver.title
    section_title = driver.find_element(By.CLASS_NAME, "title").text

    assert page_title == "Swag Labs", f'Error: El título de la página es incorrecto. Título actual: {page_title}'
    assert section_title == "Products", f'Error: El título de la sección es incorrecto. Título actual: {section_title}'

def test_03_productos_visibles(driver):
    # Verificar que los productos estén visibles en la página
    inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")


    assert len(inventory_items) > 0, "Error: No se encontraron productos visibles en la página."    

def test_04_validar_interfaz(driver):
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

    assert menu_button.is_displayed(), "Error: El botón del menú no está visible."
    assert filtro.is_displayed(), "Error: El filtro no está visible."
    
def test_05_añadir_producto_al_carrito(driver):

    # Obtener el primer producto del catálogo
    first_item = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]

    # Buscar el botón para agregarlo al carrito
    boton_agregar = first_item.find_element(By.TAG_NAME, "button")

    # Agregar el producto al carrito
    boton_agregar.click()

    # Volver a buscar el primer producto después de la actualización
    first_item = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]

    # Obtener nuevamente el botón
    boton_remove = first_item.find_element(By.TAG_NAME, "button")

    # Verificar que el botón haya cambiado a "Remove"
    assert boton_remove.text == "Remove", \
        "Error: El producto no se agregó al carrito correctamente."
