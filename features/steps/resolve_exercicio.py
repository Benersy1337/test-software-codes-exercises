from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Variavel com a URL do site que iremos acessar
base_url = 'https://www.codepractice.dev/js/problems/181'

@given(u'acesso a pagina inicial do code practice')
def step_impl(context):
    context.driver.get(base_url)
    time.sleep(7)


@when(u'insiro o codigo js')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="code"]'))).send_keys('<h1>OLA MUNDO</h1>')
    time.sleep(5)
    



