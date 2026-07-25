from typing import List
from app.chunking.base import BaseSplit

class CharacterSplitter(BaseSplit):
    def __init__(self, chunk_size :int = 1000,overlap_chunk :int= 200):
        self.chunk_size = chunk_size
        self.overlap_chunk = overlap_chunk
    def split(self,text:str)->List[str]:
        chunks = []
        start = 0
        while start<len(text):
            end = start + self.chunk_size
            chunks.append(text[start:end])
            start +=self.chunk_size - self.overlap_chunk
        return chunks