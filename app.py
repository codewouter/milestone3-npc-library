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
    return render_template('welcome.html')

# ---------- routes for NPCs ----------
@app.route('/get_npcs')
def get_npcs():
    return render_template("npcs.html", npcs=mongo.db.NPC.find().sort('name', 1))


@app.route('/add_npc')
def add_npc():
    allRaces = mongo.db.race.find()
    allClasses = mongo.db.NPCClass.find()
    return render_template('newnpc.html', races=allRaces, classes=allClasses)


@app.route('/insert_npc', methods=['POST'])
def insert_npc():
    npcs = mongo.db.NPC
    npcs.insert_one(request.form.to_dict())
    return redirect(url_for('get_npcs'))


@app.route('/npc_overview/<npc_id>')
def npc_overview(npc_id):
    currentNPC = mongo.db.NPC.find_one({"_id": ObjectId(npc_id)})
    return render_template('npcoverview.html', npc=currentNPC)


@app.route('/edit_npc/<npc_id>')
def edit_npc(npc_id):
    currentNPC = mongo.db.NPC.find_one({"_id": ObjectId(npc_id)})
    allRaces = mongo.db.race.find()
    allClasses = mongo.db.NPCClass.find()
    return render_template('editnpc.html', npc=currentNPC, races=allRaces, classes=allClasses)


@app.route('/update_npc/<npc_id>', methods=["POST"])
def update_npc(npc_id):
    npcs = mongo.db.NPC
    npcs.update({'_id': ObjectId(npc_id)},
    {
        'name': request.form.get('npcOverviewName'),
        'race': request.form.get('npcOverviewRace'),
        'class': request.form.get('npcOverviewClass'),
        'level': request.form.get('npcOverviewLevel'),
        'strength': request.form.get('npcOverviewStrength'),
        'dexterity': request.form.get('npcOverviewDexterity'),
        'constitution': request.form.get('npcOverviewConstitution'),
        'intelligence': request.form.get('npcOverviewIntelligence'),
        'wisdom': request.form.get('npcOverviewWisdom'),
        'charisma': request.form.get('npcOverviewCharisma'),
        'description': request.form.get('npcOverviewDescription')
    })
    return redirect(url_for('npc_overview', npc_id=npc_id))


@app.route('/delete_npc/<npc_id>')
def delete_npc(npc_id):
    mongo.db.NPC.remove({'_id': ObjectId(npc_id)})
    return redirect(url_for('get_npcs'))

# ---------- routes for races ----------
@app.route('/get_races')
def get_races():
    return render_template('races.html', races=mongo.db.race.find().sort('race', 1))


@app.route('/add_race')
def add_race():
    return render_template('newrace.html')


@app.route('/insert_race', methods=['POST'])
def insert_race():
    races = mongo.db.race
    races.insert_one(request.form.to_dict())
    return redirect(url_for('get_races'))


@app.route('/edit_race/<race_id>')
def edit_race(race_id):
    currentRace = mongo.db.race.find_one({"_id": ObjectId(race_id)})
    return render_template('editrace.html', race=currentRace)


@app.route('/update_race/<race_id>', methods=["POST"])
def update_race(race_id):
    races = mongo.db.race
    races.update({'_id': ObjectId(race_id)},
    {
        'race': request.form.get('raceName'),
        'description': request.form.get('raceDescription')
    })
    return redirect(url_for('get_races'))


@app.route('/delete_race/<race_id>')
def delete_race(race_id):
    mongo.db.race.remove({'_id': ObjectId(race_id)})
    return redirect(url_for('get_races'))


# ---------- routes for classes ----------
@app.route('/get_classes')
def get_classes():
    return render_template('classes.html', classes=mongo.db.NPCClass.find().sort('class', 1))


@app.route('/add_class')
def add_class():
    return render_template('newclass.html')


@app.route('/insert_class', methods=['POST'])
def insert_class():
    classes = mongo.db.NPCClass
    classes.insert_one(request.form.to_dict())
    return redirect(url_for('get_classes'))


@app.route('/edit_class/<class_id>')
def edit_class(class_id):
    currentClass = mongo.db.NPCClass.find_one({"_id": ObjectId(class_id)})
    return render_template('editclass.html', NPCClass=currentClass)


@app.route('/update_class/<class_id>', methods=["POST"])
def update_class(class_id):
    classes = mongo.db.NPCCLass
    classes.update({'_id': ObjectId(class_id)},
    {
        'NPCClass': request.form.get('className.lower()'),
        'description': request.form.get('classDescription')
    })
    return redirect(url_for('get_classes'))


@app.route('/delete_class/<class_id>')
def delete_class(class_id):
    mongo.db.NPCClass.remove({'_id': ObjectId(class_id)})
    return redirect(url_for('get_classes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
