__all__ = ['queries_to_urls']

def queries_to_urls(base_Url, queries):
    urls = []
    for query in queries:
        urls.append(f"{base_Url}?{query}")

    return urls