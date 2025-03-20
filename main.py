
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from botcity.core import DesktopBot
from selenium import webdriver
from dotenv import load_dotenv

import pygetwindow as gw
import pytesseract
import random
import time
import cv2
import os
import re

load_dotenv()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

user = os.getenv("USER")
password = os.getenv("PASSWORD")

class SeleniumBot:
    def __init__(self):
        self.deskBot = DesktopBot()
           
        """
        Inicializa o WebDriver com opções configuráveis utilizando WebDriver Manager.
        """
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Executar em modo headless
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Evitar detecção de automação
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        
        # Usar um perfil de usuário específico (substitua pelo caminho do seu perfil)
        chrome_options.add_argument(r"C:\Users\natto\AppData\Local\Google\Chrome\User Data")
        chrome_options.add_argument("profile-directory=Default")
                                
        try:
            self.service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=self.service, options=chrome_options)
        except WebDriverException as e:
            print(f"Erro ao iniciar o WebDriver: {e}")
            raise
      
    def acessar_site(self, url: str):
        """
        Acessa o site desejado.
        :param url: URL do site a ser acessado
        """
        try:
            self.driver.get(url)
            time.sleep(random.uniform(2, 4))  # Aguarde um tempo aleatório para garantir que a página carregue
            
            elemento = self.driver.find_element(By.TAG_NAME, "body")
            print("Página carregada com sucesso!", elemento.text[:100])  # Exibir parte do conteúdo
            self.driver.maximize_window()
            
            while len(self.driver.find_elements(By.XPATH, '//*[@id="cookie-settings-simple"]/div[2]/div[2]')) < 1:
                time.sleep(5)
                print('Aguardando carregamento completo da página...')
                
            if self.driver.find_element(By.XPATH, '//*[@id="cookie-settings-simple"]/div[2]/div[2]'):
                print('Aceitando Cookies')
                time.sleep(random.uniform(1, 2))
                self.driver.find_element(By.XPATH, '//*[@id="cookie-settings-simple"]/div[2]/div[2]').click()
                time.sleep(random.uniform(1, 2))
            else:
                print('Janela de Cookies não encontrada')
                
            btn_login = self.driver.find_element(By.XPATH, '/html/body/header/div/div[2]/div[1]/div/div/div/a')
            btn_login.click()
            
            time.sleep(random.uniform(1, 2))
            btn_sigin = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
            btn_sigin.click()
            time.sleep(random.uniform(1, 2))
            
            btn_login_google = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/a[1]')
            btn_login_google.click()
            time.sleep(random.uniform(1, 2))
            
            campo_email = self.driver.find_element(By.XPATH, '//*[@id="identifierId"]')
            campo_email.click()
            time.sleep(random.uniform(1, 2))
            campo_email.send_keys(user)
            time.sleep(random.uniform(1, 2))
            
            btn_email_proximo = self.driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
            btn_email_proximo.click()
            time.sleep(random.uniform(5, 6))
            
            campo_senha_email = self.driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
            campo_senha_email.click()
            time.sleep(random.uniform(1, 2))
            campo_senha_email.send_keys(password)
            time.sleep(random.uniform(1, 2))
            
            btn_senha_next = self.driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span')
            btn_senha_next.click()
            time.sleep(random.uniform(3, 4))
            
            self.checar_whatsapp()
            codigo = self.whatsapp_navegacao()
            
            if codigo:
                print(f"Código identificado: {codigo}")
            else:
                print("Nenhum código encontrado!")
            
            window = gw.getWindowsWithTitle("Fazer login nas Contas do Google - Google Chrome")[0]  # Altere para o título correto
            if window:
                window.restore()# Restaura se estiver minimizado
                window.activate()  # Traz a janela para frente
                window.maximize()
                
            campo_autenticador = self.driver.find_element(By.XPATH,'//*[@id="totpPin"]')
            campo_autenticador.click()
            campo_autenticador.send_keys(codigo)
            
            btn_next_autenticador = self.driver.find_element(By.XPATH,'//*[@id="totpNext"]/div/button/span') 
            btn_next_autenticador.click()
            input()
              
        except WebDriverException as e:
            print(f"Erro ao acessar o site {url}: {e}")
            raise

    def checar_whatsapp(self):
        
        btn_whatsapp = self.deskBot.find("btn_whatsapp", matching=0.97, waiting_time=10000)
        if not btn_whatsapp:
            self.deskBot.find("btn_windows", matching=0.97, waiting_time=10000)
            self.deskBot.click()
            time.sleep(2)
            self.deskBot.kb_type("Whatsapp")  
            time.sleep(2)
            self.deskBot.enter()       
            
        else:
            self.deskBot.find("btn_whatsapp", matching=0.97, waiting_time=10000)
            self.deskBot.click()
            time.sleep(2)
                            
    def whatsapp_navegacao(self):
        
        # Searching for element 'lupa_pesquisa_whatsapp'
        btn_lupa_pesquisa = self.deskBot.find("lupa_pesquisa_whatsapp", matching=0.97, waiting_time=10000)
        if not btn_lupa_pesquisa:
            print('Botão Lupa não encontrado')
        else:
            time.sleep(2)
            self.deskBot.click()
            time.sleep(2)
            self.deskBot.kb_type('Meu Tim')
            # Searching for element 'btn_meu_tim'
            time.sleep(2)# Searching for element 'btn_meu_tim'
            if not self.deskBot.find("btn_meu_tim", matching=0.97, waiting_time=10000):
                print('Contato MEU TIM, Não encontrado"')
            self.deskBot.click()
            time.sleep(1)
            self.deskBot.kb_type('Por favor, informe o Codigo do Antenticador:')
            self.deskBot.enter() 
            
        time.sleep(20)
        # Capturar a tela do WhatsApp
        self.deskBot.screenshot("chat.png")

        # Processar a imagem com OCR
        img = cv2.imread("chat.png")
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        texto_extraido = pytesseract.image_to_string(img_gray)

        print(f"Texto extraído: {texto_extraido}")  # Debug

        # Extrair o código numérico de 6 dígitos
        padrao = r"\b\d{6}\b"
        codigos = re.findall(padrao, texto_extraido)

        if codigos:
            return codigos[-1]  # Retorna o código mais recente

        return None         
                         
    def finalizar(self):
        """
        Finaliza o WebDriver e encerra o programa corretamente.
        """
        if self.driver:
            self.driver.quit()
            print("WebDriver finalizado com sucesso.")
            
    def run(self, url: str):
        """
        Método principal para executar o bot. :param url: URL a ser acessada
        """
        try:
            self.acessar_site(url)
            
        except NoSuchElementException as e:
            print(f"Erro ao encontrar elemento: {e}")
            
        finally:
            self.finalizar()
    
if __name__ == "__main__":
    bot = SeleniumBot()
    bot.run("https://www.simbrief.com/home/")