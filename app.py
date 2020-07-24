import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'NPCLibrary'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/get_npcs')
def get_npcs():
    return render_template("npcs.html",
        npcs=mongo.db.NPC.find().sort('name', 1))


@app.route('/npc_overview/<npc_id>')
def npc_overview(npc_id):
    currentNPC = mongo.db.NPC.find_one({"_id": ObjectId(npc_id)})
    return render_template('npcoverview.html', npc=currentNPC)


@app.route('/edit_npc/<npc_id>')
def edit_npc(npc_id):
    currentNPC = mongo.db.NPC.find_one({"_id": ObjectId(npc_id)})
    return render_template('editnpc.html', npc=currentNPC)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
