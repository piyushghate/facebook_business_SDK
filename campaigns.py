from facebook_imp import *


def createCamp():
    fields = []
    params = {
        'objective': 'PAGE_LIKES',
        'status': 'PAUSED',
        'buying_type': 'AUCTION',
        'name': 'My Campaign',
    }
    campaign = AdAccount(ad_account_id).create_campaign(
        fields=fields,
        params=params,
    )
    print ('campaign', campaign)

    campaign_id = campaign.get_id()
    return campaign_id

def readCampaigns():
    print((AdAccount(ad_account_id)).get_campaigns())

def deleteCampaigns(campIDD):
    campaign = Campaign(campIDD)
    campaign.remote_delete()
    print('Campaign with ID: ', campIDD, 'deleted!')