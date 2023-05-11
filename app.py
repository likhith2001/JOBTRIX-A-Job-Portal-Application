from smtplib import SMTPException
from flask import Flask, render_template,  request, redirect, url_for, flash, jsonify
#render_template to convert to html page, flash- to intialize app, request- html data form request, redirect- call python fns from the main code file
import sqlite3
import base64 #to store img in form of bytes and print the bytes image on html page
import pickle #load ML pkl model file
import json #web scrapping 
import requests #web scrapping
import time
import csv
from pprint import pprint
from forms import ContactForm
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'development key'
app.secret_key = 'my_secrest_key'
mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'nammi16march@gmail.com'
app.config["MAIL_PASSWORD"] = 'klbszdesuyhivjhg'
mail.init_app(app)

with open('xgb_v2.pkl', 'rb') as f:
    pickled_model = pickle.load(f)

roll=['AI ML Specialist','API Specialist','Application Support Engineer','Business Analyst','Customer Service Executive', 'Cyber Security Specialist','Data Scientist'
    ,'Database Administrator','Graphics Designer','Hardware Engineer','Helpdesk Engineer','Information Security Specialist','Networking Engineer',
    'Project Manager','Software Developer','Software tester','Technical Writer']

connection = sqlite3.connect('job_recommend.db')
curcsor = connection.cursor()

curcsor.execute("CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, mobile TEXT, gmail TEXT, profile BLOB, resume TEXT)")
curcsor.execute("create table if not exists academics(gmail TEXT, course TEXT, university TEXT, result TEXT, passout TEXT)")
curcsor.execute("create table if not exists summury(gmail TEXT, summuries TEXT)")
curcsor.execute("create table if not exists activity(gmail TEXT, activities TEXT)")
curcsor.execute("create table if not exists strength(gmail TEXT, strengths TEXT)")
curcsor.execute("create table if not exists personal(fname TEXT, lname TEXT, bday TEXT, gender TEXT, pnum TEXT, gmail TEXT, caddress TEXT, paddress TEXT, languages TEXT, marital TEXT, declaration TEXT)")
curcsor.execute("create table if not exists other(objective TEXT, skill TEXT, tool TEXT, db TEXT, sos TEXT , title TEXT, srvr TEXT, pos TEXT, team TEXT, tech TEXT, desp TEXT, gmail TEXT)")
curcsor.execute("create table if not exists jobs(title TEXT, applylink TEXT, jobdescription TEXT, companyname TEXT, location TEXT, salary TEXT, skills TEXT, enddate TEXT, source TEXT, experience TEXT, gmail TEXT)")

@app.route('/contact', methods = ['GET','POST'])
def contact():
    form = ContactForm()
    
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msgg = Message(form.subject.data, sender='nammi16march@gmail.com', recipients=['nammi16march@gmail.com'])
            msgg.body = """ From: %s <%s> %s """ % (form.name.data, form.email.data, form.message.data)
        # if app.config['mail']:
        #     try:
            mail.send(msgg)
        #     except SMTPException as e:
        #         app.logger.error(e.message)
        # else:
        #     print(msgg.html)
        connection = sqlite3.connect('job_recommend.db')
        cursor = connection.cursor()

        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        List =  [name, email, subject, message]
        cursor.execute("INSERT INTO contact VALUES (?, ?, ?, ?)", List)
        connection.commit()


        return render_template('index.html', msg='Query submitted!  We will get back to you soon')
    elif request.method == 'GET':
        return render_template('contact.html', form=form)    

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/landinguser')
def landinguser():
    return render_template('landinguser.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buildresume')
