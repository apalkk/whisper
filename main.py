from fastapi import Form, File, UploadFile, Request, FastAPI
from typing import List
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import os
import webbrowser
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def jsonBinRead():
 url = 'https://api.jsonbin.io/v3/b/63b38cdfdfc68e59d576caed/latest?meta=false'
 headers = {
  'X-Master-Key': '$2b$10$2fEbQjOC/U05fN2qCBFLn.IbJKWeVNdMLCksJCPTI0o7M1MiPm9fO'
   }

 req = requests.get(url, json=None, headers=headers)
 return(req.text)

def jsonBinAdd(entry):
 url = 'https://api.jsonbin.io/v3/b/63b38cdfdfc68e59d576caed/latest?meta=false'
 headers = {
 'X-Master-Key': '$2b$10$2fEbQjOC/U05fN2qCBFLn.IbJKWeVNdMLCksJCPTI0o7M1MiPm9fO'
 }
 req = requests.get(url, json=None, headers=headers)
 txt = req.text
 data=json.loads(txt)
 url = 'https://api.jsonbin.io/v3/b/63b38cdfdfc68e59d576caed'
 headers = {
  'Content-Type': 'application/json',
  'X-Master-Key': '$2b$10$2fEbQjOC/U05fN2qCBFLn.IbJKWeVNdMLCksJCPTI0o7M1MiPm9fO'
 }
 data.append(entry)
 req = requests.put(url, json=data, headers=headers)


@app.post("/submit")
def submit(
    name: str = Form(...),
    id: int = Form(...),
    is_accepted: str = Form(...),
):   
    jsonBinAdd({id:{"name": name,"message": is_accepted}})
    return {
        "JSON Payload ": {"name": name, "id": id, "is_accepted": is_accepted},
    }


@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/superSecret/FindAll", response_class=HTMLResponse)
def main():
    print(jsonBinRead())


@app.get("/search/{id}")
def main(id:int):
    output_json = json.loads(jsonBinRead())
    key = str(id)
    for d in output_json:
         if key in d:
             yield (d[key]['message'] + " - "+d[key]['name'])

@app.get("/delete/{id}")
def main(id:int):
    output_json = json.loads(jsonBinRead())
    key = str(id)
    for d in output_json:
         if key in d:
             output_json.pop(d)
    url = 'https://api.jsonbin.io/v3/b/63b38cdfdfc68e59d576caed'
    headers = {
    'Content-Type': 'application/json',
    'X-Master-Key': '$2b$10$2fEbQjOC/U05fN2qCBFLn.IbJKWeVNdMLCksJCPTI0o7M1MiPm9fO'
    }
    req = requests.put(url, json=output_json, headers=headers)
    
    
