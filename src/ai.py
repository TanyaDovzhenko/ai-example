import os
import nltk
import utils
import prompts
from dotenv import load_dotenv
from simpleaichat import AIChat
from llama_index import StorageContext, load_index_from_storage
from nltk.tokenize import word_tokenize

nltk.download('punkt')
load_dotenv()

MAX_CONTEXT_TOKENS = 6000
STORAGE_PATH = './storage'
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def sendAiRequest(query_str): 
  if not query_str: return '' 
  if not os.path.isdir(STORAGE_PATH): utils.createStorage()
  
  ai = AIChat(api_key=OPENAI_API_KEY, console=False, model="gpt-3.5-turbo-16k")
  storage_context = StorageContext.from_defaults(persist_dir=STORAGE_PATH)
  index = load_index_from_storage(storage_context)
  
  sub_queries = ai(prompts.MULTIPLE_QUERY_GEN_PROMPT(3, query_str), output_schema=utils.GET_SUB_QUERIES_EVENT_METADATA)  
  retriever = index.as_retriever(similarity_top_k=2)
  retrieved_nodes = {}

  for q in sub_queries:
    if not sub_queries[q]: continue
    nodes = retriever.retrieve(sub_queries[q])
    for node in nodes:
      retrieved_nodes[node.node_id] = node
    
  context_str = ''
  for node in list(retrieved_nodes.values()):
    context_str_tokens = word_tokenize(context_str)
    node_tokens = word_tokenize(node.text)
    sum_tokens_len = len(context_str_tokens) + len(node_tokens)
  
    if(sum_tokens_len <= MAX_CONTEXT_TOKENS):
      context_str += node.text
    else:
      replace_tokens_num = sum_tokens_len - MAX_CONTEXT_TOKENS
      del node_tokens[-replace_tokens_num:]
      shorter_node_text = " ".join(node_tokens) 
      context_str += shorter_node_text
      break
      
  response = ai(prompts.MAIN_QUERY_PROMPT(context_str, query_str))
  return response
