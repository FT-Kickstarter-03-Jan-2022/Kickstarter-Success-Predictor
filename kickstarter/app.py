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
            feature_list=list(dict1.values())
            column_list=list(dict1.keys())
            df = pd.DataFrame(columns=column_list)
            df.loc[len(df)] = feature_list
            date1= dict1.get("date_created")
            date2= dict1.get("date_launched")
            date3 = datetime.datetime.strptime(date1,"%Y-%m-%d")
            date4 = datetime.datetime.strptime(date2,"%Y-%m-%d")
            unixtime = datetime.datetime.timestamp(date4)-datetime.datetime.timestamp(date3)
            
            print(unixtime)    
                  
        return render_template('next.html', title='User')

    
    return app


