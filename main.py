#Import Flask Library
import flask
from flask import Flask, render_template, request, session, url_for, redirect, flash
import os
#import config
from app import app
#from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import hashlib

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


###Initialize the app from Flask
##app = Flask(__name__)
##app.secret_key = "secret key"

#Configure MySQL
conn = pymysql.connect(host='localhost',
                       port = 8889,
                       user='root',
                       password='root',
                       db='...',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)


#Define a route to hello function
@app.route('/')
def hello():
    session['name'] = None
    return render_template('index.html')

#Define a route to login
@app.route('/login')
def login():
    return render_template('login.html')

#Define a route to register
@app.route('/register')
def register():
    return render_template('register.html')

#Authenticates the login
@app.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
    #grab information
    username = request.form['username']
    password = request.form['password']

    #add hash
   

    #cursor
    cursor = conn.cursor()
    #execute query
    query = 'SELECT pwd FROM user WHERE username=%s'
    cursor.execute(query,username)
    #store result
    data = cursor.fetchone()
    cursor.close()
    if(data==None):
        return render_template('index.html')
    db_password = data['pwd']
   
    error = None

    #check
    if(input_pwd_hash==db_pwd_hash):
        session['name'] = username
        #update login status

        formatted_date = loginStats.strftime('%Y-%m-%d')
    
        cursor = conn.cursor()
        cursor.execute(loginDateSql,(username))
        lastLoginTime = cursor.fetchone()
        # store the last login time
        session['lastlogin'] = lastLoginTime['lastlogin']
        cursor.execute(query, (formatted_date, username))
        conn.commit()
        cursor.close()
        return redirect(url_for(('home')))
    else:
        error = 'Invalid login'
        return render_template('login.html',error=error)

#Authenticates the register
@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
    #grabs information from the forms
    username = flask.request.form['username']
    password = flask.request.form['password']
    fname = flask.request.form['fname']
    lname = flask.request.form['lname']
    nickname = flask.request.form['nickname']
    #cursor used to send queries
    cursor = conn.cursor()
    #executes query
    query = 'SELECT * FROM user WHERE username = %s'
    cursor.execute(query, (username))
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    error = None

    loginStats = datetime.utcnow().strftime('%Y-%m-%d')

    if(data):
        #If the previous query returns data, then user exists
        error = "This user already exists"
        return render_template('register.html', error = error)
    else:
        ins = 'INSERT INTO user VALUES(%s, %s, %s, %s, %s,%s)'
        cursor.execute(ins, (username, password, fname, lname, loginStats, nickname))
        conn.commit()
        cursor.close()
        return render_template('index.html')


@app.route('/home')
def home():
    if session['name'] == None:
        return render_template('index.html')
    else:
        username = session['name']
    
        lastlogin = datetime.strptime(lastlogin,session['stringFormat'])
        lastlogin = lastlogin.date()
        cursor = conn.cursor()
        query = 'SELECT fname,lname,nickname FROM user WHERE username=%s'
        cursor.execute(query, (username))
        data = cursor.fetchone()

        
        
            '''



        #cursor.execute(query1, (username,lastlogin,username,lastlogin,username,lastlogin))

        cursor.execute(query1,(username,lastlogin,username,lastlogin,username,lastlogin))
        friendReviewsData = cursor.fetchall()
        songdata = cursor.fetchall()
        cursor.close()
        return render_template('home.html',user=data,songReviews=friendReviewsData,newSongs=songdata)



#Define music search

@app.route('/musicSearch',methods=['GET','POST'])
def musicSearch():
    return render_template('musicSearch.html')





#Define music search action
@app.route('/musicSearchAction',methods=['GET','POST'])



#Define song
@app.route('/song',methods=["GET","POST"])
def song():

    songID = request.form['songID']
    session['songID'] = songID

    #cursor used to send queries
    cursor = conn.cursor()

    # drop view
    dropSql = "DROP VIEW IF EXISTS aveRate"
    cursor.execute(dropSql)

    #executes query
    VIEW = ''' CREATE VIEW aveRate AS (SELECT songID,AVG(stars) as aves
                FROM song NATURAL JOIN rateSong 
                GROUP BY songID);
        '''

    cursor.execute(VIEW)
    cursor.execute(query,(songID))
    #stores the results in a variable
    data = cursor.fetchone()



    cursor.close()
    error = None
    if(data):
        return render_template("song.html",songs=data)
    else:
        #returns an error message to the html page
        error = 'Invalid, no matching song'
        return render_template('musicSearch.html', error=error)

#Define showSong for back
@app.route('/showSong',methods=["GET","POST"])
def showSong():

    songID = session['songID']

    #cursor used to send queries
    cursor = conn.cursor()

    # drop view
    dropSql = "DROP VIEW IF EXISTS aveRate"
    cursor.execute(dropSql)

    #executes query

        '''

    cursor.execute(VIEW)
    cursor.execute(query,(songID))
    #stores the results in a variable
    data = cursor.fetchone()

    cursor.close()
    error = None
    if(data):
        return render_template("song.html",songs=data)
    else:
        #returns an error message to the html page
        error = 'Invalid, no matching song'
        return render_template('musicSearch.html', error=error)



