from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Edge('C:/Selenium/edgedriver')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")

#codificación de casos de prueba

barranav = driver.find_element(By.ID, "twotabsearchtextbox") #buscar la barra de navegación
barranav.send_keys("HP Pavilion Azul.") #escribir lo solicitado
barranav.send_keys("\n") #confirmar lo escrito con Enter
sleep(1) #tiempo de espera

driver.find_element(By.CSS_SELECTOR, ".s-main-slot .s-list-col-right h2 .a-link-normal").click() #dar click al primer producto que aparece
sleep(1) #tiempo de espera


select = Select(driver.find_element(By.CSS_SELECTOR, '#desktop_qualifiedBuyBox select')) #buscar el selector de productos
select.select_by_value("2") #cambiar a dos elementos seleccionados

sleep(1) #tiempo de espera

driver.find_element(By.CSS_SELECTOR, "#desktop_qualifiedBuyBox #add-to-cart-button").click() #dar click a añadir al carrito
sleep(1)

driver.find_element(By.CSS_SELECTOR, "#nav-cart").click() #visualizar el carrito
sleep(4.5)

