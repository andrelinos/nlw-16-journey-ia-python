<img src=".github/image.png" alt="NLW-16 - Journey - IA" />

```markdown
# Travel Agent Chatbot

Este projeto é um chatbot desenvolvido para uma agência de viagens, capaz de gerar roteiros de viagem detalhados e personalizados. Utiliza várias bibliotecas de IA para pesquisa na web, carregamento de documentos e recuperação de informações relevantes.

## Funcionalidades

- Pesquisa de eventos e informações na web usando ferramentas como DuckDuckGo Search e Wikipedia.
- Carregamento e processamento de documentos da web.
- Criação de um agente supervisor para gerar roteiros de viagem detalhados usando contexto da web e documentos relevantes.
- Integração com AWS Lambda para execução do chatbot.

## Requisitos

- Python 3.12
- Pacotes listados em `requirements.txt`

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/travel-agent-chatbot.git
    cd travel-agent-chatbot
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```sh
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. Configure as variáveis de ambiente no arquivo `.env`:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    USER_AGENT=your_user_agent
    ```

## Uso

### Pesquisar na Web

A função `researchAgent` realiza uma pesquisa na web usando as ferramentas configuradas:

```python
query = "Vou viajar para Londres em agosto de 2024. Quero que faça um roteiro de viagem para mim com os eventos que irão ocorrer na data da viagem e com o preço da passagem de São Paulo para Londres."
result = researchAgent(query, llm)
print(result)
```

### Carregar Dados da Web

A função `loadData` carrega e processa documentos de URLs específicas:

```python
retriever = loadData()
```

### Obter Documentos Relevantes

A função `getRelevantDocs` obtém documentos relevantes para uma consulta específica:

```python
query = "Eventos em Londres em agosto de 2024"
documents = getRelevantDocs(query)
print(documents)
```

### Agente Supervisor

A função `supervisorAgent` cria um roteiro de viagem detalhado usando contexto da web, documentos relevantes e a entrada do usuário:

```python
response = supervisorAgent(query, llm, webContext, relevant_documents)
print(response)
```

### Função Lambda

A função `lambda_handler` integra o chatbot com AWS Lambda:

```python
def lambda_handler(event, context):
    query = event.get('question')
    response = getResponse(query, llm).context
    return {'body': response, 'status': 200}
```

## Estrutura do Projeto

```
.
├── Dockerfile
├── README.md
├── requirements.txt
├── .env
└── travelAgent.py
```

## Contribuições

Sinta-se à vontade para abrir issues e enviar pull requests. Todas as contribuições são bem-vindas!

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

```

Esse `README.md` simples fornece uma visão geral completa do projeto, incluindo funcionalidades, instalação, uso e estrutura do projeto.
