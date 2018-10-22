from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

access_token = 'ACCESS TOKEN'
app_secret = 'SECRET KEY'
app_id = '2215442238727389'
id = 'act_Account ID'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My campaign',
  'objective': 'LINK_CLICKS',
  'status': 'PAUSED',
}
print(AdAccount(id).create_campaign(
  fields=fields,
  params=params,
))

