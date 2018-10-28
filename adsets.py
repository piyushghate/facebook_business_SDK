from facebook_imp import *
# from campaigns import campaign_id

def createAdset(campaign_id):
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

    return ad_set.get_id()
    # print ('ad_set_id:', ad_set_id, '\n')