from flask import Flask
from es_node import Cluster

app = Flask(__name__)

client = Cluster(app)

@app.route('/pop')
def handle_beverage():
    return client.get_all()

@app.route('/pop/id/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_pop(id):
    return client.search_by_id(id)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
