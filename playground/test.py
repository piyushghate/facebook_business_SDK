from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

access_token = ''
app_secret = ''
app_id = ''
id = 'act_'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My campaign',
  'objective': 'LINK_CLICKS',
  'status': 'PAUSED',
}

campaign = AdAccount(id).create_campaign(
  fields=fields,
  params=params,
)

print(campaign)

