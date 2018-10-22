from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

access_token = 'EAAfe7teo5N0BACQ0UZAf43ZCG0uVPvaJaNd4YpHDZCWFjv6lv4ZAH1hPidbbwuxTFLzGRCbAAOGXc50jIosvKr4D1wWNAcR6nC8WZBwbAZAqQtJGKd3xLuOMlknmlEDyr63ls8R1gFyhMyBtlbFVa34bKmGfIhfKbtfXBEkYZAg2fA0jjp5xFugNudzuMr8byLTnCpoGArK2zkZBG59zgzkZC3NcwQkgFU8MDJw5J3oTsEwZDZD'
app_secret = '3b86f20ea08f7fd2a3cc6b2925d1b07b'
app_id = '2215442238727389'
id = 'act_257672218227370'
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

