# yfs_cli_testing

Testing Yahoo and YFS API with CLI utility.

## Install

    pip install -r requirements.txt

## Setup
For Oauth2, there are three credential values you require:

1. Client ID
2. Client secret
3. Authentication token

See below for application specific configuration.

### yahoo_oauth module
Client ID and secret could be created via [YDN console](https://developer.yahoo.com/apps/). The authentication token is generated after a web browser workflow that looks like the following:

1. After setting up a `YahooOauth` object with both the client ID and secret, request an authentication link via `YahooOauth.get_auth_url(callback_url)`.
2. Visit that link and acknowledge access permission.
3. You'll get redirected to the `callback_url` provided in step 1. In that URL, you'll see a `code` parameter. Grab that and provide it as the `verify_code` parameter to `YahooOauth.create_session(callback_url, verify_code)`.
4. The `YahooOauth.auth_session(...)` call will return the authorization token. You could also retrieve it via `YahooOauth.get_auth_config()`

The authorization token could be saved and re-used to necro a session.

### Example scripts
These are using YAML (`creds.yaml` in the CWD) to keep credential values. See [example config](config.yaml.example). Requires the following values:

* `base_url` - For Yahoo Sports, use `https://fantasysports.yahooapis.com/fantasy/v2/`
* `client_id` - Retrieve from [YDN console](https://developer.yahoo.com/apps/)
* `client_secret` - Retrieve from [YDN console](https://developer.yahoo.com/apps/)

You also need `access_token` but that could be generated via a browser workflow on first run of an example script.


