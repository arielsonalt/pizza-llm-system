import os
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.postgres import PGVectorStore
from app.db import engine

def _index() -> VectorStoreIndex:
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
    return VectorStoreIndex.from_vector_store(vector_store=vector_store, storage_context=storage_context)

def query_index(q: str):
    index = _index()
    engine_q = index.as_query_engine(similarity_top_k=5)
    r = engine_q.query(q)
    return {"answer": str(r), "sources": getattr(r, "source_nodes", None)}
