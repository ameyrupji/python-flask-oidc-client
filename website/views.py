from flask import Blueprint, request, session, url_for
from flask import render_template, redirect, jsonify
from website import app
from .models import db
from .oauth2 import require_oauth, oauth

bp = Blueprint(__name__, 'home')

@bp.route('/', methods=['GET', 'POST'])
def homepage():
    user = session.get('user')
    return render_template('home.html', user=user)

@bp.route('/about')
def about():
  return {
    "app": "SSO - Client"
  }

@bp.route('/login', methods=['GET', 'POST'])
def login():
    redirect_uri = url_for('website.views.auth', _external=True)
    return oauth.local.authorize_redirect(redirect_uri)


@bp.route('/auth', methods=['GET', 'POST'])
def auth():
    print(request)
    token = oauth.local.authorize_access_token()
    print(token)
    print(token['id_token'])

    from authlib.jose import JsonWebToken, JWTClaims
    jwt = JsonWebToken(['HS256'])
    claims = jwt.decode(token['id_token'], key='')

    # print(claims)
    # print(claims.validate())
    user = oauth.local.get('/userinfo').json()

    session['user'] = user
    return redirect('/')


@bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


app.register_blueprint(bp, url_prefix='')