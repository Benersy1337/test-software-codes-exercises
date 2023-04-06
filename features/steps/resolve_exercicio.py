from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Variavel com a URL do site que iremos acessar
base_url = 'https://www.w3schools.com/js/exercise_js.asp?filename=exercise_js_variables1'

@given(u'acesso a pagina do w3schools')
def step_impl(context):
    context.driver.get(base_url)
    time.sleep(3)

@when(u'coloco a variavel')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="assignmentcontainer"]/input[1]'))).send_keys('carName')
    time.sleep(3)

@when(u'coloco o valor da variavel')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="assignmentcontainer"]/input[2]'))).send_keys('Volvo')
    time.sleep(3)

@when(u'clico no botao submit')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="answerbutton"]'))).click()
    time.sleep(3)

@when(u'clico na div next')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="assignmentCorrect"]'))).click()
    time.sleep(3)

@when(u'clico em js arrays')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="exercisemenu"]/div[4]/div[9]'))).click()
    time.sleep(3)

@when(u'clico em exercicio 1')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="exercisemenu"]/div[4]/div[9]/div[2]/a[1]'))).click()
    time.sleep(3)

@when(u'atribuo valor a variavel do array')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="assignmentcontainer"]/input'))).send_keys('cars[1]')
    time.sleep(3)

@then(u'clico no botao para verificar resposta')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="answerbutton"]'))).click()
    time.sleep(3)


