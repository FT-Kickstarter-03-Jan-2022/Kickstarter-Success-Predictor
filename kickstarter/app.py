from flask import Flask
from datetime import datetime
import json
from flask import render_template, request
import pandas as pd
import datetime
  

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
          
            columnlist=['country_code',	'month_created', 'backers_count',	'category',	'currency_code',	
            'project_length', 'goal', 'usd_pledged', 'staff_pick']

            values=[dict1.get("country_code"),dict1.get("month_launched"),dict1.get("backers_count"),dict1.get("category"),
            dict1.get("currency_code"),unixtime,dict1.get("goal"),dict1.get("usd_pledged"),dict1.get("staff_pick")]

            df = pd.DataFrame(columns=columnlist)
            df.loc[len(df)] = values
            
            print(df)    
            print(dict1)    

    
    return app


