from typing import List
from app.chunking.base import BaseSplitter

class CharacterSplitter(BaseSplitter):
    def __init__(self,chunk_size:int =1000, chunk_overlap:int= 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
    def split(self, text:str)->List[str]:
        chunks = []
        start = 0
        while start<len(text):
               end = start + self.chunk_size
               chunks.append(text[start:end])
               start += self.chunk_size - self.chunk_overlap

          

        