"""
Build graph from where to start and end the Agentic AI
"""

from utils.model_loaders import ModelLoader  # Calls llm and return data
from Tools.weather_info_tool import WeatherInfoTool
from Tools.place_search_tool import PlaceSearchTool
from Tools.calculator_tool import CalculatorTool
from Tools.currency_conversion_tool import CurrencyConverterTool

from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuild import ToolNode, tools_condition

class GraphBuilder():
    def __init__(self):
        self.tools = [
            WeatherInfoTool(),
            PlaceSearchTool(),
            CurrencyConverterTool(),
            CalculatorTool()
        ]
        self.system_prompt = SYSTEM_PROMPT

    def agent_function(self, state: MessagesState):
        """Agent will make a decision and return in the form of a state to StateGraph (in the form of messages)"""
        user_question = state["messages"]
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {'messages': [response]}


    def build_graph(self):
        graph_builder = StateGraph(MessagesState)  # Store State (list of messages) of each step/LLM

        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools". ToolNode(tools=self.tools))
        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edges("agent",tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent",END)

        # To create graph we need to compile as below
        self.graph = graph_builder.compile()
        return self.graph
        
    def __call__(self, *args, **kwds):
        return self.build_graph()
