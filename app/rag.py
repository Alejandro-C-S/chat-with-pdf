from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings

# Modelo de lenguaje (Ollama)
llm = ChatOllama(
    model="llama3.1",
    temperature=0
)

# Modelo de embeddings (local)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def split_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=200
    )
    return splitter.split_text(text)


def create_vectorstore(chunks):
    db = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    db.save_local("vectorstore")


def load_vectorstore():
    return FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )


def search_documents(question):
    db = load_vectorstore()
    return db.similarity_search(question, k=10)


def ask_pdf(question):
    docs = search_documents(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
Eres un asistente que responde únicamente usando el contexto.

Si la respuesta no está en el contexto responde:

"No encontré esa información en el PDF."

Contexto:

{context}

Pregunta:

{question}
"""

    response = llm.invoke(prompt)

    return response.content