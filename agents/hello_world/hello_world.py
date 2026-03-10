from typing import Dict, TypedDict
from langgraph.graph import StateGraph

# We create an AgentState - shared data structure that keeps track of information as your application runs.
class AgentState(TypedDict):
    message: str
    
# Define a node
def greeting_node(state: AgentState) -> AgentState:
    """
    A simple node that adds a greeting message to the state.
    """
    state['message'] = "Hey " + state['message'] + ", how is it going?"
    return state

# Build the graph
graph = StateGraph(AgentState)
graph.add_node("greeting", greeting_node)
graph.set_entry_point("greeting")
graph.set_finish_point("greeting")

# Compile the graph
app = graph.compile()

# Visualize the graph
png_data = app.get_graph().draw_mermaid_png()
with open("agents/hello_world/hello_world_graph.png", "wb") as f:
    f.write(png_data)
    
# Run the application
result = app.invoke({"message": "Jose"})

print(result['message'])