from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Blog(BaseModel):
    id: int
    title: str
    description: str
    author: Optional[str] = None

blog_posts = []

@app.get("/")
def root():
    return {"message": "Welcome to my Blog App"}

@app.get("/posts", response_model=List[Blog])
def get_posts():
    return blog_posts

@app.post("/posts", response_model=Blog)
def create_post(post: Blog):
    blog_posts.append(post)
    return post

@app.get("/posts/{post_id}", response_model=Blog)
def get_post(post_id: int):
    for post in blog_posts:
        if post.id == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post Not Found")

@app.put("/posts/{post_id}", response_model=Blog)
def update_post(post_id: int, updated_post: Blog):
    for index, post in enumerate(blog_posts):
        if post.id == post_id:
            blog_posts[index] = updated_post
            return updated_post
    raise HTTPException(status_code=404, detail="Post Not Found")

@app.patch("/posts/{post_id}", response_model=Blog)
def partial_update_post(post_id: int, updated_post: Blog):
    for post in blog_posts:
        if post.id == post_id:
            if updated_post.title is not None:
                post.title = updated_post.title
            if updated_post.description is not None:
                post.description = updated_post.description
            if updated_post.author is not None:
                post.author = updated_post.author
            return post
    raise HTTPException(status_code=404, detail="Post Not Found")

@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    for index, post in enumerate(blog_posts):
        if post.id == post_id:
            blog_posts.pop(index)
            return {"detail":"Post Deleted"}
    raise HTTPException(status_code=404, detail="Post Not Found")
