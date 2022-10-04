from fastapi import Form, File, UploadFile, Request, FastAPI
from typing import List
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")

with open('sample.json', mode='r', encoding='utf-8') as feedsjson:
        feeds = json.load(feedsjson)

f=open('sample.json')
output_file = open('sample.json').read()
output_json = json.loads(output_file)

@app.post("/submit")
def submit(
    name: str = Form(...),
    point: float = Form(...),
    is_accepted: str = Form(...),
    #files: List[UploadFile] = File(...)
):   
    with open('sample.json', mode='w', encoding='utf-8') as feedsjson:
     entry = {point:{"name": name,"message": is_accepted}}
     feeds.append(entry)
     json.dump(feeds, feedsjson)
    #with open('sample.json', 'w') as f:
         #dict1 ={point:{"name": name,"message": is_accepted}}
         #json.dump(dict1, f, indent=6)
    return {
        "JSON Payload ": {"name": name, "point": point, "is_accepted": is_accepted},
        #"Filenames": [file.filename for file in files],
    }


@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/all", response_class=HTMLResponse)
def main():
    a_file = open("sample.json", "r")
    a_json = json.load(a_file)
    pretty_json = json.dumps(a_json, indent=4)
    a_file.close()
    return(pretty_json)


@app.get("/search/{id}")
def main(id:float):
    key = str(id)
    for d in output_json:
        if key in d:
            return d[key]['message'], d[key]['name']

@app.get("/delete")
def main():
    with open("sample.json", "w") as outfile:
     json.dump({}, outfile)