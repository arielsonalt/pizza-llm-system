from langgraph.graph import StateGraph, END
from app.graph.nodes import answer, router

graph_builder = StateGraph(dict)

graph_builder.add_node("router", router)
graph_builder.add_node("answer", answer)

graph_builder.set_entry_point("router")

graph_builder.add_edge("router", "answer")
graph_builder.add_edge("answer", END)  # <- ESSENCIAL

graph = graph_builder.compile()
