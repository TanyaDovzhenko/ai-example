from pydantic import BaseModel, Field
from llama_index import SimpleDirectoryReader, VectorStoreIndex, ServiceContext

def createStorage():
  documents = SimpleDirectoryReader('data').load_data()
  service_context = ServiceContext.from_defaults(chunk_size=1000)
  index = VectorStoreIndex.from_documents(documents, service_context=service_context)
  index.storage_context.persist(persist_dir='./storage')
  
class GET_SUB_QUERIES_EVENT_METADATA(BaseModel):
    """Event information"""
    sub_query_1: str = Field(description="Text of first sub-question")
    sub_query_2: str = Field(description="Text of second sub-question")
    sub_query_3: str = Field(description="Text of third sub-question")
    sub_query_4: str = Field(description="Text of fourth sub-question")
    sub_query_5: str = Field(description="Text of fifth sub-question")