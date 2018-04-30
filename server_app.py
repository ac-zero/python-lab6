from flask import Flask, jsonify, request
import sql_db

app = Flask(__name__)

@app.route('/tasks')
def apiShowTasks():
    list = sql_db.showAll()
    return jsonify(list)

@app.route('/tasks', methods=['POST'])
def apiCreateTasks():
    if request.headers['Content-Type'] == 'application/json':
        new_user = request.json
        name = new_user['todo']
        if not sql_db.check_name(name):
            if new_user['urgent']:
                sql_db.insert_urgent(name)
            else:
                sql_db.insert(name)
            response = jsonify(sql_db.get_name(name))
        else:
            response = jsonify({ 'message' : "Not Found!"})
            response.status_code = 404
    else:
        response = jsonify({ 'message': "Invalid Request"})
        response.status_code = 404
    return response

@app.route('/tasks/<int:id>')
def apiGetTask(id):
    if sql_db.check_id(id):
        response = jsonify(sql_db.get_id(id))
    else:
        response = jsonify({ 'message' : "Not Found!"})
        response.status_code = 404
    return response

@app.route('/tasks/<int:id>' , methods=['PUT'])
def apiUpdateTask(id):
    if request.headers['Content-Type'] == 'application/json':
        new_user = request.json
        id = new_user['id']
        if sql_db.check_id(id):
            sql_db.update(id,new_user['todo'],new_user['urgent'])
            response = jsonify(sql_db.get_id(id))
        else:
            response = jsonify({ 'message' : "Not Found!"})
            response.status_code = 404
    else:
        response = jsonify({ 'message': "Invalid Request"})
        response.status_code = 404
    return response

@app.route('/tasks/<int:id>' , methods=['DELETE'])
def apiDeleteTask(id):
    if sql_db.check_id(id):
        jsonify(sql_db.remove(id))
        response = jsonify({ 'message' : "Deleted!"})
    else:
        response = jsonify({ 'message' : "Not Found!"})
        response.status_code = 404
    return response

if __name__ == '__main__':
    app.run()