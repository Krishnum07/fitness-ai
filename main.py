from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# ✅ VERY IMPORTANT — NO brackets, NO comma
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/recommend", response_class=HTMLResponse)
def recommend(request: Request, age: int = Form(...), goal: str = Form(...), level: str = Form(...)):

    plan = [
        {"name": "Push-ups", "duration": 10},
        {"name": "Squats", "duration": 10},
        {"name": "Plank", "duration": 5},
        {"name": "Lunges", "duration": 10},
        {"name": "Jump Rope", "duration": 5},
        {"name": "Stretching", "duration": 10},
        {"name": "Running", "duration": 15}
    ]

    return templates.TemplateResponse("index.html", {
        "request": request,
        "plan": plan
    })