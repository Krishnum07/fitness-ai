from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request
    })


@app.post("/recommend")
def recommend(request: Request, age: int = Form(...), goal: str = Form(...), level: str = Form(...)):

    # 🔥 WEIGHT LOSS
    if goal == "weight loss":

        if level == "beginner":
            plan = [
                {"name": "Walking", "duration": 20},
                {"name": "Jump Rope", "duration": 10},
                {"name": "Stretching", "duration": 10},
                {"name": "Light Jogging", "duration": 15},
                {"name": "Step-ups", "duration": 10},
                {"name": "Arm Circles", "duration": 5},
                {"name": "Bodyweight Squats", "duration": 10}
            ]

        elif level == "intermediate":
            plan = [
                {"name": "Running", "duration": 30},
                {"name": "Cycling", "duration": 25},
                {"name": "Mountain Climbers", "duration": 15},
                {"name": "Jump Squats", "duration": 15},
                {"name": "Burpees", "duration": 15},
                {"name": "High Knees", "duration": 10},
                {"name": "Plank", "duration": 10}
            ]

        else:
            plan = [
                {"name": "HIIT Workout", "duration": 40},
                {"name": "Sprint Intervals", "duration": 25},
                {"name": "Burpees", "duration": 20},
                {"name": "Box Jumps", "duration": 15},
                {"name": "Jump Lunges", "duration": 15},
                {"name": "Battle Ropes", "duration": 20},
                {"name": "Plank Variations", "duration": 15}
            ]

    # 💪 MUSCLE GAIN
    elif goal == "muscle gain":

        if level == "beginner":
            plan = [
                {"name": "Push-ups", "duration": 15},
                {"name": "Squats", "duration": 15},
                {"name": "Plank", "duration": 10},
                {"name": "Lunges", "duration": 15},
                {"name": "Glute Bridge", "duration": 10},
                {"name": "Wall Sit", "duration": 10},
                {"name": "Superman Hold", "duration": 10}
            ]

        elif level == "intermediate":
            plan = [
                {"name": "Bench Press", "duration": 30},
                {"name": "Deadlifts", "duration": 30},
                {"name": "Pull-ups", "duration": 15},
                {"name": "Shoulder Press", "duration": 20},
                {"name": "Barbell Squats", "duration": 25},
                {"name": "Bicep Curls", "duration": 15},
                {"name": "Tricep Dips", "duration": 15}
            ]

        else:
            plan = [
                {"name": "Heavy Lifting", "duration": 60},
                {"name": "Barbell Squats", "duration": 40},
                {"name": "Deadlifts", "duration": 40},
                {"name": "Bench Press", "duration": 35},
                {"name": "Shoulder Press", "duration": 30},
                {"name": "Weighted Pull-ups", "duration": 25},
                {"name": "Leg Press", "duration": 30}
            ]

    # 🧘 OTHER
    else:
        plan = [
            {"name": "Yoga", "duration": 20},
            {"name": "Meditation", "duration": 15},
            {"name": "Stretching", "duration": 15},
            {"name": "Breathing Exercises", "duration": 10},
            {"name": "Light Walking", "duration": 20},
            {"name": "Mobility Drills", "duration": 15},
            {"name": "Relaxation Exercises", "duration": 10}
        ]

    return templates.TemplateResponse("index.html", {
        "request": request,
        "plan": plan
    })