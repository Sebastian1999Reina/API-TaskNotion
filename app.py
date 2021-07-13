import requests ,json

token = 'secret_pIqDsfSIx4rWqucnCMY3PoDz6DxWYWkd8FpniQW34VD'
databaseID = '3574f42993fa4efe90f5e4c7f7c2c112'

headers = {
    "Authorization":   token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}
def leerTareas(databaseID,headers):
    readUrl= f"https://api.notion.com/v1/databases/{databaseID}/query"

    res = requests.request("POST",readUrl,headers=headers)
    data= res.json()
    print(res.status_code)
    #print(res.text)

    with open('./db.json','w',encoding='utf8') as f:
        json.dump(data,f,ensure_ascii=False)

def dezplazarTarea():
    pass

def tareaCompletada(pageId,headers):
    updateUrl= f"https://api.notion.com/v1/pages/{pageId}"
    updateData = {
        "properties": {
            "Check": {"checkbox": True}
        }
    }
    data=json.dumps(updateData)

    response = requests.request("PATCH",updateUrl,headers=headers,data=data)
    print(response.status_code)
    print(response.text)



#leerTareas(databaseID,headers)

#pageId="7ccdf40a-114b-47dd-a3ec-13ff0bcd9103"
#tareaCompletada(pageId,headers)