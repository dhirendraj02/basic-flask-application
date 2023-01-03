import sqlite3
from flask import Flask, render_template
import json
app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/meters/', methods=['GET'])
def meters():

    conn = get_db_connection()
    meters = conn.execute('SELECT * FROM meters').fetchall()
    conn.close()
    
    return render_template('index.html', meters=meters)

@app.route('/meters/<int:meter_id>', methods=['GET'])
def meter_data(meter_id):

    conn = get_db_connection()
    meter_data = conn.execute(f'SELECT * FROM meter_data where meter_id={meter_id} order by timestmp ASC').fetchall()
    conn.close()

    data = []
    for row in meter_data:

        data.append({'id':row[0],'meter_id':row[1],'value':row[2],'timestamp':row[3]})

    
    return json.dumps(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
