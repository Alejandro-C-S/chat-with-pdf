# 📄 Chat con PDFs usando Flask + RAG + Ollama

Un asistente inteligente que permite cargar documentos PDF y realizar preguntas sobre su contenido utilizando la técnica **Retrieval-Augmented Generation (RAG)**.

El proyecto procesa el documento, genera embeddings locales, almacena la información en una base vectorial FAISS y utiliza un modelo de lenguaje ejecutado localmente con Ollama para responder preguntas sin necesidad de servicios de IA en la nube.

---

## 🚀 Características

* 📄 Carga de documentos PDF.
* ✂️ División automática del texto en fragmentos (chunks).
* 🧠 Embeddings locales con Sentence Transformers.
* 📚 Base vectorial FAISS.
* 🤖 Modelo de lenguaje local mediante Ollama.
* 💬 Chat interactivo sobre el contenido del documento.
* 🔒 No requiere conexión a servicios de IA de pago.

---

## 🛠️ Tecnologías utilizadas

* Python 3.12
* Flask
* LangChain
* Ollama
* Llama 3.1
* FAISS
* Hugging Face Sentence Transformers
* PyPDF
* HTML
* CSS
* JavaScript

---

## 📂 Estructura del proyecto

```text
chat-pdf/
│
├── app/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   ├── __init__.py
│   ├── rag.py
│   └── routes.py
│
├── uploads/
├── vectorstore/
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Alejandro-C-S/chat-with-pdf.git
cd chat-pdf
```

---

### 2. Crear un entorno virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🤖 Instalar Ollama

### macOS

```bash
brew install ollama
```

### Windows

Descargar desde:

https://ollama.com/download

---

## Descargar el modelo

```bash
ollama pull llama3.1
```

Verificar modelos instalados:

```bash
ollama list
```

---

## Ejecutar Ollama

```bash
ollama serve
```

---

## Ejecutar la aplicación

```bash
python run.py
```

Abrir en el navegador:

```
http://127.0.0.1:5000
```

---

## 📖 Uso

1. Abrir la aplicación.
2. Cargar un documento PDF.
3. Esperar a que se procese.
4. Escribir una pregunta relacionada con el contenido.
5. Recibir una respuesta basada únicamente en la información del documento.

---

## 🧠 Arquitectura

```text
               PDF
                │
                ▼
     Extracción de texto
                │
                ▼
       División en chunks
                │
                ▼
Sentence Transformers
      (Embeddings)
                │
                ▼
             FAISS
                │
                ▼
 Recuperación de contexto
                │
                ▼
        Ollama (Llama 3.1)
                │
                ▼
      Respuesta al usuario
```

---

## 📸 Capturas

Se recomienda agregar capturas como:

```
docs/images/home.png

docs/images/upload.png

docs/images/chat.png
```

---

## 🔮 Mejoras futuras

* Historial de conversaciones.
* Soporte para múltiples documentos.
* Streaming de respuestas.
* Autenticación de usuarios.
* Docker y Docker Compose.
* Persistencia de conversaciones.
* Respuestas con referencias a la página del PDF.
* Interfaz tipo ChatGPT.

---

## 👨‍💻 Autor

**Alejandro de la Cruz de los Santos**

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT.
