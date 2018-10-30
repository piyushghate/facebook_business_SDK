from facebook_business.adobjects.adaccount import AdAccount
# from facebook_business.adobjects.campaign import Campaign
# from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adpreview import AdPreview
from facebook_business.adobjects.adimage import AdImage
from facebook_business.api import FacebookAdsApi

access_token = 'EAAfe7teo5N0BAPzy9y6ZAPpGomkff74QxoUMJ6lCEmlTxrCmaDNZBurBSJNtpZArZATsNadu929qqV2hfGFkut3ZBRpKGslAVZA4rlwsHdZC6JDjGo60ifkPm01J5hlHRz2n5fke8cUlY8hcNS9ngOADE2ucCZC0e4hZBcsQq91U0ZBwLRGJK5ZA2wdFZCAM1q0OwnAP7AYBDtxBBAZDZD'
ad_account_id = 'act_10216412412039072'
app_secret = '3b86f20ea08f7fd2a3cc6b2925d1b07b'
page_id = '1961041583957344'
app_id = '2215442238727389'
FacebookAdsApi.init(access_token=access_token)

#Image Hash
image = AdImage(parent_id=ad_account_id)
image[AdImage.Field.filename] = '/home/mafia/Downloads/pubg.jpg'
image.remote_create()

print(image[AdImage.Field.hash])


#AdCreative
fields = []
params = {
    'body': 'Like My Page',
    # 'image_url': 'http://www.facebookmarketingdevelopers.com/static/images/resource_1.jpg',
    'name': 'My Creative',
    # 'object_id': page_id,
    'title': 'My Page Like Ad',
    'object_story_spec': {'page_id':'1961041583957344','link_data':{'image_hash':image[AdImage.Field.hash],'link':'https://facebook.com/1961041583957344','message':'try it out'}},
}
creative = AdAccount(ad_account_id).create_ad_creative(
    fields=fields,
    params=params,
)
print ('creative', creative)

creative_id = creative.get_id()
print ('creative_id:', creative_id, '\n')


#Ad
fields = []
params = {
    'status': 'PAUSED',
    'adset_id': ad_set_id,
    'name': 'My Ad',
    'creative': {'creative_id':creative_id},
}
ad = AdAccount(ad_account_id).create_ad(
    fields=fields,
    params=params,
)
print ('ad', ad)

ad_id = ad.get_id()
print ('ad_id:', ad_id, '\n')


#Ad Preview
fields = []
params = {
    'ad_format': 'DESKTOP_FEED_STANDARD',
}
print (Ad(ad_id).get_previews(
    fields=fields,
    params=params,
))