import Services
import Tools
import pandas as pd
import math

__all__ = ['excel_to_queries', 'add_column_to_excel']

Fields = {
    "carte" : "Numero Carte",
    "nl" : "NL",
    "pdv" : "pdv ",
    "email" : " Email",
    "tel" : "N°de Tel",
    "code_pays" : "code pays"
}

def excel_to_queries(path):
    queries = []

    # convert excel into dataframe
    df = pd.read_excel(path)

    # convert dataframe into dictionary
    dict = df.to_dict()

    for carte, nl, pdv, email, tel, code_pays in zip(dict[Fields["carte"]].values(), dict[Fields["nl"]].values(), dict[Fields["pdv"]].values(), dict[Fields["email"]].values(), dict[Fields["tel"]].values(), dict[Fields["code_pays"]].values()):

        if "+" in str(code_pays):
            code = code_pays.split("+")[0]
            code_pays = f"+{int(code)}"
        else:
            if not math.isnan(code_pays):
                code = int(code_pays)
                code_pays = f"+{code}"
            else:
                code_pays = ""

        if math.isnan(tel):
            tel = ""
        else:
            tel = int(tel)

        if nl :
            query = f"numeroCarte={str(carte).strip()}&pdvSoldeFss={str(pdv).strip()}&mobile={str(code_pays).strip()}{str(tel).strip()}&email={str(email).strip()}"
        else:
            query = f"numeroCarte={str(carte).strip()}&pdvSoldeFss={str(pdv).strip()}&mobile={str(code_pays).strip()}{str(tel).strip()}&email={str(email).strip()}"

        queries.append(query)

    return queries


def add_column_to_excel(path, column, values, new_File):
    # convert excel into dataframe
    df = pd.read_excel(path)

    # convert dataframe into dictionary
    dict = df.to_dict()

    # add column and values
    dict[column] = Tools.ListToDict.list_to_dict(values)
    print(dict)
    # columns
    columns = list(dict.keys()) + [column]

    # convert dict to dataframe
    df = pd.DataFrame(dict, columns=columns)
    try:
        # convert dataframe to excel
        df.to_excel(new_File)
        Services.Log.info(f"file {new_File} was generated successfully")
    except PermissionError:
        Services.Log.error(f"Permission denied on file {new_File}")


