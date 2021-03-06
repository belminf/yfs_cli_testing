from libs.yfs_api import YFSAPI
from pprint import pprint
import yaml


def reauth():

    # Need to get code via web borwser
    print("Authenticate with Yahoo: {}".format(my_yfs.oauth.get_auth_url('https://cashews.belm.in/')))
    verify_code=input('Verify code: ')
    my_yfs.oauth.auth_session(verify_code, 'https://cashews.belm.in')

    # Save credentials
    with open('creds.yaml', 'w') as creds_config_file:
        yaml.dump(my_yfs.oauth.get_auth_config(), creds_config_file, default_flow_style=False, explicit_start=True)


# Load configuration
with open('creds.yaml', 'r') as creds_config_file:
    creds_config = yaml.load(creds_config_file)

# Initiate API object
my_yfs = YFSAPI(**creds_config)

# If no access token, get it via web browser workflow
if 'access_token' not in creds_config or not creds_config['access_token']:
    reauth()

# Print leagues
for x in (1, 2):
    try:
        leagues = my_yfs.get_leagues()
        break
    except Exception:
        reauth()

pprint(leagues)
