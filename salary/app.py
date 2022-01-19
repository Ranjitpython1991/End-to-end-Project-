
from flask import Flask ,render_template ,request
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def salary ():
  model = pickle.load(open('model.pkl','rb')) 
  Experience= float(request.form.get('Experience'))
  prediction = model.predict([[Experience]])
  return render_template("index.html" ,result=prediction)
 
if __name__ =="__main__":  
    app.run(debug = True)  