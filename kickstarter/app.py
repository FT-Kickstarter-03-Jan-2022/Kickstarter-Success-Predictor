from flask import Flask
from datetime import datetime
from flask import render_template, request
import pandas as pd
import datetime
import pickle

# The code will run with model_gb2 (added to models folder). The 'staff pick' feature was disabled in current next.html 
# version so I replaced it
# with dummy value in a dataframe, it should be enbled in html to get accurate predictions 
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
    

    # User route
    @app.route('/user', methods=['GET', 'POST'])
    def user():
        '''User view - input page for users'''

        if request.method == 'POST':
            print('post request')
            dict1=request.values
            
            print('user function running')
            
            date1= dict1.get("date_created")
            date2= dict1.get("date_launched")
            date3 = datetime.datetime.strptime(date1,"%Y-%m-%d")
            date4 = datetime.datetime.strptime(date2,"%Y-%m-%d")
            unixtime = datetime.datetime.timestamp(date4)-datetime.datetime.timestamp(date3)
          
            columnlist=['index', 'country_code', 'month_created', 'backers_count',	'category',	'currency_code',	
            'project_length', 'goal', 'usd_pledged', 'staff_pick']
           
            values=[1, dict1.get("country_code"), int(dict1.get("month_launched")), int(dict1.get("backers_count")) ,dict1.get("category"),
             dict1.get("currency_code"),int(unixtime), float(dict1.get("goal")), float(dict1.get("usd_pledged")),0]
            df = pd.DataFrame(columns=columnlist)
            df.loc[len(df)] = values
            df.set_index(['index'], inplace=True)
            
            filename = 'model_gb2'
            grb_model = pickle.load(open(filename, 'rb'))

            y_pred = grb_model.predict(df)[0]
            print(y_pred)
            print(df.dtypes)    
                
                  
        return render_template('next.html', title='User')

	
    
    return app


