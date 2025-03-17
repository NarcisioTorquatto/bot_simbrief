from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import time

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
            time.sleep(2)  # Aguarde um tempo para garantir que a página carregue
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
        except NoSuchElementException as e:
            print(f"Erro ao encontrar elemento: {e}")
        
    def run(self, url: str):
        """
        Método principal para executar o bot.
        :param url: URL a ser acessada
        """
        try:
            self.acessar_site(url)
            self.executar_logica_bot()
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
