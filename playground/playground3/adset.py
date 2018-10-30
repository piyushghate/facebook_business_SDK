# from facebook_business.adobjects.adaccount import AdAccount
# from facebook_business.adobjects.campaign import Campaign
# from facebook_business.adobjects.adset import AdSet
# from facebook_business.adobjects.adcreative import AdCreative
# from facebook_business.adobjects.ad import Ad
# from facebook_business.adobjects.adpreview import AdPreview
# from facebook_business.adobjects.adimage import AdImage
# from facebook_business.api import FacebookAdsApi

from facebook_imports import *
from campaign import campaign_id

# access_token = 'EAAgkneVpJGQBAJc8wB7RmekGxMU1lNHciZBF4yOSLeGRfz3JxWRiCZC4BFOPZCpfGZBXN84HKasBDiwd21N3R6Y1wJYka7fs7L5wcMtMo5OxF1MLn926y3Jm4pZAxBF6caAF4zVXpZBmlnasriV7epZBoVjL8S8jT8FJweZCu23txnteiwxiYHSWevgZBZB5gfA6xplFcYwBD7iAZDZD'
# ad_account_id = 'act_2169630839952892'
# app_secret = '3b86f20ea08f7fd2a3cc6b2925d1b07b'
# page_id = '1961041583957344'
# app_id = '2215442238727389'
# FacebookAdsApi.init(access_token=access_token)


fields = []
params = {
    'status': 'PAUSED',
    'targeting': {'geo_locations':{'countries':['US']}},
    'daily_budget': '10000',
    'billing_event': 'IMPRESSIONS',
    'bid_amount': '20',
    'campaign_id': campaign_id,
    'optimization_goal': 'PAGE_LIKES',
    'promoted_object': {'page_id': page_id},
    'name': 'My AdSet',
}
ad_set = AdAccount(ad_account_id).create_ad_set(
    fields=fields,
    params=params,
)
print ('ad_set', ad_set)

ad_set_id = ad_set.get_id()
print ('ad_set_id:', ad_set_id, '\n')