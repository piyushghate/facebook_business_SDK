from facebook_imp import *

print('In camps.py')

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

def pauseCamp(campIDD):
    camp = Campaign(fbid=campIDD, parent_id=ad_account_id)
    camp.update({
    Campaign.Field.status: Campaign.Status.paused,
    })
    camp.remote_update()
    print('Campaign with ID: ', campIDD,'paused!')

def startCamp(campIDD):
    camp = Campaign(fbid=campIDD, parent_id=ad_account_id)
    camp.update({
    Campaign.Field.status: Campaign.Status.active,
    })
    camp.remote_update()
    print('Campaign with ID: ', campIDD,'activated!')