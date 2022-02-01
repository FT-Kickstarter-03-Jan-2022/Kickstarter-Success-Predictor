'''Kickstarter campaign predictor with Flask'''

from flask import Flask, render_template, request


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
            print(request.values)
            print('user function running')

        return render_template('next.html', title='User')


    return app

