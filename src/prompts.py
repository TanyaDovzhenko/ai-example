def MULTIPLE_QUERY_GEN_PROMPT(num_queries, query_str):
  return (
    "You are a helpful assistant that generates multiple small sub-questions based on a single question."
    "We have provided question below. \n"
    "{query_str}\n"
    "Generete {num_queries} sub-questions for this question.\n"
    "Return them one on each line.\n"
    .format(num_queries=num_queries, query_str=query_str)
  )

def MAIN_QUERY_PROMPT(context_str, query_str):
  return (
    "We have provided context information below. \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Given this information, please answer the question in as much detail as possible: {query_str}\n"
    .format(context_str=context_str, query_str=query_str)
  )
