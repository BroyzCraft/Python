from selenium import webdriver
import time

navegador = webdriver.Chrome()

navegador.get("https://leomadeiras.routeasy.com.br/#!/dashboard")
time.sleep(5)

username = navegador.find_element_by_xpath('//*[@id="page-top"]/section/div/div/div/div/div[1]/form[1]/div[1]/input')
password = navegador.find_element_by_xpath('//*[@id="page-top"]/section/div/div/div/div/div[1]/form[1]/div[2]/input')
username.send_keys("")
password.send_keys("")
navegador.find_element_by_xpath('//*[@id="page-top"]/section/div/div/div/div/div[1]/form[1]/div[3]/button').click()
time.sleep(5)

qtde = 20
aux = 2

menu = '/html/body/section/ui-view/div/div/div[1]/div[1]/div/div[3]/span'
fecharMenu = 'body > div.modal.fade.ng-isolate-scope.custom-options-modal-relatory.in > div > div > div > div.modal-header-options > a'
rotas = 'body > div.modal.fade.ng-isolate-scope.custom-options-modal-relatory.in > div > div > div > div.modal-body.ng-scope > div > div > div:nth-child(10)'
servicos = 'body > div.modal.fade.ng-isolate-scope.custom-options-modal-relatory.in > div > div > div > div.modal-body.ng-scope > div > div > div:nth-child(7)'

while aux < qtde:    
    navegador.get("https://leomadeiras.routeasy.com.br/#!/routings/list")
    time.sleep(3)
    navegador.find_element_by_xpath('/html/body/section/ui-view/div/div/div[' + str(aux) + ']').click()
    time.sleep(3)
    navegador.find_element_by_xpath(menu).click()
    time.sleep(3)
    navegador.find_element_by_css_selector(rotas).click()
    time.sleep(3)
    navegador.find_element_by_css_selector(servicos).click()
    time.sleep(3)
    navegador.find_element_by_css_selector(fecharMenu).click()
    time.sleep(10)
    aux += 1
