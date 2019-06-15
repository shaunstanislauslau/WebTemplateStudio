from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
from sampleData import *
from createdDb import SQLObj
from constants import CONSTANTS
import ast
import sys

app = Flask(__name__)

sqlDatabaseObj = SQLObj()

# List Endpoints
@app.route(CONSTANTS['ENDPOINT']['LIST'])
def getList():
    queryStr = {
        'query': "SELECT r.id as _id, r.text FROM root r ORDER BY r._ts DESC"}
    options = {}
    options['enableCrossPartitionQuery'] = True
    options['maxItemCount'] = 2
    results_iterable = sqlDatabaseObj.getClient().QueryItems(
        sqlDatabaseObj.getContainer()['_self'], queryStr, options)
    return jsonify(
        list(results_iterable)
    )


@app.route(CONSTANTS['ENDPOINT']['LIST'], methods=['POST'])
def addListItem():
    data = request.data.decode('utf-8')
    data = ast.literal_eval(data)
    listItem = {'text': data['text']}
    created = sqlDatabaseObj.getClient().CreateItem(
        sqlDatabaseObj.getContainer()['_self'], listItem)
    return jsonify(
        {'_id': created['id'], 'text': listItem['text']}
    )


@app.route(CONSTANTS['ENDPOINT']['LIST'] + '/<id>', methods=['DELETE'])
def deleteListItem(id):
    # use parameterized queries to avoid SQL injection attacks
    findStr = "SELECT * FROM c where c.id = @id"
    queryStr = {
        'query': findStr,
        'parameters': [
            {'name': '@id', 'value': id}
        ]
    }
    result = sqlDatabaseObj.getClient().QueryItems(
        sqlDatabaseObj.getContainer()['_self'], queryStr)
    count = sum(1 for _ in iter(result))
    if count == 0:
        return jsonify({'error': 'Could not find an item with given id'})
    elif count > 1:
        return jsonify({'error': 'There is more than one item with the given id'})
    for item in iter(result):
        sqlDatabaseObj.getClient().DeleteItem(item['_self'])
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

# Error Handler
@app.errorhandler(404)
def page_not_found(error):
    return make_response(
        jsonify({'error': 'Page not found'}), 404
    )


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=CONSTANTS['PORT'])
