import Services

__all__ = ['send_passkit']


base_Url = "https://extranet.avomark.fr/tools/creationPass.php"
headers = {"accept": "text/plain"}
queries = []
links = []

def send_passkit(path, new_File):
    queries = Services.FileProcessing.excel_to_queries(path)
    Urls = Services.Http.queries_to_urls(base_Url=base_Url, queries=queries)
    status = []

    for url in Urls:
        response = Services.Http.send_get(url=url, headers=headers)
        if "success" in response.keys():
            state = response["success"] == True
            Services.Log.info(msg=f" result success: {state}")
        else:
            state = False
            Services.Log.error(msg=f" result success: {state}")


        status.append(state)

    Services.FileProcessing.add_column_to_excel(path=path, column="status", values=status, new_File=new_File)


