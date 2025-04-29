from fastapi import FastAPI, HTTPException, status
from fastapi.params import Body
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel

site = FastAPI()

class Materia(BaseModel):
    faculdade: str
    disciplina: str
    tema: str
    semestre: int
    curso: str

while True:
    try:
        conn = psycopg2.connect(
            host = "localhost", 
            database = "fastapi", 
            user = "postgres", 
            password = 'jumajupwar',
            cursor_factory = RealDictCursor)
        print('Successfully connected to the DataBase!')
        cursor = conn.cursor()
        break
    
    except Exception as error:
        print("Failed to connect to DataBase!")
        print('Error:', error)
        
        

@site.get("/")
def home_page():
    return{"Message": "This is the HomePage of our Site!"}

@site.get("/materias")
def get_materias():
    cursor.execute("""SELECT * FROM materias""")
    materias = cursor.fetchall()
    return {"Data": materias}

@site.get("/materias/{id}")
def get_materia(id: int):
    cursor.execute("""SELECT * FROM materias WHERE id = %s""", (str(id)))
    materia = cursor.fetchone()

    if not materia:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 
                            detail={"message" : f"The post with id {id} was not found"})
    
    return{"Data": materia}

@site.post("/materias", status_code=status.HTTP_201_CREATED)
def create_lesson(materia : Materia):
    cursor.execute("""INSERT INTO materias (faculdade, disciplina, tema, semestre, curso) VALUES (%s, %s, %s, %s, %s) RETURNING *""", 
                    (materia.faculdade, materia.disciplina, materia.tema, materia.semestre, materia.curso))
    new_lesson = cursor.fetchone()
    conn.commit()
    return{"Data" : new_lesson}

@site.put("/materias/{id}")
def update_lesson(id : int, materia : Materia):
    cursor.execute("""UPDATE materias SET faculdade = %s, disciplina = %s, tema  = %s, semestre = %s, curso = %s WHERE id = %s RETURNING *""",
                    (materia.faculdade, materia.disciplina, materia.tema, materia.semestre, materia.curso, str(id)))
    updated_lesson = cursor.fetchone()
    conn.commit()

    if not updated_lesson:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"Message" : "Materia nao encontrada!"})

    return{"Data" : updated_lesson}