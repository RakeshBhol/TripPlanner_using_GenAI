import os
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field

from utils.config_loader import load_config
from langchain_qroq import ChatGroq
from langchain_openai import ChatOpenAI


class ConfigLoader:
    def __init__(self):
        print("Loading config.....")
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key]


class ModelLoader:    
    model_provider: Literal["qroq","openai"] = "qroq"  # Class Variable
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)  # Class Variable

    def model_post_init(self, __context: Any) -> None:
        self.config = ConfigLoader()
    
    class Config:
        arbitary_types_allowed = True  #class variable
    
    def load_llm(self):
        """
        load and retun the LLM model
        """
        print("LLM Loading....")
        print(f"Loading model from provider: {self.model_provider}")
        if self.model_provider == "qroq":
            print("Loading LLM from Groq...........")
            groq_api_key = os.getenv("GROQ_API_KEY")  # Load from .env
            model_name = self.config["llm"]["qroq"]["model_name"]  # Load from yaml
            llm = ChatGroq(model=model_name, api_key=groq_api_key)
        elif self.model_provider == "openai":
            print("Loading LLM from OpenAI...........")
            openai_api_key = os.getenv("OPENAI_API_KEY")  # Load from .env
            model_name = self.config["llm"]["openai"]["model_name"]  # Load from yaml
            llm = ChatOpenAI(model_name=model_name, api_key=openai_api_key)
        
        return llm