from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("YOUR_MONGODB_ATLAS_URI")
db = client.get_database('test_db')
collection = db.get_collection('todo_items')

@app.route("/", methods=["GET"])
def index():
    return render_template("todo_page.html")

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    try:
        collection.insert_one({'name': item_name, 'description': item_description})
        return redirect(url_for('index'))
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
