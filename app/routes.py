import flask
from flask import render_template,jsonify
from app import app
from flask_pyoidc.provider_configuration import ProviderConfiguration, ClientMetadata
from flask_pyoidc.user_session import UserSession
from flask_pyoidc import OIDCAuthentication
import datetime
import os

app.config.update({'OIDC_REDIRECT_URI': os.environ.get('REDIRECT_URI'),
                   'SECRET_KEY': os.environ.get('SECRET'),  
                   'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=7).total_seconds(),
                   'DEBUG': True})

provider_config = ProviderConfiguration(
    issuer=os.environ.get('OAUTH_SERVER_URL'),
    client_metadata=ClientMetadata(os.environ.get('CLIENT_ID'), os.environ.get('SECRET')))

PROVIDER = 'provider'
auth = OIDCAuthentication({PROVIDER: provider_config}, app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/login')
@auth.oidc_auth(PROVIDER)
def login():
    user_session = UserSession(flask.session)
    user_data = {
        'access_token': user_session.access_token,
        'id_token': user_session.id_token,
        'userinfo': user_session.userinfo}
    return render_template('login.html', title='Login', data=user_data)

@app.route('/protected')
@auth.oidc_auth(PROVIDER)
def protected():
    return render_template('protected.html', title='Recurso protegido')

@app.route('/logout')
@auth.oidc_logout
def logout():
    return render_template('logout.html', title='Logout')

@auth.error_view
def error(error=None, error_description=None):
    return jsonify({'error': error, 'message': error_description})


