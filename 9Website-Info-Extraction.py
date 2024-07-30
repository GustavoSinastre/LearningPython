# In this code, we'll extract some info and save them

# Imporing the libraries used in this project
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep




# Importing the sheet's useds
search_sheet_path = 'Files-9Website-Info-Extraction/Lista de Ativos Pesquisa.xlsx'
search_sheet = openpyxl.load_workbook(search_sheet_path)
search_page = search_sheet['Pesquisa']
final_sheet_path = 'Files-9Website-Info-Extraction/Lista de Ativos Final.xlsx'
final_sheet = openpyxl.load_workbook(final_sheet_path)
final_page = final_sheet['Resultado']

# Opening the website
url_path = 'https://statusinvest.com.br/'
driver = webdriver.Chrome()
driver.get(url_path)

wait = WebDriverWait(driver,15)

# Creating the search loop
for row in search_page.iter_rows(min_row=2,values_only=True):
    ATIVO = row
    search_button = element = driver.find_element(By.XPATH, '//i[@class="material-icons prefix" and text()="search"]')
    sleep(1)

    search_button.click()
    search_field = element.find_element(By.XPATH, "//input[@class='Typeahead-input input tt-input']")
    search_field.send_keys(ATIVO)
    sleep(1)

    item_to_click = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@class="code text-main-green" and @title="ticker/código do ativo"]')))
    item_to_click.click()
    sleep(5)
    
    value_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//strong[@class="value"]')))
    value_text = value_element.text



    
