from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Variavel com a URL do site que iremos acessar
base_url = 'https://www.fronteditor.dev/'

@given(u'acesso a pagina inicial do front editor')
def step_impl(context):
    context.driver.get(base_url)
    time.sleep(3)


@when(u'clica no html')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div[1]/main/div/section/div/div/div[1]/div[2]/div[1]/div[4]'))).click()
    time.sleep(3)


@when(u'insiro o codigo html')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div[1]/main/div/section/div/div/div[1]/textarea'))).send_keys('<h1>OLA MUNDO</h1>')
    time.sleep(3)
    
@when(u'clica no css')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div[1]/nav/button[2]'))).click()
    time.sleep(3)
    
@when(u'insiro o codigo css')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div[1]/main/div/section/div/div/div[1]/textarea'))).send_keys("h1{color:aqua;}")
    time.sleep(3)

@when(u'clica no js')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div[1]/nav/button[3]'))).click()
    time.sleep(3)
    
@when(u'insiro o codigo js')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div[1]/main/div/section/div/div/div[1]/textarea'))).send_keys("const changecolor = document.querySelector('h1');" + "\n" + "changecolor.style.color = 'green';")
    time.sleep(3)

