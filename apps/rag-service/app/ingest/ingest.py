from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

def ingest(path: str):
    docs = SimpleDirectoryReader(path).load_data()
    index = VectorStoreIndex.from_documents(docs)
    index.storage_context.persist()
