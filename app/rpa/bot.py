from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
from datetime import datetime

from dotenv import load_dotenv
import os

load_dotenv()

USER=os.getenv("USER_S")
PASSWORD=os.getenv("PASSWORD_S")

#def scraper(job_id, fecha_inicial, fecha_final, limit, db):
def scraper(fecha_inicial, fecha_final):
    chrome_options = Options()

    driver = webdriver.Chrome(options=chrome_options)
    #chrome_options.add_argument("--headless")
    wait = WebDriverWait(driver, 180)

    try:
        driver.get("https://prodiagnosticotest.hiruko.com.co/login")

        input_user = driver.find_element(By.ID, "username")
        input_user.send_keys(USER)
        print("Escribiendo usuario")
        input_password = driver.find_element(By.ID, "password")
        input_password.send_keys(PASSWORD)
        print("Escribiendo contraseña")

        driver.find_element(By.ID, "_submit").click()

        print("Inicio de sesión exitoso")

        boton_facturacion = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[.//span[text()='Facturación']]")
        ))
        boton_facturacion.click()
        print("Menu de facturación desplegado") #eliminar prints

        boton_generar_factura = wait.until(EC.element_to_be_clickable((By.ID, "ui-id-73")))
        boton_generar_factura.click()
        print("Accediendo a generar factura")

        boton_fecha_inicial = wait.until(EC.visibility_of_element_located((By.ID, "dateInit")))
        print("Llegando hasta fecha inicial")
        boton_fecha_inicial.clear()
        boton_fecha_inicial.send_keys(fecha_inicial)  

        boton_fehca_final = driver.find_element(By.ID, "dateEnd")
        boton_fehca_final.clear()
        boton_fehca_final.send_keys(fecha_final)

        #Seleccion convenio
        boton_convenio = driver.find_element(By.CSS_SELECTOR, "button[data-id='convenios_facturas']").click()
        opcion_savia = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='text' and text()='Savia Salud Subsidiado']")
        ))
        opcion_savia.click()

        #contrato facturas
        boton_contrato_facturas = driver.find_element(By.CSS_SELECTOR, "button[data-id='contratos_facturas']").click()
        opcion_contrato = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='text' and text()='SAVIA SALUD SUBSIDIADO']")
        ))
        opcion_contrato.click()

        #Sedes
        boton_sedes = driver.find_element(By.CSS_SELECTOR, "button[data-id='sedes_facturas']")
        boton_sedes.click()

        boton_seleccionar_todo = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "bs-select-all")
        ))
        boton_seleccionar_todo.click()

        #Modalidad
        driver.find_element(By.CSS_SELECTOR, "button[data-id='modalidades']").click()

        opcion_us = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='text' and text()='US']")
        ))
        opcion_us.click()
        print("Modalidad 'US' seleccionada")

        driver.find_element(By.ID, "buscar").click()
        print("Búsqueda enviada, esperando resultados...")

        # Esperar a que la tabla contenga filas que no sean el mensaje de "No hay datos"
        wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#tablaPacientes tbody tr")) > 0)

        print("Resultados encontrados")


        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()