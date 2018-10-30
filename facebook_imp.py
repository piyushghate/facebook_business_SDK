from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adpreview import AdPreview
from facebook_business.adobjects.adimage import AdImage
from facebook_business.api import FacebookAdsApi


access_token = ''
ad_account_id = 'act_adaccount'
app_secret = ''
page_id = ''
app_id = ''

FacebookAdsApi.init(access_token=access_token)