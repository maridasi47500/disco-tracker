from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,phone,country_id,email,password) values (:username,:phone,:country_id,:email,:password)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','phone','country_id','email','password']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','phone','country_id','email','password']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','phone','country_id','email','password']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_userhasreviews", methods=["GET","POST"])
def add_one_userhasreviews():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into userhasreviews (user_id,content,reviewby) values (:user_id,:content,:reviewby)",hey)
        user = query_db('select * from userhasreviews')

        return render_template("userhasreviewsform.html", userhasreviewss=user, one_user=one_user, the_title="add new userhasreviews", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from userhasreviews')
    one_user = query_db("select * from userhasreviews limit 1", one=True)
    return render_template("userhasreviewsform.html", userhasreviewss=user, one_user=one_user, the_title="add new userhasreviews", touslesuser=touslesuser)

@app.route("/add_one_discosong", methods=["GET","POST"])
def add_one_discosong():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into discosong (composer_artist,title) values (:composer_artist,:title)",hey)
        user = query_db('select * from discosong')

        return render_template("discosongform.html", discosongs=user, one_user=one_user, the_title="add new discosong")


    user = query_db('select * from discosong')
    one_user = query_db("select * from discosong limit 1", one=True)
    return render_template("discosongform.html", discosongs=user, one_user=one_user, the_title="add new discosong")

@app.route("/add_one_food", methods=["GET","POST"])
def add_one_food():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into food (name,country_id) values (:name,:country_id)",hey)
        user = query_db('select * from food')

        return render_template("foodform.html", foods=user, one_user=one_user, the_title="add new food", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from food')
    one_user = query_db("select * from food limit 1", one=True)
    return render_template("foodform.html", foods=user, one_user=one_user, the_title="add new food", touslescountry=touslescountry)

@app.route("/add_one_dance", methods=["GET","POST"])
def add_one_dance():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into dance (name) values (:name)",hey)
        user = query_db('select * from dance')

        return render_template("danceform.html", dances=user, one_user=one_user, the_title="add new dance")


    user = query_db('select * from dance')
    one_user = query_db("select * from dance limit 1", one=True)
    return render_template("danceform.html", dances=user, one_user=one_user, the_title="add new dance")

@app.route("/add_one_userhasdance", methods=["GET","POST"])
def add_one_userhasdance():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesdance= query_db("select * from dance")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into userhasdance (dance_id,user_id,agility_level) values (:dance_id,:user_id,:agility_level)",hey)
        user = query_db('select * from userhasdance')

        return render_template("userhasdanceform.html", userhasdances=user, one_user=one_user, the_title="add new userhasdance", touslesdance=touslesdance, touslesuser=touslesuser)


    touslesdance= query_db("select * from dance")

    touslesuser= query_db("select * from user")

    user = query_db('select * from userhasdance')
    one_user = query_db("select * from userhasdance limit 1", one=True)
    return render_template("userhasdanceform.html", userhasdances=user, one_user=one_user, the_title="add new userhasdance", touslesdance=touslesdance, touslesuser=touslesuser)

@app.route("/add_one_userhasfood", methods=["GET","POST"])
def add_one_userhasfood():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        touslesfood= query_db("select * from food")

        one_user = query_db("insert into userhasfood (user_id,food_id) values (:user_id,:food_id)",hey)
        user = query_db('select * from userhasfood')

        return render_template("userhasfoodform.html", userhasfoods=user, one_user=one_user, the_title="add new userhasfood", touslesuser=touslesuser, touslesfood=touslesfood)


    touslesuser= query_db("select * from user")

    touslesfood= query_db("select * from food")

    user = query_db('select * from userhasfood')
    one_user = query_db("select * from userhasfood limit 1", one=True)
    return render_template("userhasfoodform.html", userhasfoods=user, one_user=one_user, the_title="add new userhasfood", touslesuser=touslesuser, touslesfood=touslesfood)

@app.route("/add_one_artisthassong", methods=["GET","POST"])
def add_one_artisthassong():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        touslesdiscosong= query_db("select * from discosong")

        one_user = query_db("insert into artisthassong (user_id,discosong_id) values (:user_id,:discosong_id)",hey)
        user = query_db('select * from artisthassong')

        return render_template("artisthassongform.html", artisthassongs=user, one_user=one_user, the_title="add new artisthassong", touslesuser=touslesuser, touslesdiscosong=touslesdiscosong)


    touslesuser= query_db("select * from user")

    touslesdiscosong= query_db("select * from discosong")

    user = query_db('select * from artisthassong')
    one_user = query_db("select * from artisthassong limit 1", one=True)
    return render_template("artisthassongform.html", artisthassongs=user, one_user=one_user, the_title="add new artisthassong", touslesuser=touslesuser, touslesdiscosong=touslesdiscosong)

@app.route("/add_one_city", methods=["GET","POST"])
def add_one_city():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into city (name) values (:name)",hey)
        user = query_db('select * from city')

        return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city")


    user = query_db('select * from city')
    one_user = query_db("select * from city limit 1", one=True)
    return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city")

@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey)
        user = query_db('select * from country')

        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_nightclub", methods=["GET","POST"])
def add_one_nightclub():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescity= query_db("select * from city")

        one_user = query_db("insert into nightclub (name,city_id) values (:name,:city_id)",hey)
        user = query_db('select * from nightclub')

        return render_template("nightclubform.html", nightclubs=user, one_user=one_user, the_title="add new nightclub", touslescity=touslescity)


    touslescity= query_db("select * from city")

    user = query_db('select * from nightclub')
    one_user = query_db("select * from nightclub limit 1", one=True)
    return render_template("nightclubform.html", nightclubs=user, one_user=one_user, the_title="add new nightclub", touslescity=touslescity)

@app.route("/add_one_nightclubhassong", methods=["GET","POST"])
def add_one_nightclubhassong():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesnightclub= query_db("select * from nightclub")

        touslesdiscosong= query_db("select * from discosong")

        one_user = query_db("insert into nightclubhassong (nightclub_id,discosong_id) values (:nightclub_id,:discosong_id)",hey)
        user = query_db('select * from nightclubhassong')

        return render_template("nightclubhassongform.html", nightclubhassongs=user, one_user=one_user, the_title="add new nightclubhassong", touslesnightclub=touslesnightclub, touslesdiscosong=touslesdiscosong)


    touslesnightclub= query_db("select * from nightclub")

    touslesdiscosong= query_db("select * from discosong")

    user = query_db('select * from nightclubhassong')
    one_user = query_db("select * from nightclubhassong limit 1", one=True)
    return render_template("nightclubhassongform.html", nightclubhassongs=user, one_user=one_user, the_title="add new nightclubhassong", touslesnightclub=touslesnightclub, touslesdiscosong=touslesdiscosong)

@app.route("/add_one_userhasnightclub", methods=["GET","POST"])
def add_one_userhasnightclub():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        touslesnightclub= query_db("select * from nightclub")

        one_user = query_db("insert into userhasnightclub (user_id,nightclub_id) values (:user_id,:nightclub_id)",hey)
        user = query_db('select * from userhasnightclub')

        return render_template("userhasnightclubform.html", userhasnightclubs=user, one_user=one_user, the_title="add new userhasnightclub", touslesuser=touslesuser, touslesnightclub=touslesnightclub)


    touslesuser= query_db("select * from user")

    touslesnightclub= query_db("select * from nightclub")

    user = query_db('select * from userhasnightclub')
    one_user = query_db("select * from userhasnightclub limit 1", one=True)
    return render_template("userhasnightclubform.html", userhasnightclubs=user, one_user=one_user, the_title="add new userhasnightclub", touslesuser=touslesuser, touslesnightclub=touslesnightclub)

@app.route("/add_one_userdating", methods=["GET","POST"])
def add_one_userdating():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        touslesotheruser= query_db("select * from otheruser")

        one_user = query_db("insert into userdating (user_id,otheruser_id) values (:user_id,:otheruser_id)",hey)
        user = query_db('select * from userdating')

        return render_template("userdatingform.html", userdatings=user, one_user=one_user, the_title="add new userdating", touslesuser=touslesuser, touslesotheruser=touslesotheruser)


    touslesuser= query_db("select * from user")

    touslesotheruser= query_db("select * from otheruser")

    user = query_db('select * from userdating')
    one_user = query_db("select * from userdating limit 1", one=True)
    return render_template("userdatingform.html", userdatings=user, one_user=one_user, the_title="add new userdating", touslesuser=touslesuser, touslesotheruser=touslesotheruser)

