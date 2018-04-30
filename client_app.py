import requests

baseurl = 'http://localhost:5000'

def list_tasks():
    tasks = requests.get(baseurl + "/tasks").json()
    print(tasks)

def create_task(todo, urgent):
    new_task = {'todo' : todo, 'urgent' : urgent}
    req = requests.post(baseurl + "/tasks", json=new_task)
    if req.status_code == 200:
        print(req.json())
    else:
        print("Error on task creation")

def update_task(id, todo, urgent):
    new_task = {'id' : id, 'todo' : todo, 'urgent' : urgent}
    req = requests.put(baseurl + "/tasks/" + str(id), json=new_task)
    if req.status_code == 200:
        print(req.json())
    else:
        print("Error on update")

def delete_task(id):
    req = requests.delete(baseurl + "/tasks/" + str(id))
    if req.status_code == 200:
        print("Deleted")
    else:
        print("Error on delete")

def get_task(id):
    req = requests.get(baseurl + "/tasks/" + str(id))
    if req.status_code == 200:
        print(req.json())
    else:
        print("Error on getting task")

if __name__ == '__main__':
    list_tasks()