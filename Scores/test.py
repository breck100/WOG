import requests

def get_advertisers(start_date, end_date):
    """
    Get a list of advertisers from the Ads Transparency Center API.

    Args:
        start_date: The start date of the query.
        end_date: The end date of the query.

    Returns:
        A list of advertisers.
    """

    url = "https://www.googleapis.com/ads/v1/advertisers"
    params = {
        "start_date": start_date,
        "end_date": end_date,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["advertisers"]
    else:
        print (response)
        raise Exception("Error getting advertisers: {}".format(response.status_code))


start_date = "2023-06-01"
end_date = "2023-06-03"
advertisers = get_advertisers(start_date, end_date)

for advertiser in advertisers:
    print(advertiser["name"])