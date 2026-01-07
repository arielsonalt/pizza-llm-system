from langgraph.graph import StateGraph
from app.graph.nodes import classify, answer

graph_builder = StateGraph(dict)
graph_builder.add_node("classify", classify)
graph_builder.add_node("answer", answer)

graph_builder.set_entry_point("classify")
graph_builder.add_edge("classify", "answer")
graph = graph_builder.compile()
