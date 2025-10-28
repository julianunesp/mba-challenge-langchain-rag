## Configuração do Ambiente

Para configurar o ambiente e instalar as dependências do projeto, siga os passos abaixo:

1. **Criar e ativar um ambiente virtual (`venv`):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

2. **Instalar as dependências:**

   **Opção A - A partir do `requirements.txt`:**
   ```bash
   pip install -r requirements.txt
   ```

   **Opção B - Instalação direta dos pacotes principais:**
   ```bash
   pip install langchain langchain-openai langchain-google-genai langchain-community langchain-text-splitters langchain-postgres psycopg python-dotenv beautifulsoup4 pypdf && pip freeze > requirements.txt
   ```
   Este comando também instalará todas as dependências automaticamente e gerará o arquivo `requirements.txt`.

3. **Configurar as variáveis de ambiente:**

   - Duplique o arquivo `.env.example` e renomeie para `.env`
   - Abra o arquivo `.env` e substitua os valores pelas suas chaves de API reais obtidas conforme instruções abaixo

## Execução do projeto

1. Subindo o banco de dados
   ```bash
   docker-compose up -d
   ```

2. Ingestão do pdf no DB
   ```bash
   python3 src/ingest.py
   ```

3. Executando pesquisa (e pergunta)
   ```bash
   python3 src/chat.py
   ```

## Resultado esperado:

   __(venv) jpedrosa@BR000FPWDXN4N9L 6-mba-challenge % python3 src/chat.py__

   Escreva a sua pergunta: Qual o faturamento da Empresa Azul Eventos LTDA? E em qual ano?
   Resposta: O faturamento da Empresa Azul Eventos LTDA é de R$ 420.897.381,89 e o ano é 1959.

   __(venv) jpedrosa@BR000FPWDXN4N9L 6-mba-challenge % python3 src/chat.py__

   Escreva a sua pergunta: Quantos clientes temos em 2024?
   Resposta: Não tenho informações necessárias para responder sua pergunta.