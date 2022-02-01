'''Kickstarter campaign predictor with Flask'''

from flask import Flask, render_template, request


def create_app():
    '''Function that creates app'''
    
    # Create flask object
    app = Flask(__name__)
    
    # # Homepage route
    # @app.route('/')
    # def home_page():
    #     '''Home view - returns a marketing page'''
    #     return render_template('next.html', title='Home')
    

    # User route
    @app.route('/user', methods=['GET', 'POST'])
    
    results = []
    
    def user():
        '''User view - input page for users'''
        results.append(
            (request.next.get("date_created"),
            request.next.get("date_launched"),
            request.next.get("number_of_backers"),
            request.next.get("goal_amount"),
            request.next.get("usd_pledged"),
            request.next.get("month_launched"),
            request.next.get("category"),
            request.next.get("country_code"),
            request.next.get("currency_code"),
            request.next.get("is_it_a_staff_pick?"),
            request.next.get("spotlight"))
            )

        return render_template('next.html', title='User')

        
    return app

