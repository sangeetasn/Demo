from flask import Flask, render_template, request

from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'beml_1'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
con = mysql.connect()
cursor = con.cursor()

@app.route('/')
def index():
    return render_template('Beml_Format.html')

@app.route('/', methods=['POST'])
def authonticate():
    reference_number = request.form['Reference Number']
    date = request.form['Date']
    staff_number = request.form['Staff Number']
    staff_name = request.form['Staff Name']
    patient_name = request.form['Patient Name']
    patient_relationship = request.form['Patient Relationship']
    hospital_name = request.form['Hospital Name']
    hospital_address = request.form['Hospital Address']
    reason_for_hospitality = request.form['Reason for Hospitality']
    signature = request.form['signature']
    patient_photo = request.form['Patient_Photo']

    cursor.execute("INSERT INTO costumer_data(Reference_Number,Date,Staff_Number,Staff_Name,Patient_Name,Patient_Relationship,Hospital_Name,Hospital_Adrdress,Reason_For_Hospitality,Signature,Patient_Photo) \
     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                   (reference_number, date, staff_number, staff_name, patient_name, patient_relationship, hospital_address, hospital_name,
                    reason_for_hospitality, signature, patient_photo))
    con.commit()
    return "Data inserted successfully"


if __name__ == "__main__":
    app.run(debug=True)













