import os
from search import search_prompt, PROMPT_TEMPLATE
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

for k in ("OPENAI_API_KEY", "PGVECTOR_URL", "PGVECTOR_COLLECTION"):
    if not os.getenv(k):
        raise RuntimeError(f"Variável de ambiente {k} não configurada")

def main():
    question = input("Escreva a sua pergunta: ")
    
    try:
        results = search_prompt(question)
        if not results:
            print("Não foi possível encontrar contexto relevante.")
            return

        context = "\n\n".join([doc.page_content for doc, score in results])
        
    except Exception as e:
        print(f"Erro na busca: {e}")
        return

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)

    chain = prompt | llm

    try:
        response = chain.invoke({
            "contexto": context,
            "pergunta": question
        })

        print(f"Resposta: {response.content}")
        
    except Exception as e:
        print(f"Erro ao gerar resposta: {e}")

if __name__ == "__main__":
    main()