from typing import List
from app.chunking.strategies import SplitterFactory

class Chunker:
      """
    Coordinates the chunking process.

    Responsibilities:
    - Get the appropriate splitting strategy.
    - Split cleaned text into chunks.
    - Return a list of chunks.
    """
      def __init__(self, strategy:str = "character"):
            self.splitter = SplitterFactory.get_splitter(strategy)
      def chunk(self,text:str)->List[str]:
            '''converted clean text into chunk'''
            return self.splitter.split(text)    