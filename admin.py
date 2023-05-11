import sqlite3
import app
from flask import url_for, redirect

con = sqlite3.connect('job_recommend.db')
cr = con.cursor()

cr.execute("create table if not exists admin(username TEXT, password TEXT)")

cr.execute("insert into admin values('admin', 'admin')")
con.commit()

@app.route('select')
def select():
    import telepot
    bot = telepot.Bot("6154690574:AAET6-I9f2GV1jVMPZhLoNe2Er8NByx1iBo")
    bot.sendMessage("1384687751", str('hi, you are selected'))
    return redirect(url_for('adminhome'))

@app.route('reject')
def reject():
    import telepot
    bot = telepot.Bot("6154690574:AAET6-I9f2GV1jVMPZhLoNe2Er8NByx1iBo")
    bot.sendMessage("1384687751", str('hi, you are rejected'))
    return redirect(url_for('adminhome'))
