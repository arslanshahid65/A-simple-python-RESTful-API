from fastapi import FastAPI, status, HTTPException,Response
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randint

app = FastAPI()

# model creation for schema validation
class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None

my_posts = [{"title":"AI software", "Content":"I want to talk about AI software", "id": 1}, {"title":"Best languages", "Content":"1) Python 2) Javascript 3) PHP", "id": 2}]

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post

def find_post_index(id):
    for index, post in enumerate(my_posts):
        if post["id"] == id:
            return index

@app.get("/")
def root():
    return {"Home":"A Blogging App"}

@app.get("/posts")
def get_posts():     
    return {"data": my_posts}

@app.post("/posts", status_code =status.HTTP_201_CREATED)
def create_post(payload: Post):
    post_dict= payload.dict()
    post_dict["id"] = randint(1, 10000)
    my_posts.append(post_dict)
    return {"New Post": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with ID: {id} doesnt exist")
    return post

@app.delete("/posts/{id}")
def delete_post(id: int):
    index = find_post_index(id)
    print(index)
    if index== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} doesnt exits.")
    
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put('/posts/{id}')
def update_post(payload: Post, id: int):
    index = find_post_index(id)
    print(index)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The post with id: {id} doesnt exist.")
    post_dict= payload.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict
    return {"Updated": f"The post with ID: {id} has been updated"}