
# SeleniumBot - Template de Automação com Selenium

Este é um template de automação utilizando Selenium com Python. Ele foi projetado para ser simples, flexível e configurável para realizar ações em um site específico. O bot é executado em modo **headless**, o que significa que ele não abre uma interface gráfica, tornando-o ideal para execuções em servidores ou ambientes sem interface gráfica.

## Funcionalidades

- **Configuração automática do WebDriver:** Utiliza o `webdriver_manager` para gerenciar a instalação e atualização do ChromeDriver de forma automática.
- **Modo Headless:** O navegador é executado sem interface gráfica, ideal para execução em servidores.
- **Acesso e Interação com Sites:** O bot consegue acessar sites e interagir com elementos da página.
- **Tratamento de Erros:** Inclui tratamento básico de exceções como `NoSuchElementException` e `WebDriverException` para tornar o bot mais robusto.
- **Estrutura Extensível:** A lógica específica do bot pode ser facilmente inserida no método `executar_logica_bot`.

## Como Usar

### Pré-requisitos

1. **Python**: Certifique-se de ter o Python 3.x instalado em seu sistema.
2. **Bibliotecas Necessárias**: As dependências podem ser instaladas via `pip`.

```bash
pip install selenium webdriver-manager
```

### Executando o Bot

Para rodar o bot, siga as etapas abaixo:

1. Clone este repositório:

   ```bash
   git clone origin https://github.com/NarcisioTorquatto/selenium_bot_template.git
   cd selenium-bot
   ```

2. Execute o script Python:

   ```bash
   python bot.py
   ```

   O bot irá acessar o site configurado na variável `url` no método `run()`.

### Personalizando o Bot

1. Modifique o URL para o site que você deseja acessar, substituindo o valor em `bot.run("https://www.example.com")` no final do script.
2. Implemente a lógica específica do bot dentro do método `executar_logica_bot()`. Esse é o lugar onde você pode interagir com os elementos da página usando os métodos do Selenium (como `find_element`, `click`, `send_keys`, etc.).

## Estrutura do Código

- **SeleniumBot Class**: A classe principal que gerencia o WebDriver e a execução do bot.
  - **__init__**: Inicializa o WebDriver e configura as opções do Chrome.
  - **acessar_site**: Método para acessar um site específico.
  - **executar_logica_bot**: Implementação da lógica personalizada que você deseja que o bot execute.
  - **run**: Método principal que orquestra o funcionamento do bot.
  - **finalizar**: Encerra o WebDriver e limpa os recursos.

## Exemplos de Uso

1. **Acessando um site específico**:

   Se você quiser acessar um site diferente, basta alterar o URL dentro do método `run` para a URL do site desejado.

2. **Interagindo com elementos**:

   No método `executar_logica_bot()`, você pode usar a API do Selenium para interagir com elementos na página. Exemplo de como clicar em um botão:

   ```python
   def executar_logica_bot(self):
       try:
           botao = self.driver.find_element(By.ID, "id_do_botao")
           botao.click()
           print("Botão clicado com sucesso!")
       except NoSuchElementException as e:
           print(f"Erro ao encontrar o botão: {e}")
   ```

## Contribuição

Se você deseja contribuir para este projeto, sinta-se à vontade para enviar pull requests. Certifique-se de que seu código esteja bem testado e siga as boas práticas de Python.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
