from flask import Flask
from datetime import datetime
from flask import render_template, request
import pandas as pd
from flask import redirect, url_for
import datetime
import pickle
import os

# The code will run with model_gb2 (added to models folder). 
# make sure to adjust datatypes in df and number of features to your model to get it running

def create_app():
    '''Function that creates app'''
    
    # Create flask object
    app = Flask(__name__)
    
    # Homepage route
    @app.route('/', methods=["GET", "POST"])
    def root():
        '''Base view'''
        return render_template('next.html', title='Home')
    
    @app.route('/prediction_no', methods=["GET", "POST"])
    def prediction_no():
        return render_template ('predict_no.html', title='Prediction')

    @app.route('/prediction_yes', methods=["GET", "POST"])
    def prediction_yes():
        return render_template('predict_yes.html', title='Prediction')

    # User route
    @app.route('/user', methods=['GET', 'POST'])
    def user():
        '''User view - input page for users'''

        if request.method == 'POST':
            print('post request')
            dict1=request.values
            
            print(dict1)
            
            date1= dict1.get("date_created")
            date2= dict1.get("date_launched")
            date3 = datetime.datetime.strptime(date1,"%Y-%m-%d")
            date4 = datetime.datetime.strptime(date2,"%Y-%m-%d")
            unixtime = datetime.datetime.timestamp(date4)-datetime.datetime.timestamp(date3)
          
            columnlist=['index', 'country_code', 'month_created', 'backers_count',	'category',	'currency_code',	
            'project_length', 'goal', 'usd_pledged', 'staff_pick']
             
           
            values=[1, dict1.get("country_code"), int(dict1.get("month_launched")), int(dict1.get("backers_count")) ,dict1.get("category"),
            dict1.get("currency_code"),int(unixtime), float(dict1.get("goal")), float(dict1.get("usd_pledged")),float(dict1.get("staff_pick"))]
            df = pd.DataFrame(columns=columnlist)
            df.loc[len(df)] = values
            df.set_index(['index'], inplace=True)
            
            app_dir = os.path.dirname(os.path.abspath(__file__))
            filename =os.path.join(app_dir, 'model_gb2')
            grb_model = pickle.load(open(filename, 'rb'))

            y_pred = grb_model.predict(df)[0]
            if y_pred == 0:
               return redirect(url_for('prediction_no' ))
            else:
               return redirect(url_for('prediction_yes'))

    return app





