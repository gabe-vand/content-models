from dataclasses import dataclass
from openai import OpenAI

@dataclass
class openAI:
    """
    A wrapper for interacting with the OpenAI API using a specified model.
    
    Attributes:
        _client (OpenAI): The OpenAI client instance.
        _model (str): The model name to use for requests.
    """
    def __init__(self, model: str = "gpt-4.1"):
        """
        Initialize the openAI class with a model name.
        
        Args:
            model (str): The model name to use. Defaults to "gpt-4.1".
        """
        self._client = OpenAI()
        self._model = model

    def getResponse(self, request: str) -> str:
        """
        Get a response from the OpenAI model for a given request string.
        
        Args:
            request (str): The input string to send to the model.
        
        Returns:
            str: The response from the model as a string.
        """
        return str(self._client.responses.create(model = self._model, input=request))
    
    def changeModel(self, new_model: str) -> None:
        """
        Change the model used by the OpenAI client.
        
        Args:
            new_model (str): The new model name to use.
        """
        self._model = new_model

