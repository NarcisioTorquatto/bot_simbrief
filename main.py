from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import pywhatkit as kit
import time
import random

USER = "testes.automation@gmail.com"
PASSWORD = "N@ttoGl3ic3121430"

class SeleniumBot:
    def __init__(self):
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
        except WebDriverException as e:
            print(f"Erro ao acessar o site {url}: {e}")
            raise
    
    def executar_logica_bot(self):
        """
        Implementar aqui a lógica específica do bot.
        """
        try:
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
            campo_email.send_keys(USER)
            time.sleep(random.uniform(1, 2))
            
            btn_email_proximo = self.driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
            btn_email_proximo.click()
            time.sleep(random.uniform(5, 6))
            
            campo_senha_email = self.driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
            campo_senha_email.click()
            time.sleep(random.uniform(1, 2))
            campo_senha_email.send_keys(PASSWORD)
            time.sleep(random.uniform(1, 2))
            
            btn_senha_next = self.driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span')
            btn_senha_next.click()
            time.sleep(random.uniform(3, 4))
                 
        except NoSuchElementException as e:
            print(f"Erro ao encontrar elemento: {e}")
        
    import pywhatkit as kit

    def solicitar_codigo_whatsapp(self, numero_whatsapp):
        """
        Envia uma mensagem para o WhatsApp solicitando o código do Google Authenticator 
        e aguarda a resposta manual para inserir no campo de autenticação.

        Args:
            numero_whatsapp (str): Número de telefone no formato +55XXXXXXXXXXX para enviar a mensagem.

        Returns:
            str: Código digitado pelo usuário no console.
        """
        mensagem = "Digite o código do Google Authenticator e me responda aqui!"
        
        # Enviar mensagem via WhatsApp
        kit.sendwhatmsg_instantly(numero_whatsapp, mensagem, tab_close=True)

        # Aguarda o usuário digitar o código manualmente no console
        codigo = input("Digite o código do Google Authenticator recebido no WhatsApp: ")

        return codigo        
    
    def run(self, url: str):
        """
        Método principal para executar o bot.
        :param url: URL a ser acessada
        """
        try:
            self.acessar_site(url)
            self.executar_logica_bot()

            # Solicita o código pelo WhatsApp e aguarda entrada manual
            codigo = self.solicitar_codigo_whatsapp("+5592985872394")

            # Insere o código no campo de autenticação
            campo_codigo = self.driver.find_element(By.XPATH, '//*[@id="totpPin"]')
            campo_codigo.send_keys(codigo)
            time.sleep(random.uniform(1, 2))


            btn_codigo_next = self.driver.find_element(By.XPATH, '//*[@id="totpNext"]/div/button/span')
            btn_codigo_next.click()
            input()
            
        finally:
            self.finalizar()
    
    def finalizar(self):
        """
        Finaliza o WebDriver e encerra o programa corretamente.
        """
        if self.driver:
            self.driver.quit()
            print("WebDriver finalizado com sucesso.")
    
if __name__ == "__main__":
    bot = SeleniumBot()
    bot.run("https://www.simbrief.com/home/")