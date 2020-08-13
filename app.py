import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'NPCLibrary'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


# ---------- routes for NPCs ----------
# This route/function gets all NPC entries from the database and
# passes them to render the NPC overview list
@app.route('/get_npcs')
def get_npcs():
    return render_template("npcs.html",
                           npcs=mongo.db.NPC.find().sort('name', 1))


# This route/function gets all race and class entries from the db
# and passes them to render the newnpc page
@app.route('/add_npc')
def add_npc():
    allRaces = mongo.db.race.find().sort('race', 1)
    allClasses = mongo.db.NPCClass.find().sort('class', 1)
    return render_template('newnpc.html', races=allRaces, classes=allClasses)


# This route/function will read the form on the newnpc.html page
# and insert it as a new record in the dabase.
@app.route('/insert_npc', methods=['POST'])
def insert_npc():
    npcs = mongo.db.NPC
    newNPCObject = request.form.to_dict()
    # if statements in place to catch missing key/value pairs in case
    #  no race and/or class has been selected in the dropdown lists.
    if 'race' in newNPCObject.keys():
        newNPCObject["race"] = newNPCObject["race"].lower()
    else:
        newNPCObject.update({'race': ""})
    if 'class' in newNPCObject.keys():
        newNPCObject["class"] = newNPCObject["class"].lower()
    else:
        newNPCObject.update({'class': ""})
    npcs.insert_one(newNPCObject)
    return redirect(url_for('get_npcs'))


# This route/function will recieve the relevant npc that needs
# to be viewed by the user and get the relevant data from the database.
# The data will then be passed to render the npcoverview.html page
# displaying all content about the specific NPC.
@app.route('/npc_overview/<npc_id>')
def npc_overview(npc_id):
    currentNPC = mongo.db.NPC.find_one({"_id": ObjectId(npc_id)})
    return render_template('npcoverview.html', npc=currentNPC)


# This route/function will get all necessary values about the specific
# NPC that is selected, then pass all values to render the editnpc page
# so known values are prefilled in the edit form.
@app.route('/edit_npc/<npc_id>')
def edit_npc(npc_id):
    currentNPC = mongo.db.NPC.find_one({"_id": ObjectId(npc_id)})
    allRaces = mongo.db.race.find().sort('race', 1)
    allClasses = mongo.db.NPCClass.find().sort('class', 1)
    return render_template('editnpc.html', npc=currentNPC, races=allRaces,
                           classes=allClasses)


# This route/function will take all data from the form on the editnpc.html page
# and combined with the relevant id that is being passed from the page,
# update the values in the database.
@app.route('/update_npc/<npc_id>', methods=["POST"])
def update_npc(npc_id):
    npcs = mongo.db.NPC
    newNPCObject = request.form.to_dict()
    # if statements in place to catch missing key/value pairs in case
    #  no race and/or class has been selected in the dropdown lists.
    if 'npcOverviewRace' in newNPCObject.keys():
        raceOfNPC = newNPCObject["npcOverviewRace"].lower()
    else:
        raceOfNPC = ""
    if 'npcOverviewClass' in newNPCObject.keys():
        classOfNPC = newNPCObject["npcOverviewClass"].lower()
    else:
        classOfNPC = ""
    npcs.update({'_id': ObjectId(npc_id)}, {
        'name': request.form.get('npcOverviewName'),
        'race': raceOfNPC,
        'class': classOfNPC,
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


# This route/function will recive the selected npc_id
# and delete the entry from the database.
@app.route('/delete_npc/<npc_id>')
def delete_npc(npc_id):
    mongo.db.NPC.remove({'_id': ObjectId(npc_id)})
    return redirect(url_for('get_npcs'))


# ---------- routes for races ----------
# This route/function gets all race entries from the database
# and passes them to render race list
@app.route('/get_races')
def get_races():
    return render_template('races.html',
                           races=mongo.db.race.find().sort('race', 1))


# This route/function will render the newrace.html page.
@app.route('/add_race')
def add_race():
    return render_template('newrace.html')


# This route/function will read the form on the newrace.html page
# and insert it as a new record in the dabase
@app.route('/insert_race', methods=['POST'])
def insert_race():
    races = mongo.db.race
    newRaceObject = request.form.to_dict()
    newRaceObject["race"] = newRaceObject["race"].lower()
    races.insert_one(newRaceObject)
    return redirect(url_for('get_races'))


# This route/function will get all necessary values about the specific
# race that is selected, then pass all values to render the editrace
# page so known values are prefilled in the edit form.
@app.route('/edit_race/<race_id>')
def edit_race(race_id):
    currentRace = mongo.db.race.find_one({"_id": ObjectId(race_id)})
    return render_template('editrace.html', race=currentRace)


# This route/function will take all data from the form on the
# editrace.html page and combined with the relevant id that
# is being passed from the page, then update the values in the database.
@app.route('/update_race/<race_id>', methods=["POST"])
def update_race(race_id):
    races = mongo.db.race
    races.update({'_id': ObjectId(race_id)}, {
        'race': request.form.get('raceName').lower(),
        'description': request.form.get('raceDescription')
    })
    return redirect(url_for('get_races'))


# This route/function will recive the selected race_id
# and delete the entry from the database.
@app.route('/delete_race/<race_id>')
def delete_race(race_id):
    mongo.db.race.remove({'_id': ObjectId(race_id)})
    return redirect(url_for('get_races'))


# ---------- routes for classes ----------
# This route/function gets all class entries from the database
# and passes them to render race list
@app.route('/get_classes')
def get_classes():
    return render_template('classes.html',
                           classes=mongo.db.NPCClass.find().sort('class', 1))


# This route/function will render the newclass.html page.
@app.route('/add_class')
def add_class():
    return render_template('newclass.html')


# This route/function will read the form on the newclass.html page
# and insert it as a new record in the dabase
@app.route('/insert_class', methods=['POST'])
def insert_class():
    classes = mongo.db.NPCClass
    newClassObject = request.form.to_dict()
    newClassObject["class"] = newClassObject["class"].lower()
    classes.insert_one(newClassObject)
    return redirect(url_for('get_classes'))


# This route/function will get all necessary values about the
# specific class that is selected, then pass all values to render
# the editclass page so known values are prefilled in the edit form.
@app.route('/edit_class/<class_id>')
def edit_class(class_id):
    currentClass = mongo.db.NPCClass.find_one({"_id": ObjectId(class_id)})
    return render_template('editclass.html', NPCClass=currentClass)


# This route/function will take all data from the form on the editclass.html
# page and combined with the relevant id that is being passed from the page,
# then update the values in the database.
@app.route('/update_class/<class_id>', methods=["POST"])
def update_class(class_id):
    classes = mongo.db.NPCClass
    classes.update({'_id': ObjectId(class_id)}, {
        'class': request.form.get('class').lower(),
        'description': request.form.get('description')
    })
    return redirect(url_for('get_classes'))


# This route/function will recive the selected class_id
# and delete the entry from the database.
@app.route('/delete_class/<class_id>')
def delete_class(class_id):
    mongo.db.NPCClass.remove({'_id': ObjectId(class_id)})
    return redirect(url_for('get_classes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
