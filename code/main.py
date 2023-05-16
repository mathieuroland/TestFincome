import typer
import api
from fastapi import FastAPI, File, UploadFile
import pandas
import uvicorn


Store_DF = []

app = typer.Typer()

@app.command()
def get_all():
    return api.datasets(Store_DF)

#@app.command()
#def add(file : File):
#    return api.upload_file(file,Store_DF)

@app.command()
def get_one(id : int):
    return api.name(id, Store_DF)

@app.command()
def delete(id: int):
    return api.delete_ds(id,Store_DF)

@app.command()
def excel(id: int):
    return api.df_to_excel(id,Store_DF)

@app.command()
def stat(id: int):
    return api.stats(id,Store_DF)

@app.command()
def plot(id: int):
    return api.get_hist(id,Store_DF)

if __name__ == '__main__':
    uvicorn.run(app, host = "127.0.0.1", port = 3000)

