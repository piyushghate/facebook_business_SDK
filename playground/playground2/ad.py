from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adimage import AdImage
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.api import FacebookAdsApi

access_token = 'EAAfe7teo5N0BAMoVK5ZBGgJEaTU0lBpmO9sZAS9aDyChllVtawUEHLkyMgX38yhvpg5aCwjlH3ZAaOjYj0SswQljaTO5MsHfYbMP18oeEtsoixqEH0WDZAQDKk3hgztRPs5tVOFJqFrSoOJMVeSiQTkQnnaFk7kFwZBZCLffXoXmlTehoEsEuuWAsr4fc2JvTq3lSOvIIZBkgZDZD'
app_secret = 'cf211f667917a33303eee8ac90889907'
app_id = '298221930778662'
id = 'act_2169630839952892'
FacebookAdsApi.init(access_token=access_token)


image = AdImage(parent_id='act_2169630839952892')
image[AdImage.Field.filename] = '/home/mafia/Downloads/pubg.jpg'
image.remote_create()

# Output image Hash
print(image[AdImage.Field.hash])


#AdCreative:
fields = []
params = {
  'name': 'Sample Creative',
  'object_story_spec': {'page_id':'1961041583957344','link_data':{'image_hash':'aa2f25e81f15d9f2c07a03ee874e6625','link':'https://facebook.com/1961041583957344','message':'try it out'}},
}
print (AdAccount(id).create_ad_creative(
  fields=fields,
  params=params,
))