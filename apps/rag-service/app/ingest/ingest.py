import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
from llama_index.vector_stores.postgres import PGVectorStore
from app.db import engine

def ingest(path: str):
    docs = SimpleDirectoryReader(path).load_data()

    vector_store = PGVectorStore.from_params(
        database=engine.url.database,
        host=engine.url.host,
        password=engine.url.password,
        port=engine.url.port,
        user=engine.url.username,
        table_name=os.getenv("VEC_TABLE", "rag_chunks"),
        embed_dim=int(os.getenv("EMBED_DIM", "1536")),
    )

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    VectorStoreIndex.from_documents(docs, storage_context=storage_context)

    return {"status": "ok", "docs_indexed": len(docs)}
