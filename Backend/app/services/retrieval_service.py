from app.services.embedding_service import EmbeddingService
from app.storage.vectorstore import VectorStore
class RetrievalService:
    ''' WE will take the text from user and use embeddings ''' 
    def __init__(self):
        self.embed_service = EmbeddingService()
        self.vector_search = VectorStore()

    def retrieve(self,question:str)->str:
        embeddings = self.embed_service.embed_text(question)
        Retreived_chunks = self.vector_search.search(embeddings)
        return Retreived_chunks