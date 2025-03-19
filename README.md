
# Automação de Login no SimBrief com Google Authenticator

Este projeto automatiza o login no SimBrief utilizando o Selenium WebDriver com Python. A automação inclui a integração com a autenticação via Google, incluindo a captura do código do Google Authenticator via WhatsApp, utilizando a API do Twilio.

## Funcionalidades

- Acessa o site SimBrief automaticamente.
- Realiza login usando sua conta do Google.
- Solicita e captura o código do Google Authenticator automaticamente via WhatsApp.
- Preenche o código no campo correspondente e continua o processo de login.

## Tecnologias Usadas

- Python
- Selenium WebDriver
- PyWhatKit (para integração com WhatsApp)
- Twilio API (para leitura automática de mensagens do WhatsApp)

## Requisitos

Para rodar este projeto, você precisará das seguintes dependências:

- Python 3.x
- Selenium
- pywhatkit
- Twilio (caso deseje usar a automação do código via WhatsApp)
- WebDriver do Chrome

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd seu_repositorio
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o seu WebDriver do Chrome. O projeto foi testado com o [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/).

## Configuração da Twilio API (se necessário)

1. Crie uma conta no Twilio: [https://www.twilio.com/](https://www.twilio.com/).
2. Configure um número de WhatsApp para a API do Twilio.
3. Adicione suas credenciais no arquivo de configuração do Twilio.

## Como Usar

1. Execute o script de automação:
   ```bash
   python automacao_simbrief.py
   ```

2. A automação irá solicitar que você insira o código do Google Authenticator enviado por WhatsApp.
3. O código será inserido automaticamente no campo correto no SimBrief.

## Contribuições

Sinta-se à vontade para contribuir para este projeto! Se você encontrar algum problema ou desejar adicionar novas funcionalidades, por favor, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