def buildresume():
    f = open('session.txt', 'r')
    email = f.read()
    f.close()
    return render_template('buildresume.html', email=email)

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        skill1 = request.form['skill1']
        skill2 = request.form['skill2']
        skill3 = request.form['skill3']
        skill4 = request.form['skill4']
        skill5 = request.form['skill5']
        skill6 = request.form['skill6']
        skill7 = request.form['skill7']
        skill8 = request.form['skill8']
        skill9 = request.form['skill9']
        skill10 = request.form['skill10']
        skill11 = request.form['skill11']
        skill12 = request.form['skill12']
        skill13 = request.form['skill13']
        skill14 = request.form['skill14']
        skill15 = request.form['skill15']
        skill16 = request.form['skill16']
        skill17 = request.form['skill17']
        data = [skill1, skill2, skill3, skill4, skill5, skill6, skill7, skill8, skill9, skill10, skill11, skill12, skill13, skill14, skill15, skill16, skill17]
        print(data)
        import pickle
        import sklearn
        clf=pickle.load(open("xgb_v2.pkl","rb"))
        import pandas as pd
        df=pd.read_csv("changed.csv")
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        df['Role'] = le.fit_transform(df['Role'])

        # Make job recommendations for a new candidate
        ##new_candidate=([[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
        new_candidate = pd.DataFrame({
            'Database Fundamentals': data[0]                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ,
            'Computer Architecture': data[1],
            'Distributed Computing Systems': data[2],
            'Cyber Security': data[3],
            'Networking': data[4],
            'Software Development': data[5],
            'Programming Skills': data[6],
            'Project Management': data[7],
            'Computer Forensics Fundamentals': data[8],
            'Technical Communication':data[9],
            'AI ML': data[10],
            'Software Engineering': data[11],
            'Business Analysis': data[12],
            'Communication skills': data[13],
            'Data Science': data[14],
            'Troubleshooting skills': data[15],
            'Graphics Designing':data[16]
        }, index=[0])
        prediction = clf.predict(new_candidate)
        recommended_role = le.inverse_transform(prediction)
        print('Recommended role:', recommended_role[0])

        # skills = []
        # for key in data:
        #     skills.append(int(data[key]))
        # print(skills)
        # out = pickled_model.predict([skills])
        # print(roll[out[0]])
        return render_template('jobs.html', pred=recommended_role[0])
    return render_template('jobs.html')

@app.route('/profile1')
def profile1():
    connection = sqlite3.connect('job_recommend.db')
    cursor = connection.cursor()
    
    f = open('session.txt', 'r')
    email = f.read()
    f.close()

    cursor.execute("SELECT resume FROM user WHERE gmail = '"+email+"'")
    result = cursor.fetchone()
    print(result[0])

    if result[0] == 'yes':
        cursor.execute("SELECT profile FROM user WHERE gmail = '"+email+"'")
        dp = cursor.fetchone()

        cursor.execute("SELECT * FROM other WHERE gmail = '"+email+"'")
        result = cursor.fetchone()
        
        objective, skill, tool, db, sos, title, srvr, pos, team, tech, desp = result[:-1]

        cursor.execute("SELECT * FROM personal WHERE gmail = '"+email+"'")
        result = cursor.fetchone()

        fname, lname, bday, gender, pnum, gid, caddress, paddress, languages, marital, declaration = result
        fullname = fname+' '+lname

        cursor.execute("SELECT course, university, result, passout FROM academics WHERE gmail = '"+email+"'")
        academic = cursor.fetchall()

        cursor.execute("SELECT summuries FROM summury WHERE gmail = '"+email+"'")
        summury = cursor.fetchall()

        cursor.execute("SELECT activities FROM activity WHERE gmail = '"+email+"'")
        activity = cursor.fetchall()

        cursor.execute("SELECT strengths FROM strength WHERE gmail = '"+email+"'")
        strength = cursor.fetchall()

        cursor.execute("SELECT profile FROM user WHERE gmail = '"+email+"'")
        dp = cursor.fetchone()
        dp = dp[0].decode('utf-8')

        return render_template('profile1.html', dp=dp, ud=result[0], objective=objective, declaration=declaration,marital=marital,
            languages=languages,paddress=paddress, caddress=caddress,gid=gid,pnum=pnum,gender=gender,bday=bday,
            fullname=fullname,lname=lname,fname=fname,strength=strength,activities=activity,desp=desp,tech=tech,
            team=team,pos=pos,srvr=srvr,title=title,sos=sos,db=db,tool=tool,skill=skill,summury=summury,academic=academic)
    else:
        return render_template('profile1.html')

