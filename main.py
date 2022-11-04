from fastapi import Form, File, UploadFile, Request, FastAPI
from typing import List
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import os
import webbrowser

app = FastAPI()
templates = Jinja2Templates(directory="templates")


f=open('sample.json')

@app.post("/submit")
def submit(
    name: str = Form(...),
    id: int = Form(...),
    is_accepted: str = Form(...),
    #files: List[UploadFile] = File(...) # Dead File Uploader
):   
    #key = str(id)
    #for d in f:
        #if key in d:
            #webbrowser.open('file://' + os.path.realpath('invalid.html')) #Not working ??
            #return("Key Has Aldready Been Taken")
            
    with open('sample.json', mode='r+', encoding='utf-8') as feedsjson:
     feeds = json.load(feedsjson)
     entry = {id:{"name": name,"message": is_accepted}}
     feeds.append(entry)
     json.dump(feeds, feedsjson)
    #with open('sample.json', 'w') as f:
         #dict1 ={point:{"name": name,"message": is_accepted}}
         #json.dump(dict1, f, indent=6)
    return {
        "JSON Payload ": {"name": name, "id": id, "is_accepted": is_accepted},
        #"Filenames": [file.filename for file in files],
    }


@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/superSecret/FindAll", response_class=HTMLResponse)
def main():
    a_file = open("sample.json", "r")
    a_json = json.load(a_file)
    pretty_json = json.dumps(a_json, indent=4)
    a_file.close()
    return(pretty_json)


@app.get("/search/{id}")
def main(id:int):
    output_file = open('sample.json').read()
    output_json = json.loads(output_file)
    key = str(id)
    for d in output_json:
         if key in d:
             yield (d[key]['message'] + " - "+d[key]['name'])


def search(key:str):
    output_file = open('sample.json').read()
    output_json = json.loads(output_file)
    for d in output_json:
        if key in d:
            yield d[key]['message'] + " - "+d[key]['name']
        else: return("End")
    #search(key) #Recursive search deprecated
    

@app.get("/superSecret/DeleteAll")
def main():
    with open("sample.json", "w") as killfile:
     json.dump({}, killfile)

@app.get("/delete/{id}")
def main(id:int):
    id = str(id)
    file_name = 'example.json'
    with open('sample.json', 'r', encoding='utf-8') as f:
     my_list = json.load(f)
     output_file = open('sample.json').read()
     output_json = json.loads(output_file)
     key = str(id)
     for d in output_json:
         if key in d:
             my_list.pop(d[key])
     new_file_name = 'sample.json'
     with open(new_file_name, 'w', encoding='utf-8') as f:
         f.write(json.dumps(my_list, indent=2))
    