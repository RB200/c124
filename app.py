from flask import Flask,jsonify,Request
from werkzeug.wrappers import request

tasks=[{
    'id':1,
    'title':u'learn python',
    'description':u'need to find good python tutorial on the web',
    'run':False
},{
    'id':2,
    'title':u'learn python',
    'description':u'need to find good python tutorial on the web',
    'run':False
}]



app=Flask(__name__)
@app.route('/')
def Hello_World():
    return 'Hello World'
@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({'status':'error',
        'message':'Please provide the data'},400)
    task={
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',''),
        'run':False
    }
    tasks.append(task)
    return jsonify({
        'status':'success',
        'message':'Task added successfully'
    
    })
@app.route('/get-data')
def get_task():
     return jsonify({
         'data':tasks
     })

if(__name__=='__main__'):
    app.run(debug=True)


