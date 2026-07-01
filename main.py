# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Data(BaseModel):
#     id: int
#     name: str
#     course: str


# @app.get("/contact")
# def contact():
#     return "hi I am Pruthviraj"

# @app.post("/form")
# def submit_form(data: Data):
#     print(data.id)
#     print(data.name)
#     print(data.course)
#     return {"message": "Form submitted successfully"}








# from fastapi import FastAPI
# from pydantic import BaseModel
# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# load_dotenv()

# app = FastAPI()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel("gemini-2.5-flash")

# class Request(BaseModel):
#    prompt: str

# @app.post("/generate")
# def generate_response(request: Request):
#     response = model.generate_content(
#         request.prompt
#     )
#     return {"response": response.text}



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
load_dotenv()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


class Request(BaseModel):
    prompt: str


@app.post("/generate")
def generate_response(request: Request):
    try:
        response = model.generate_content(request.prompt)
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))