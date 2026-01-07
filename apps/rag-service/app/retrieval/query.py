from llama_index.core import StorageContext, load_index_from_storage

storage = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage)

def query_index(q: str):
    engine = index.as_query_engine()
    return {"answer": engine.query(q).response}
