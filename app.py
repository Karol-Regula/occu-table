#add links to CSV file, display all occupations and percentages in table

from flask import Flask, render_template
from utils import occuTable

app = Flask(__name__)

@app.route("/")
@app.route("/occupations/")
def printer ():
    occupationName = occuTable.randomOccupation()
    jobList = occuTable.occupations
    return render_template('occu-table.html', occupationName = occupationName, jobList = jobList)

if __name__ == '__main__':  #will not print if imported as module
    app.run(debug = True)
