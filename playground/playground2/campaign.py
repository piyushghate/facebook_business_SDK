from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

access_token = 'EAAfe7teo5N0BAPNFh0LZC8R6mbXZCgjzZAN38UblWSmoeuVNexCahFuDUt9z2i4VxypwdRDkYZBXEoss5qW5dmSSpQPx9NbIfzeCtLOaa3mqwSIOKQJVRjDPCuWyt0qnqwSQH0ZC8MSm4xoAqZCC2RGMwFkvUtjYH0AhtrCo4OttYKkVmfND51ssp4BPPzdqANceHlFxzmaQZDZD'
app_secret = '3b86f20ea08f7fd2a3cc6b2925d1b07b'
app_id = '2215442238727389'
id = 'act_2169630839952892'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My campaign',
  'objective': 'LINK_CLICKS',
  'status': 'PAUSED',
}
adcampaign = AdAccount(id).create_campaign(
  fields=fields,
  params=params,
)

print(adcampaign)