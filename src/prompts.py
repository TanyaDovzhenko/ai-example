def MULTIPLE_QUERY_GEN_PROMPT(num_queries, query_str):
  return (
    "You are a helpful assistant that generates multiple search queries based on a "
    "single input query. Generate {num_queries} search queries, one on each line, "
    "related to the following input query:\n"
    "Query: {query_str}\n"
    "Queries:\n"
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