@app.route('/download')
def download():
    connection = sqlite3.connect('job_recommend.db')
    cursor = connection.cursor()
    
    f = open('session.txt', 'r')
    email = f.read()
    f.close()

    cursor.execute("SELECT * FROM other WHERE gmail = '"+email+"'")
    result = cursor.fetchone()
    
    objective, skill, tool, db, sos, title, srvr, pos, team, tech, desp = result[:-1]

    cursor.execute("SELECT * FROM personal WHERE gmail = '"+email+"'")
    result = cursor.fetchone()

    fname, lname, bday, gender, pnum, gid, caddress, paddress, languages, marital, declaration = result
    fullname = fname+' '+lname

    cursor.execute("SELECT course, university, result, passout FROM academics WHERE gmail = '"+email+"'")
    academic = cursor.fetchall()

    cursor.execute("SELECT summuries FROM summury WHERE gmail = '"+email+"'")
    summury = cursor.fetchall()

    cursor.execute("SELECT activities FROM activity WHERE gmail = '"+email+"'")
    activity = cursor.fetchall()

    cursor.execute("SELECT strengths FROM strength WHERE gmail = '"+email+"'")
    strength = cursor.fetchall()

    return render_template('resume.html', ud=result[0], objective=objective, declaration=declaration,marital=marital,
        languages=languages,paddress=paddress, caddress=caddress,gid=gid,pnum=pnum,gender=gender,bday=bday,
        fullname=fullname,lname=lname,fname=fname,strength=strength,activities=activity,desp=desp,tech=tech,
        team=team,pos=pos,srvr=srvr,title=title,sos=sos,db=db,tool=tool,skill=skill,summury=summury,academic=academic)

@app.route('/adminlog', methods=['GET', 'POST'])
def adminlog():
    if request.method == 'POST':

        connection = sqlite3.connect('job_recommend.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']

        cursor.execute("SELECT username, password FROM admin WHERE username = '"+name+"' AND password= '"+password+"'")
        result = cursor.fetchall()

        if len(result) == 0:
            return render_template('index.html', msg='Sorry, Incorrect Credentials Provided,  Try Again')
        else:
            cursor.execute("SELECT * FROM user")
            result = cursor.fetchall()
            return render_template('adminpage.html', result=result)

    return render_template('index.html')

@app.route('/userlog', methods=['GET', 'POST'])
def userlog():
    if request.method == 'POST':

        connection = sqlite3.connect('job_recommend.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']

        cursor.execute("SELECT name, password FROM user WHERE name = '"+name+"' AND password= '"+password+"'")
        result = cursor.fetchall()

        if len(result) == 0:
            return render_template('index.html', msg='Sorry, Incorrect Credentials Provided,  Try Again')
        else:
            cursor.execute("SELECT gmail FROM user WHERE name = '"+name+"' AND password= '"+password+"'")
            result = cursor.fetchone()
            
            f = open('session.txt', 'w')
            f.write(result[0])
            f.close()

            return redirect(url_for('landinguser'))

    return render_template('index.html')


