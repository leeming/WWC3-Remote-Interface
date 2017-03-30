from flask import Flask
from flask import request
from flask import abort

app = Flask(__name__)

@app.route('/')
def root_view():
	return 'TODO show some help for how to use the API'

@app.route('/register')
def register_view():
	return 'register'

@app.route('/login', methods=['POST', 'GET'])
def login_view():
	if request.method == 'GET':
		return login_helper()
	elif request.method == 'POST':
		print("do some stuff")

	return 'register'

@app.route('/map')
@app.route('/map/<int:mapid>')
def map_view(mapid=None):
	if mapid is None:
		return map_helper()
	else:
		return 'map %d'%(mapid,);

@app.route('/action')
def action_view():
	if isLoggedIn():
		return action_helper()
	else:
		#abort(404);
		return 'notlogged'

@app.route('/action/move/', methods=['GET'])
def action_move_view():
	return "TODO"

@app.route('/action/move/<int:cid>', methods=['POST'])
def action_move_to(cid):
	isLoggedIn()
	return cid

@app.route('/action/attack/', methods=['GET'])
def action_attack_view():
        return "TODO"

@app.route('/action/attack/<int:cid>', methods=['POST'])
def action_attack_country(cid):
	isLoggedIn()
        return "TODO"

@app.route('/action/attack/<int:cid>/<int:pid>', methods=['POST'])
def action_attack_player(cid, pid):
        return "TODO"




#-----

def isLoggedIn():
	return False;

#-----

def login_helper():
	return "TODO"

def map_helper():
	return "TODO"


from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return "NE NOR NE NOR"
