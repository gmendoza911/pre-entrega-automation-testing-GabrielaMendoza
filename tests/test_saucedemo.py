import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from utils.helpers import login_helper




@pytest.fixture(scope="module")
def driver():
    # Configuracion de Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
   
    yield driver
    
    driver.quit()


def test_01_login(driver):

    # Ejecutar login mediante función auxiliar
    login_helper(driver)

    # Verificar que el login haya sido exitoso
    assert "/inventory.html" in driver.current_url, \
        "Error: No se redirigió a /inventory.html"


def test_02_verificar_catalogo(driver):
    # obtener el título de la página y el título de la sección de productos
    page_title = driver.title
    section_title = driver.find_element(By.CLASS_NAME, "title").text

    # Verificar que ambos títulos sean correctos
    assert page_title == "Swag Labs", f'Error: El título de la página es incorrecto. Título actual: {page_title}'
    assert section_title == "Products", f'Error: El título de la sección es incorrecto. Título actual: {section_title}'



def test_03_productos_visibles(driver):
    # Verificar que los productos estén visibles en la página
    inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")

    # Verificar que exista al menos un producto visible
    assert len(inventory_items) > 0, "Error: No se encontraron productos visibles en la página."    



def test_04_validar_interfaz(driver):
    # Obtener el botón de menú y el filtro de productos
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

    # Verificar que ambos elementos sean visibles
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


def test_06_verificar_contador_carrito( driver ):
    # Obtener el contador del carrito
    contador_carrito = driver.find_element(By.CLASS_NAME,'shopping_cart_badge').text

    # Verificar que el contador muestre un producto
    assert contador_carrito == "1" ,f'Error: Se esperaba 1 , obtuvo {contador_carrito}'


def test_07_navegar_carrito(driver):
    # Acceder al carrito
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    # Verificar que se haya navegado correctamente
    assert "/cart.html" in driver.current_url , "Error: No se redirigió a /cart.html"

def test_08_comprobar_producto_en_el_carrito( driver):
    # Obtener el nombre del producto dentro del carrito
    producto_nombre_en_carrito = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text

    # Verificar que sea el producto esperado
    assert producto_nombre_en_carrito == 'Sauce Labs Backpack' , f'Error: NO ES EL MISMO NOMBRE'        



def test_09_nombre_precio_primer_producto(driver):

    # Volver al catálogo
    driver.get("https://www.saucedemo.com/inventory.html")

    # Obtener el primer producto del catálogo
    first_item = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]

    # Obtener el nombre y precio del primer producto
    nombre_producto = first_item.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    precio_producto = first_item.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    # Mostrar el nombre y precio
    print(f"Primer producto: {nombre_producto} - Precio: {precio_producto}")

    # Verificar los datos
    assert nombre_producto == "Sauce Labs Backpack", \
        f"Error: El nombre del producto es incorrecto. Nombre actual: {nombre_producto}"

    assert precio_producto == "$29.99", \
        f"Error: El precio del producto es incorrecto. Precio actual: {precio_producto}"