@app.route('/userreg', methods=['GET', 'POST'])
def userreg():
    if request.method == 'POST':

        connection = sqlite3.connect('job_recommend.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        dp = request.form['dp']
        
        cursor.execute("SELECT * FROM user WHERE gmail = '"+email+"'")
        result = cursor.fetchall()

        if len(result) == 0:
            with open(dp, "rb") as img_file:
                my_string = base64.b64encode(img_file.read())
            
            List =  [name, password, mobile, email, my_string, 'no']
            cursor.execute("INSERT INTO user VALUES (?, ?, ?, ?, ?, ?)", List)
            connection.commit()

            return render_template('index.html', msg='Successfully Registered')
        else:
            return render_template('index.html', msg='Email already exists')

    return render_template('index.html')

@app.route('/resume', methods=['GET', 'POST'])
def resume():
    if request.method == 'POST':
        objective = request.form['objective']
        skill = request.form['skill']
        tool = request.form['tool']
        db = request.form['db']
        sos = request.form['sos']
        title = request.form['title']
        srvr = request.form['srvr']
        pos = request.form['pos']
        team = request.form['team']
        tech = request.form['tech']
        desp = request.form['desp']

        fname = request.form['fname'] 
        lname = request.form['lname']
        fullname = fname+' '+lname
        bday = request.form['bday']
        gender = request.form['gender']
        pnum = request.form['pnum']
        gid = request.form['gid']
        caddress = request.form['caddress']
        paddress = request.form['paddress']
        languages = request.form['languages']
        marital = request.form['marital']
        declaration = request.form['declaration']

        other_info = [objective, skill, tool, db, sos, title, srvr, pos, team, tech, desp, gid]
        personal_info = [fname, lname, bday, gender, pnum, gid, caddress, paddress, languages, marital, declaration]
        academic=[]
        i=0
        while True:
            try:
                course = request.form['course['+str(i)+']']
                university = request.form['university['+str(i)+']']
                result = request.form['result['+str(i)+']']
                passout = request.form['passout['+str(i)+']']
                academic.append([gid, course, university, result,  passout])
                i += 1
            except Exception as e:
                print(str(e))
                break    
        summury = [] 
        j=0
        while True:
            try:
                sm = request.form['summury['+str(j)+']']
                summury.append([gid, sm])
                j += 1
            except Exception as e:
                print(str(e))
                break
       
        activities = [] 
        k=0
        while True:
            try:
                ac = request.form['activities['+str(k)+']']
                activities.append([gid, ac])
                k += 1
            except Exception as e:
                print(str(e))
                break
        
        strength = [] 
        l=0
        while True:
            try:
                st = request.form['strength['+str(l)+']']
                strength.append([gid, st])
                l += 1
            except Exception as e:
                print(str(e))
                break
        
        print(objective, declaration,marital,languages,paddress
        ,caddress,gid,pnum,gender,bday,fullname,lname,fname,strength,
        activities,desp,tech,team,pos,srvr,title,sos,db,tool,skill,summury,academic)

        connection = sqlite3.connect('job_recommend.db')
        cursor = connection.cursor()

        for row in academic:
            cursor.execute("insert into academics values(?, ?, ?, ?, ?)", row)
            connection.commit()

        for row in summury:
            cursor.execute("insert into summury values(?, ?)", row)
            connection.commit()
        
        for row in activities:
            cursor.execute("insert into activity values(?, ?)", row)
            connection.commit()
        
        for row in strength:
            cursor.execute("insert into strength values(?, ?)", row)
            connection.commit()

        cursor.execute("insert into personal values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", personal_info)
        connection.commit()
        
        cursor.execute("insert into other values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", other_info)
        connection.commit()

        cursor.execute("update user set resume = 'yes' where gmail = '"+gid+"'")
        connection.commit()

        return redirect(url_for('profile1'))
    return render_template('index.html')

@app.route('/logout')
def logout():
    return render_template('index.html')

@app.route('/posts/<job>')
def posts(job):
    print(job)
    try:
        timestamp = time.time()
        headers = json.load(open('headers.json'))
        json_filename = './files/timesjobs.json'
        fp = open(json_filename, 'w')

        url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=198130$&aosValues=&sortby=Y&from=filter&faids=&txtKeywords='+job+'&pSize=19'
        response = requests.get(url)
        jobs = json.loads(response.text)
        jobs = jobs['jobsList']

        joblist = []
        heading = ['title', 'apply link', 'job description', 'company name', 'location', 'salary', 'skills', 'enddate', 'source', 'experience']
        pprint(heading)
        for job in jobs:
            row = dict.fromkeys(headers)
            title = job['title']
            applylink = 'http://www.timesjobs.com/candidate/' + job['jdUrl']
            jd = job['jobDesc']
            companyname = job['companyName']
            location = job['Location']
            salary = job['salary']
            skills = ", ".join([x.strip().strip("\"") for x in job['keySkills']])
            enddate = job['expiry']
            source = 'timesjobs'
            experience = job['experience'] + " yrs"
            joblist.append([title, applylink, jd, companyname, location, salary, skills, enddate, source, experience])
            pprint([title, applylink, jd, companyname, location, salary, skills, enddate, source, experience])            
        json.dump(joblist, fp)
        fp.close()
        return render_template('posts.html', joblist=joblist, heading=heading)

    except Exception as ex:
        return render_template('posts.html', msg='posts not found')

@app.route('/jobsearch', methods=['GET', 'POST'])
def jobsearch():
    if request.method == 'POST':
        job = request.form['job']
        try:
            timestamp = time.time()
            headers = json.load(open('headers.json'))
            json_filename = './files/timesjobs.json'
            fp = open(json_filename, 'w')
            
            url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=198130$&aosValues=&sortby=Y&from=filter&faids=&txtKeywords='+job+'&pSize=19'
            response = requests.get(url)
            jobs = json.loads(response.text)
            jobs = jobs['jobsList']

            joblist = []
            heading = ['title', 'apply link', 'job description', 'company name', 'location', 'salary', 'skills', 'enddate', 'source', 'experience']
            pprint(heading)
            for job in jobs:
                row = dict.fromkeys(headers)
                title = job['title']
                applylink = 'http://www.timesjobs.com/candidate/' + job['jdUrl']
                jd = job['jobDesc']
                companyname = job['companyName']
                location = job['Location']
                salary = job['salary']
                skills = ", ".join([x.strip().strip("\"") for x in job['keySkills']])
                enddate = job['expiry']
                source = 'timesjobs'
                experience = job['experience'] + " yrs"
                joblist.append([title, applylink, jd, companyname, location, salary, skills, enddate, source, experience])
                pprint([title, applylink, jd, companyname, location, salary, skills, enddate, source, experience])            
            json.dump(joblist, fp)
            fp.close()
 
            return render_template('allpost.html', joblist=joblist, heading=heading)

        except Exception as ex:
            return render_template('allpost.html', msg='posts not found')
    
    return render_template('index.html')


@app.route('/view/<email>')
def view(email):
    connection = sqlite3.connect('job_recommend.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM other WHERE gmail = '"+email+"'")
    result = cursor.fetchone()
    
    objective, skill, tool, db, sos, title, srvr, pos, team, tech, desp = result[:-1]

    cursor.execute("SELECT * FROM personal WHERE gmail = '"+email+"'")
    result = cursor.fetchone()

    fname, lname, bday, gender, pnum, gid, caddress, paddress, languages, marital, declaration = result
    fullname = fname+' '+lname

    cursor.execute("SELECT course, university, result, passout FROM academics WHERE gmail = '"+email+"'")
    academic = cursor.fetchall()

    cursor.execute("SELECT summuries FROM summury WHERE gmail = '"+email+"'")
    summury = cursor.fetchall()

    cursor.execute("SELECT activities FROM activity WHERE gmail = '"+email+"'")
    activity = cursor.fetchall()

    cursor.execute("SELECT strengths FROM strength WHERE gmail = '"+email+"'")
    strength = cursor.fetchall()

    return render_template('viewresume.html', ud=result[0], objective=objective, declaration=declaration,marital=marital,
        languages=languages,paddress=paddress, caddress=caddress,gid=gid,pnum=pnum,gender=gender,bday=bday,
        fullname=fullname,lname=lname,fname=fname,strength=strength,activities=activity,desp=desp,tech=tech,
        team=team,pos=pos,srvr=srvr,title=title,sos=sos,db=db,tool=tool,skill=skill,summury=summury,academic=academic)

@app.route('/appliedjobs')
def appliedjobs():
    f = open('session.txt', 'r')
    email = f.read()
    f.close()

    connection = sqlite3.connect('job_recommend.db')
    cursor = connection.cursor()

    cursor.execute("select * from jobs where gmail = '"+email+"'")
    joblist = cursor.fetchall()

    heading = ['title', 'apply link', 'job description', 'company name', 'location', 'salary', 'skills', 'enddate', 'source', 'experience']
    return render_template('appliedjobs.html', joblist=joblist, heading=heading)

@app.route('/applied_jobs/<In>')
def applied_jobs(In):
    f = open('session.txt', 'r')
    email = f.read()
    f.close()

    data = json.load(open('./files/timesjobs.json'))
    data = data[int(In)]

    data.append(email)

    print(data)

    connection = sqlite3.connect('job_recommend.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO jobs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)

    # cursor.execute("update user set applied = 'yes' where gmail = '"+email+"'")
    connection.commit()
    connection.commit()

    import telepot
    bot = telepot.Bot('6154690574:AAET6-I9f2GV1jVMPZhLoNe2Er8NByx1iBo')
    bot.sendMessage('1384687751', str('Successfully applied for job {}'.format(data[1])))
    return redirect(url_for('appliedjobs'))

# @app.route('/view1/<email>')
# def view1(email):
#     connection = sqlite3.connect('job_recommend.db')
#     cursor = connection.cursor()

#     cursor.execute("SELECT * FROM jobs WHERE gmail = '"+email+"'")
#     result = cursor.fetchone()
#     title, applylink, jobdescription, companyname, salary, skills, location, enddate, source, experience = result[:-1]

#     # cursor.execute("SELECT * FROM personal WHERE gmail = '"+email+"'")
#     # result = cursor.fetchone()

#     # # fname, lname, bday, gender, pnum, gid, caddress, paddress, languages, marital, declaration = result
#     # # fullname = fname+' '+lname

#     # cursor.execute("SELECT course, university, result, passout FROM academics WHERE gmail = '"+email+"'")
#     # academic = cursor.fetchall()

#     # cursor.execute("SELECT summuries FROM summury WHERE gmail = '"+email+"'")
#     # summury = cursor.fetchall()

#     # cursor.execute("SELECT activities FROM activity WHERE gmail = '"+email+"'")
#     # activity = cursor.fetchall()

#     # cursor.execute("SELECT strengths FROM strength WHERE gmail = '"+email+"'")
#     # strength = cursor.fetchall()
#     cursor.execute("SELECT * FROM personal WHERE gmail = '"+email+"'")
#     result = cursor.fetchone()

#     cursor.execute("SELECT title FROM jobs WHERE gmail = '"+email+"'")
#     title = cursor.fetchall()

#     cursor.execute("SELECT applylink FROM jobs WHERE gmail = '"+email+"'")
#     applylink = cursor.fetchall()

#     cursor.execute("SELECT jobdescription FROM jobs WHERE gmail = '"+email+"'")
#     jobdescription = cursor.fetchall()

#     cursor.execute("SELECT companyname FROM jobs WHERE gmail = '"+email+"'")
#     companyname = cursor.fetchall()

#     cursor.execute("SELECT salary FROM jobs WHERE gmail = '"+email+"'")
#     salary = cursor.fetchall()

#     cursor.execute("SELECT skills FROM jobs WHERE gmail = '"+email+"'")
#     skills = cursor.fetchall()

#     cursor.execute("SELECT location FROM jobs WHERE gmail = '"+email+"'")
#     location = cursor.fetchall()

#     cursor.execute("SELECT enddate FROM jobs WHERE gmail = '"+email+"'")
#     enddate = cursor.fetchall()

#     cursor.execute("SELECT source FROM jobs WHERE gmail = '"+email+"'")
#     source = cursor.fetchall()

#     cursor.execute("SELECT experience FROM jobs WHERE gmail = '"+email+"'")
#     experience = cursor.fetchall()

#     return render_template('appliedjobs.html', ud=result[0], title=title, applylink=applylink, jobdescription=jobdescription, 
#                                companyname=companyname, salary=salary, skills=skills, location=location, enddate=enddate, 
#                                source=source, experience=experience)

@app.route('/appliedjobsadmin')
def appliedjobsadmin():
    f = open('session.txt', 'r')
    email = f.read()
    f.close()

    connection = sqlite3.connect('job_recommend.db')
    cursor = connection.cursor()

    cursor.execute("select * from jobs where gmail = '"+email+"'")
    joblist = cursor.fetchall()

    heading = ['title', 'apply link', 'job description', 'company name', 'location', 'salary', 'skills', 'enddate', 'source', 'experience']
    return render_template('appliedjobsadmin.html', joblist=joblist, heading=heading)

@app.route('/applied_jobsadmin/<In>')
def applied_jobsadmin(In):
    f = open('session.txt', 'r')
    email = f.read()
    f.close()

    data = json.load(open('./files/timesjobs.json'))
    data = data[int(In)]

    data.append(email)

    print(data)

    connection = sqlite3.connect('job_recommend.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO jobs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    connection.commit()

#endpoint for search
# @app.route('/search1', methods=['GET', 'POST'])
# def search1():
#     if request.method == "POST":
#         user = request.form['name']
#         # search by author or book
#         curcsor.execute("SELECT name, gmail from user WHERE name LIKE %s OR email LIKE %s", (user, user))
#         connection.commit()
#         data = curcsor.fetchall()
#         # all in the search box will return all the tuples
#         if len(data) == 0 and book == 'all': 
#             curcsor.execute("SELECT name, gmail from user")
#             connection.commit()
#             data = curcsor.fetchall()
#         return render_template('adminpage.html', data=data)
#     return render_template('adminpage.html')

@app.route('/update_pass', methods=['GET', 'POST'])
def update_pass():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        otp = int(request.form['otp'])

        f = open('OTP.txt', 'r')
        otp1 = f.readline()
        otp1 = int(otp1)
        f.close()

        if otp == otp1:
            con = sqlite3.connect('job_recommend.db')
            cr = con.cursor()
            cr.execute("update user set password = '"+password+"' where gmail = '"+email+"' ")
            con.commit()

            return render_template('index.html', msg="password updated successfully")
        return render_template('index.html', msg="Entered wrong otp")
    return render_template('index.html')

@app.route('/getotp')
def getotp():
    import random
    number = random.randint(1000,9999)
    number = str(number)
    print(number)
    f = open('OTP.txt', 'w')
    f.write(number)
    f.close()
    import telepot
    bot = telepot.Bot("6154690574:AAET6-I9f2GV1jVMPZhLoNe2Er8NByx1iBo")
    bot.sendMessage("1384687751", str(number))
    return jsonify('otp sent')

@app.route('/adminhome')
def adminhome():
    connection = sqlite3.connect('job_recommend.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user")
    result = cursor.fetchall()
    return render_template('adminpage.html', result=result)

@app.route('/select/<email>')
def select(email):
    print(email)
    import telepot
    bot = telepot.Bot("6154690574:AAET6-I9f2GV1jVMPZhLoNe2Er8NByx1iBo")
    bot.sendMessage("1384687751", str('Hello {}, your resume has been shortlisted, Kindly monitor your inbox for further updates regarding your application'.format(email)))
    return redirect(url_for('adminhome'))

@app.route('/reject/<email>')
def reject(email):
    print(email)
    import telepot
    bot = telepot.Bot("6154690574:AAET6-I9f2GV1jVMPZhLoNe2Er8NByx1iBo")
    bot.sendMessage("1384687751", str('Hello {}, your resume has been rejected. We wish you luck on your future endeavors'.format(email)))
    return redirect(url_for('adminhome'))

@app.route('/quizpython')
def quizpython():
    return render_template('quizpython.html')

@app.route('/quizjava')
def quizjava():
    return render_template('quizjava.html')

@app.route('/quizhtml')
def quizhtml():
    return render_template('quizhtml.html')

@app.route('/quizcss')
def quizcss():
    return render_template('quizcss.html')

@app.route('/quizjs')
def quizjs():
    return render_template('quizjs.html')

@app.route('/quizlanding')
def quizlanding():
    return render_template('quizlanding.html')

@app.route('/quiz')
def quiz():
    return render_template('quizlanding.html')
@app.route("/exam",methods=["POST","GET"])
def exam():
    if request.method == 'POST':
        data = request.form
        print("===================================")
        print(data)
        user_answers = []
        for key in data:
            user_answers.append(int(data[key]))
            
        print(user_answers)
        answers = [3,4,1,1,3]
        score = 0
        
        for i in range(5):
            if user_answers[i] == answers[i]:
                score = score + 5
        print(score)
        if score >= 20:
            text="You Are Excellent !!"
        elif (score >= 10 and score < 20):
            text="You Can Be Better !!"
        else:
            text="You Should Work Hard !!"
            
        print("===================================")
        return jsonify(text)
    return jsonify("error")

@app.route('/select1')
def select1():
    import telepot
    bot = telepot.Bot("6154690574:AAET6-I9f2GV1jVMPZhLoNe2Er8NByx1iBo")
    bot.sendMessage("1384687751", str('Hello, the company of your interest has sent you an update on one/more applications. Kindly check your inbox.'))
    return redirect(url_for('adminhome'))

if __name__ == "__main__":
    app.run(debug=True)