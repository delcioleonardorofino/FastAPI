from models import Task
from database import cursor, conn
from fastapi import HTTPException, Response, status


def get_tasks():
    cursor.execute("""SELECT * FROM tasks""")
    tasks = cursor.fetchall()
    return {"Tasks" : tasks}


def get_completed_tasks():
    cursor.execute("""SELECT * FROM tasks WHERE completed = true""")
    completed_tasks = cursor.fetchall()

    if  not completed_tasks:
        print("You don't have completed tasks.")

    return {'Data': completed_tasks}


def get_uncompleted_tasks():
    cursor.execute('''SELECT * FROM tasks WHERE completed = false''')
    uncompleted_task = cursor.fetchone()

    if not uncompleted_task:
        print('You do not have uncompleted tasks!')

    return {'Uncompleted Tasks' : uncompleted_task}


def create_task(task : Task):
    cursor.execute('''INSERT INTO taks (title, content) VALUES (%s, %s) 
                   RETURNING *''', (task.title, task.content))
    new_task = cursor.fetchone()
    conn.commit()

    return{"Data" : new_post}

def complete_task(id : int, task : Task):
    cursor.execute('''UPDATE tasks SET completed = true WHERE id = %s RETURNING *''',
                    (task.completed, str(id)))
    task_completed = cursor.fetchone()
    conn.commit()

    if not task_completed: #Retrieves a status_code to tell the frontend what is the issue if post with certain id was not found
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                           detail={"message" : f"The task with id {id} was not found"})

    return {"Data" : task_completed}

def delete_task(id : int):
    cursor.execute('''DELETE FROM tasks WHERE id = %s RETURNING *''',
                    (task.title, task.content, task.completed, str(id)))
    task_deleted = cursor.fetchone()
    conn.commit()

    if not task_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="task not Found!")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

