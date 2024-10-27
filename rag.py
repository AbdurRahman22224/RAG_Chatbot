from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader, PyMuPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain.indexes import SQLRecordManager, index
from pathlib import Path

# Function to load, split, and retrieve documents
def load_and_retrieve_docs(path: str):

    docs = [] 
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1024, chunk_overlap = 50)
    path = Path(path)
    for pdf in path.glob("*.pdf"):
        loader = PyMuPDFLoader(str(pdf))
        documents = loader.load()
        docs += text_splitter.split_documents(documents)
        
    embeddings = OllamaEmbeddings(model = 'nomic-embed-text')
    doc_search = Chroma.from_documents(docs, embeddings)


    # namespace = "chromadb/my_documents"
    # record_manager = SQLRecordManager(
    #     namespace, db_url="sqlite:///record_manager_cache.sql"
    # )
    # record_manager.create_schema()

    # index_result = index(
    #     docs,
    #     record_manager,
    #     doc_search,
    #     cleanup = "incremental",
    #     source_id_key = "source",
    # )

    # print(f"Indexing stats: {index_result}")

    return doc_search


# Function to format documents
def format_docs(docs : list):
    return "\n\n".join(doc.page_content for doc in docs)



 

