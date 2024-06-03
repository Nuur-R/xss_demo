from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": ""})

@app.post("/", response_class=HTMLResponse)
async def submit_form(request: Request, message: str = Form(...)):
    return templates.TemplateResponse("index.html", {"request": request, "message": message})
