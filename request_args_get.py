from flask import Flask, request, jsonify

app = Flask(__name__)

def query_example():
    language = request.args.get('language')
    return f'''<h1>The language value is: {language}</h1>'''

app.add_resource(query_example, '')
if __name__ == '__main__':
    app.run(debug=True)
