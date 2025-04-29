from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time


app = FastAPI()

class Post(BaseModel): #Inherites from the Class BaseModel
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title" : "This is my first post", "content" : "This the content of my first post", "id" : 1},
{"title" : "POst nr 2", "content" : "content 2", "id" : 2}]

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='jumajupwar', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connected Successfully!")
        break

    except Exception as error:
        print("connection to database failed!")
        print("Error: ", error)
        time.sleep(5)


def find_post(id): #Looks for the post in the posts 
        #list that matches with given id
    for post in my_posts:
        if post["id"] == id:
            return post

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    print(posts)
    return {"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post : Post): #takes the class Post and assigns it to the variable post, to then                    
    cursor.execute("""INSERT INTO posts (name, content, published) VALUES (%s, %s, %s) RETURNING *""", 
                    (post.title, post.content, post.published)) # converts the post JSON file into a py dict
    new_post = cursor.fetchone()
    conn.commit()
    return {"data" : new_post}

@app.get("/posts/{id}")
def get_post(id:int, response: Response):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    post = cursor.fetchone()
    
    if not post: #Retrieves a status_code to tell the frontend what is the issue if post with certain id was not found
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                           detail={"message" : f"The post with id {id} was not found"})
    return {"Post" : post }

@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
    deleted_post = cursor.fetchone()
    conn.commit()
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} unexistent!")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id:int, post : Post):
    cursor.execute("""UPDATE posts SET name = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
                (post.title, post.content, post.published, (str(id))) )
    updated_post = cursor.fetchone()
    conn.commit()
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} unexistent!")

    return {"Data": updated_post}
