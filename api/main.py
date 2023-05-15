from fastapi import FastAPI
from pydantic import *
from typing import List
import pandas
import uvicorn

app = FastAPI()



#a class to store our Dataset
class Dataset(BaseModel):
    id_ds = 0
    name = "test"
    dataframe: pandas.DataFrame = None
    class Config:
        arbitrary_types_allowed = True

Store_DF = []


#list the uploaded datasets
@app.get("/datasets/")
def datasets():
    ret = []
    for i in range(len(Store_DF)):
        ret.append(Store_DF[i].name)
    return ret

#@app.post("/datasets/")

#return the file name, and size of the dataset object
@app.get("/datasets/{id}/")
def name(id : int):
    for i in range(len(Store_DF)-1):
        if i.id_ds == id:
            return "{}.csv".format(i.name),i.dataframe.size

#delete the dataset object
@app.delete("/datasets/{id}")
def delete_ds(id : int):
    try:
        obj = Store_DF[id]
        Store_DF.pop(id)
        return obj
    except :
        raise HTTPException(status_code = 404, detail="Dataset not found")

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 3000)
