from flask import Flask
from flask import jsonify
from flask import request
from constants import CONSTANTS
from flask import make_response
from sampleData import *
from createDB import *
from bson import json_util, ObjectId  # For ObjectId to work
import json
from settings import *
import ast
import sys  # for printing to terminal

app = Flask(__name__)


def serial(items):
    for index in items:
        if isinstance(items[index], ObjectId):
            items[index] = str(items[index])
    return items

# List Endpoint -
@app.route(CONSTANTS['ENDPOINT']['LIST'])
def getList():
    itemCol = list_items.find()
    data = [serial(item) for item in itemCol]
    return jsonify(data)

# throw 404 if id doesn't exist
@app.route(CONSTANTS['ENDPOINT']['LIST'], methods=['POST'])
def addListItem():
    data = request.data.decode('utf-8')
    data = ast.literal_eval(data)
    listItem = {'text': data['text']}
    created = list_items.insert_one(listItem)
    return jsonify(
        {'_id': str(created.inserted_id), 'text': listItem['text']}
    )

# add error handler - None or >1
@app.route(CONSTANTS['ENDPOINT']['LIST'] + '/<id>', methods=['DELETE'])
def deleteListItem(id):
    queryStr = {'_id': ObjectId(id)}
    count = 0
    result = list_items.find(queryStr)
    for item in iter(result):
        count += 1
    if count == 0:
        return jsonify({'error': 'Could not find an item with given id'})
    elif count > 1:
        return jsonify({'error': 'There is more than one item with the given id'})
    list_items.delete_one(queryStr)
    return jsonify(
        {'_id': id, 'text': 'This comment was deleted'}
    )

# Grid Endpoint
@app.route(CONSTANTS['ENDPOINT']['GRID'])
def getGrid():
    return jsonify(
        sampleGridData
    )

# MasterDetail Endpoint
@app.route(CONSTANTS['ENDPOINT']['MASTERDETAIL'])
def getMasterDetail():
    return jsonify(
        sampleGridData
    )


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=CONSTANTS['PORT'])
