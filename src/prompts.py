def MULTIPLE_QUERY_GEN_PROMPT(num_queries, query_str):
  return (
    "You are a helpful assistant that generates sub-questions to make it easier to answer the main question."
    "We have provided main question below. \n"
    "Question: {query_str}\n"
    "Generete {num_queries} sub-questions for this question without duplicates.\n"
    "Return questions one on each line.\n"
    .format(num_queries=num_queries, query_str=query_str)
  )

def MAIN_QUERY_PROMPT(context_str, query_str):
  return (
    "We have provided context information below. \n"
    "Context:\n"
    "{context_str}"
    "\n---------------------\n"
    "Given only this information, please answer the question: {query_str}\n"
    .format(context_str=context_str, query_str=query_str)
  )
