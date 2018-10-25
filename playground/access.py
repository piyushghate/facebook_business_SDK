from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
# from facebook_business.adobjects.adimage import AdImage

my_app_id = ''
my_app_secret = ''
my_access_token = ''
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount('act_')
campaigns = my_account.get_campaigns()
print("Campaigns: ",campaigns)

adset = my_account.get_ad_sets()
print("AdSets: ",adset)