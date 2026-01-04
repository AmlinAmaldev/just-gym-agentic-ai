from langchain_tavily import TavilySearch

search = TavilySearch(max_results=3)

def research(query):
    return search.run(query)
