from flask import Flask, render_template, request, redirect, url_for
import traceback
from db_orm import *
from sqlalchemy import create_engine, select
from sqlalchemy_utils import database_exists, create_database

app = Flask(__name__)

printable_char_set = "[a-zA-Z0-9\/*-_àçéèùïüë]+"
absolute_path=''
engine = create_engine('sqlite:///test.db', echo=True)
Base.metadata.create_all(engine)

class RequetDb:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()



    def get_datas(self):
        try:
            print("ok")
            print(self.session.query(Line).all())
            return self.session.execute(select(Line))


        except Exception as e:
            traceback.print_exc()
            # raise e
        pass

    def save_datas(self, firstname, lastname):
        try:
            line = Line(firstname=firstname,lastname=lastname)
            self.session.add(line)
            self.session.commit()
            self.session.flush()
            self.session.refresh(line)
            return line.id
        except Exception as e:
            self.session.rollback()
            traceback.print_exc()
            # raise e

        pass





@app.route('/')
@app.route('/home')
@app.route('/load_db_datas')
def load_db_datas():
    db = RequetDb()
    datas = db.get_datas()
    print("datas en cours")
    print(datas)
    return render_template('index.html', datas = datas)

@app.route('/set_db_datas', methods=['GET'])
def set_db_datas():
    db = RequetDb()
    result = request.args
    firstname = result['firstname']
    lastname = result['lastname']
    db.save_datas(firstname, lastname)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