#Define rating the song
@app.route('/rateSong',methods=["GET","POST"])
def rateSong():
    if(None!=session['name']):
        username = session['name']
        songID = session['songID']
        # cursor used to send queries
        cursor = conn.cursor()
        # executes query
     
        cursor.execute(query, (songID))
        # stores the results in a variable
        rates = cursor.fetchall()
        cursor.close()

        return render_template('rateSong.html',rateResult=rates)
    else:
        return render_template('index.html')


#Define rate song action
@app.route('/rateSongAction',methods=["GET","POST"])





#Define review the song
@app.route('/reviewSong',methods=["GET","POST"])
def reviewSong():
    if (session['name']!=None):
        username = session['name']
        songID = session['songID']
        # cursor used to send queries
        cursor = conn.cursor()
        # executes query
     
        cursor.execute(query, (songID))
        # stores the results in a variable
        reviews = cursor.fetchall()
        cursor.close()
        return render_template('reviewSong.html',reviewResult=reviews)
    else:
        return render_template('index.html')




#Define review song action
@app.route('/reviewSongAction',methods=["GET","POST"])
def reviewSongAction():
    if (session['name']!=None):
        username = session['name']
        songID = session['songID']
        reviews = request.form['reviews']
        cursor = conn.cursor()
        date = datetime.utcnow().strftime('%Y-%m-%d')

        # executes query
        query = 'SELECT * FROM reviewSong WHERE username=%s AND songID=%s'
        cursor.execute(query, (username, songID))
        # stores the results in a variable
        data = cursor.fetchone()


    else:
        return render_template('index.html')






########

# NOTE: Assume in a friend request, user1 is the sender, user2 is the receiver in friend request system

#Define friends page



# NOTE: Assume in a friend request, user1 is the sender, user2 is the receiver in friend request system

#Define friend accept
@app.route('/accept',methods=['GET','POST'])
def accept():
    user = session['name']
    sender = request.form['acceptUserName']
    cursor = conn.cursor()

    check = "SELECT * FROM friend WHERE user1=%s AND user2=%s AND acceptStatus='Pending'"
    cursor.execute(check, (sender, user))
    checkone = cursor.fetchone()

    if(checkone):
         # user1 is the sender, user2 is the receiver
        cursor.execute(query, (sender, user))
        conn.commit()
        cursor.close()
        return redirect(url_for('friends'))

    else:

        error = 'no such pending request'
        return redirect(url_for('friends'))

#Define friend reject
@app.route('/reject',methods=['POST'])
def reject():
    user = session['name']
    sender = request.form['rejectUserName']
    cursor = conn.cursor()

    check = "SELECT * FROM friend WHERE user1=%s AND user2=%s AND acceptStatus='Pending'"
    cursor.execute(check, (sender, user))
    checkone = cursor.fetchone()

    if (checkone):
        cursor.execute(query, (sender, user))
        conn.commit()
        cursor.close()
        return redirect(url_for('friends'))
    else:
        error = 'no such pending request'
        return redirect(url_for('friends'))


#Define send requests
@app.route('/friendRequest',methods=['POST'])


