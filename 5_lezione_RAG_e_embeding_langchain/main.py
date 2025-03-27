# Importiamo le librerie necessarie
from langchain_community.llms import Ollama  # Per interagire con il modello LLM
from langchain_community.document_loaders import (
    TextLoader,
)  # Per caricare file di testo
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)  # Per dividere il testo
from langchain_community.embeddings import (
    OllamaEmbeddings,
)  # Per generare gli embedding
from langchain_chroma import Chroma  # Database vettoriale
from langchain_core.prompts import ChatPromptTemplate  # Per creare il prompt
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import os

MODEL_NAME = "gemma3:12b"
BASE_URL = "https://6235-34-124-202-167.ngrok-free.app/"

# Configurazione del modello LLM
model = Ollama(
    base_url=BASE_URL,  # URL del server Ollama locale
    model=MODEL_NAME,  # Modello da utilizzare
    verbose=False,
)

# Caricamento del documento di testo
loader = TextLoader("./dati/ReEric.txt")  # Sostituire con il path del vostro file
documents = loader.load()

# Divisione del testo in chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # Dimensione di ogni chunk in caratteri
    chunk_overlap=200,  # Sovrapposizione tra chunks per mantenere il contesto
)
splits = text_splitter.split_documents(documents)

# Configurazione degli embeddings
embeddings = OllamaEmbeddings(
    base_url=BASE_URL,
    model=MODEL_NAME,
)

# Creazione del database vettoriale persistente
persist_directory = "db_vectoriale"  # Directory dove salvare il database

# Creazione o caricamento del database vettoriale
if not os.path.exists(persist_directory):
    # Prima esecuzione: creiamo il database
    vectorstore = Chroma.from_documents(
        documents=splits, embedding=embeddings, persist_directory=persist_directory
    )
    # vectorstore.persist()  # Salviamo il database su disco
else:
    # Esecuzioni successive: carichiamo il database esistente
    vectorstore = Chroma(
        persist_directory=persist_directory, embedding_function=embeddings
    )

# Creazione del retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",  # Ricerca per similarità
    search_kwargs={"k": 2},  # Numero di documenti da recuperare
)

# Definizione del template per il prompt
template = """Rispondi alla domanda utilizzando SOLO le informazioni fornite nel contesto.
Se le informazioni nel contesto non sono sufficienti per rispondere,
rispondi: "Mi dispiace, non ho abbastanza informazioni per rispondere a questa domanda."
Contesto:
{context}
Domanda: {question}
"""

# Creazione del prompt
prompt = ChatPromptTemplate.from_template(template)


# Funzione per formattare i documenti recuperati
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# Creazione della catena RAG
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)


# Funzione per interrogare il RAG
def query_rag(question: str) -> str:
    """
    Interroga il sistema RAG con una domanda.
    Args:
        question (str): La domanda da porre al sistema
    Returns:
        str: La risposta del sistema
    """
    return rag_chain.invoke(question)


# Esempio di utilizzo
if __name__ == "__main__":
    while True:
        question = input("\nFai una domanda (o scrivi 'exit' per uscire): ")
        if question.lower() == "exit":
            break
        print("\nRisposta:", query_rag(question))
