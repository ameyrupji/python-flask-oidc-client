from authlib.integrations.flask_client import OAuth
from authlib.integrations.flask_oauth2 import ResourceProtector
from authlib.jose import jwt
from website import app

require_oauth = ResourceProtector()


oauth = OAuth(app)

AUTHORIZE_URL = 'http://localhost:5000/oauth/authorize'
AUTHORIZE_PARAMS = None
ACCESS_TOKEN_URL = 'http://localhost:5000/oauth/token'
ACCESS_TOKEN_PARAMS = None
API_BASE_URL = 'http://localhost:5000'
CLIENT_ID = 'hDihqlbEebpIbIjwSFrPkLo4'
CLIENT_SECRET = 'Cm34ECZ8eIqY98TJ7gI95iw5pm3AfQ6nomHZNZ7Zj75IUO4L'
CLIENT_KWARGS = { 'scope': 'openid email profile' }

# For automatic configurations
# CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'

oauth.register(
    name='local',
    # server_metadata_url=CONF_URL,

    access_token_url=ACCESS_TOKEN_URL,
    access_token_params=ACCESS_TOKEN_PARAMS,

    api_base_url=API_BASE_URL,

    authorize_url=AUTHORIZE_URL,
    authorize_params=AUTHORIZE_PARAMS,

    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    client_kwargs=CLIENT_KWARGS,
)