#Define unfriend
@app.route('/unfriend',methods=["POST"])
def unfriend():
    sender = session['name']
    name = request.form['name']
    cursor = conn.cursor()
    query = '''SELECT * FROM friend WHERE user1=%s AND user2=%s
    UNION 
    SELECT * FROM friend WHERE user1=%s AND user2=%s'''  # consider both cases that user is in user1 or in user2
    cursor.execute(query,(sender,name,name,sender))
    data = cursor.fetchone()
    if(data):


        cursor.execute(delete1,(name,sender))
        conn.commit()
        cursor.execute(delete2, (sender, name))
        conn.commit()
        cursor.close()
        return redirect(url_for('friends'))

    else:
        error = 'no matching friend'
        return redirect(url_for('friends'))




#Define addFollow page
@app.route('/addFollow',methods=["POST"])
def addFollow():
    user = session['name']
    person = request.form['name']


    cursor = conn.cursor()
    check = 'SELECT * FROM user WHERE username=%s'
    cursor.execute(check,person)
    Person=cursor.fetchone()
    if(Person):
        query = '''INSERT INTO follows values(%s,%s,%s)'''
        cursor.execute(query,(user,person,sendTime))
        conn.commit()
        cursor.close()
        return redirect(url_for('follow'))
    else:
        return redirect(url_for('follow'))

#Define unfollow page
@app.route('/unfollow',methods=["POST"])
def unfollow():
    user = session['name']
    person = request.form['name']

    #check
    cursor = conn.cursor()
    check = 'SELECT * FROM user WHERE username=%s'
    cursor.execute(check, person)
    Person = cursor.fetchone()
    if(Person):
        query = '''DELETE FROM follows WHERE follower=%s AND follows=%s'''
        cursor.execute(query,(user,person))
        conn.commit()
        cursor.close()
        return redirect(url_for('follow'))
    else:
        return redirect(url_for('follow'))



#Define playlist
@app.route('/playlist')
def playlist():
    username = session['name']
    cursor = conn.cursor()
    query = '''SELECT * FROM playlist WHERE username=%s'''
    cursor.execute(query, username)
    data = cursor.fetchall()
    cursor.close()

    return render_template('playlist.html',playlist=data)

#Define createPlaylist
@app.route('/createPlaylist',methods=["GET","POST"])
def createPlaylist():
    username = session['name']
    title = request.form['title']
    desp = request.form['desp']
    cursor = conn.cursor()
    query1 = '''SELECT * FROM playlist WHERE username=%s AND title=%s'''
    cursor.execute(query1, (username,title))
    data = cursor.fetchall()
    if(data):
        error='playlist already exists'
        cursor.close()
        return render_template('playlist.html', error=error)
    else:
        loginStats = datetime.utcnow()
        formatted_date = loginStats.strftime('%Y-%m-%d')
        query = '''INSERT INTO playlist VALUES(%s,%s,%s,%s)'''
        cursor.execute(query,(title,username,formatted_date,desp))
        conn.commit()
        query1 = '''SELECT * FROM playlist WHERE username=%s'''
        cursor.execute(query1, username)
        data = cursor.fetchall()
        cursor.close()
        return render_template('playlist.html',playlist=data)


#Define addPlaylist
@app.route('/addPlaylist',methods=['GET','POST'])
def addPlaylist():
    if session['name'] == None:
        return render_template('index.html')
    else:
        username = session['name']
        cursor = conn.cursor()
        query1 = '''SELECT * FROM playlist WHERE username=%s'''
        cursor.execute(query1, username)
        data = cursor.fetchall()
        cursor.close()
        if(data):
            return render_template('addPlaylist.html',playlist=data)
        else:
            return redirect(url_for('showSong'))

#Define addPlaylistAction
@app.route('/addPlaylistAction',methods=['GET','POST'])


#Define listSong
@app.route('/listSong',methods=['GET','POST'])
def listSong():
    username = session['name']
    title = request.form['title']

    cursor = conn.cursor()
    query1 = '''SELECT song.songID,song.title FROM songInList JOIN song ON (song.songID=songInList.songID AND username=%s) WHERE songInList.title=%s'''
    cursor.execute(query1, (username, title))
    data = cursor.fetchall()
    return render_template('listSong.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.secret_key = 'some key that you will never guess'
# Run the app on localhost port 5000
# debug = True -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
















