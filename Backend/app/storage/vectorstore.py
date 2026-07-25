from chromadb import PersistentClient

class VectorStore:
    def __init__(self):
      self.client = PersistentClient(path = 'database')
      self.collection = self.client.get_or_create_collection(name= "BoardIQ")
    def add_document(self,ids,documents,metadatas,embeddings):
        self.collection.add(
            ids = ids,documents = documents,metadatas = metadatas,embeddings = embeddings
        )
    def search(self):
        pass
    def delete_document():
        pass   