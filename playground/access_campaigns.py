from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

my_app_id = '2215442238727389'
my_app_secret = 'SECRET'
my_access_token = 'ACCESS TOKEN'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount('act_Account ID')
campaigns = my_account.get_campaigns()
print(campaigns)