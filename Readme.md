
# RAG Chatbot with LangChain, Ollama, ChromaDB, and Chainlit

This project is a Retrieval-Augmented Generation (RAG) chatbot that combines the capabilities of LangChain, Ollama, ChromaDB, and Chainlit. The goal is to build a robust chatbot capable of retrieving relevant documents and generating coherent responses based on the documents' content.

## Features
- **Retrieval-Augmented Generation (RAG)** for improved contextual responses.
- **Document embedding and retrieval** with ChromaDB.
- **Large Language Model (LLM)** integration using Ollama.
- **User interface** for chatbot interactions using Chainlit.

## Getting Started

### Prerequisites

Make sure you have the following installed:
- Python 3.9 or higher
- [Ollama](https://ollama.com/) installed locally and start the server


### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/AbdurRahman22224/RAG_Chatbot.git
   cd [folder name]
   ```

2. **Create a Virtual Environment** Optional

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```


### Usage

1. **Run Ollama Server** if it's not running already:

   ```bash
   ollama pull llama3
   ```

   ```bash
   ollama pull [embedding_name]
   ```

2. **Start the Chainlit Server**
   ```bash
   chainlit run app.py -w
   ```
   
### Project Structure

```plaintext
.
├── README.md                   # Project README file
├── app.py                      # Main application file for Chainlit server
├── rag.py                      # Functions for loading, retrieving and formating
├── pdf                         # For pdfs
├── requirements.txt            # Python dependencies
```
---
Dont want to show sources while giving the response change show_sources to False in app.py
