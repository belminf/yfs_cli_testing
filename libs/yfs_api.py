from .yahoo_oauth import YahooOauth


class YFSAPI:
    oauth = None

    def __init__(self, **kwargs):
        self.oauth = YahooOauth(**kwargs)

    def get_leagues(self):

        # Make request and get raw response
        r = self.oauth.get('users;use_login=1/games;seasons=2017;game_codes=nfl;/leagues')
        raw_leagues = r.json()['fantasy_content']['users']['0']['user'][1]['games']['0']['game'][1]['leagues']

        # Clean up response
        leagues = [raw_leagues[k]['league'][0] for k in raw_leagues.keys() if isinstance(raw_leagues[k], dict) and 'league' in raw_leagues[k]]

        return leagues

    def get_content(self, url):

        # Make request and get raw response
        r = self.oauth.get(url)
        raw_content = r.json()['fantasy_content']

        return raw_content
