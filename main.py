from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None


@app.get("/")
def root():
    return {"message": "just making sure this works save this "}

@app.get("/post")
def get_posts():
    return [
        "data",
        "calls",
        "Instance"
    ]
    
@app.post("/createposts")
def create_post(post: Post):
    print(post)
    print(post.model_dump())
    return {"new_post" : f"title {post.title}, content {post.content}"}
# title : Str, content: Str
    