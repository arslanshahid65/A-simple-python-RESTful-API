from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# model creation for schema validation
class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None

my_posts = [{"title":"Post 1", "Content":"I want to talk about AI software"}]

@app.get("/")
def root():
    return {"Home":"A Blogging App"}

@app.get("/")
def get_posts():
    return {"data": "This is your Post."}

@app.post("/posts")
# title: str, content: str
def create_post(payload: Post):
    print(payload)
    return {"New Post":f"Payload: {payload}"}