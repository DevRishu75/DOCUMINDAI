from chromadb import PersistentClient


class VectorStore:
    def __init__(self):
      self.client = PersistentClient(path = 'database')
      self.collection = self.client.get_or_create_collection(name= "BoardIQ")
    def add_document(self,ids,documents,metadatas,embeddings):
        self.collection.add(
            ids = ids,documents = documents,metadatas = metadatas,embeddings = embeddings
        )
    def search(self,embeddings,top_k :int = 5):
        return self.collection.query(query_embeddings=[embeddings],
                                     n_results = top_k)
    def delete_document(self,document_id):
        self.collection.delete(
            where={
                'document_id': str(document_id)
            }
        )
    def count_document_chunk(self,document_id):
        results = self.collection.get(
            where={
                'document_id': str(document_id)
            }
        )
        include = []
        return len(results["ids"])