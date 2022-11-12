from fastapi import FastAPI, Form, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import validators
import random
import uvicorn

app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/main", StaticFiles(directory=r"C:\Users\Administrator\Desktop\url-shortener\main"))

links = {}

dictionary = 'abcdefghiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def mk_string():
    global dictionary
    s = ''
    for i in range(0,5):
        s = s + dictionary[random.randint(0,len(dictionary) -1)]
    return s

@app.get('/')
async def main():
    return FileResponse('Desktop/url-shortener/main/index.html')

@app.get("/link/{hash}")
async def main(hash : str | None = None):
    if hash:
        return RedirectResponse(links[hash])
    

@app.post('/shortener/')
async def mk_link(long_url : str = Form()):
    
    if validators.url(long_url)== True:
        r_domain = mk_string()
        links[r_domain] = long_url
        return {
            'valid': 0,
            'link' : 'http://192.168.1.69:5555/link/' + r_domain
        }
    elif validators.url(long_url)== False:
        return {
            'valid': 1,
            'link' : 'Inserted link is not valid'
        }
    
    
    
uvicorn.run(app,host="192.168.1.69",port=5555)