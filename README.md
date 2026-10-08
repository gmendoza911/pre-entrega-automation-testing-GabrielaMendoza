
# Pre-entrega Automation Testing - Gabriela Mendoza

## Descripción

Proyecto de automatización de pruebas sobre la aplicación web SauceDemo.

El objetivo es automatizar y validar diferentes funcionalidades de la aplicación utilizando pruebas con Selenium y Pytest.

## Tecnologías utilizadas

- Python
- Pytest
- Selenium WebDriver
- WebDriver Manager
- Git
- GitHub
- Visual Studio Code

## Estructura del proyecto

```text
pre-entrega GabrielaMendoza/
│
├── tests/
│   └── test_saucedemo.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── .gitignore
├── pytest.ini
└── README.md
```

## Casos de prueba automatizados

1. **Login:** verificar que el usuario pueda iniciar sesión correctamente.
2. **Verificar catálogo:** comprobar el título de la página y de la sección de productos.
3. **Productos visibles:** verificar que los productos sean visibles en el catálogo.
4. **Validar interfaz:** comprobar la visibilidad del botón de menú y del filtro de productos.
5. **Agregar producto al carrito:** agregar un producto y verificar que la acción se haya realizado correctamente.
6. **Verificar contador del carrito:** comprobar que el contador del carrito muestre la cantidad correcta de productos.
7. **Navegar al carrito:** verificar que el usuario pueda acceder correctamente al carrito.
8. **Comprobar producto en el carrito:** verificar que el producto agregado corresponda al esperado.
9. **Verificar nombre y precio:** comprobar el nombre y precio del primer producto del catálogo.

## Funcion auxiliar

Se creó una función auxiliar login_helper() dentro de utils/helpers.py.

## Ejecucion de pruebas

pytest -v

## Resultado de las pruebas

9 casos de prueba automatizados
9 pruebas aprobadas
0 pruebas fallidas
Última ejecución:

```text
9 passed in 6.36s
```
## Sitio web utilizado

https://www.saucedemo.com/