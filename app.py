from fastapi import FastAPI
from pydantic import BaseModel
from Agent.agentic_workflow import GraphBuilder

app = FastAPI()

app.get("/query")

class QueryRequest(BaseModel):
    query: str
async def query_travel_agent(query: QueryRequest):
    try:
        print(query)
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()
        # react_app = graph.build_graph()

        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png","wb") as f:
            f.write(png_graph)