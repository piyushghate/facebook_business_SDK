from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.ad import Ad
from facebook_business.api import FacebookAdsApi

from facebook_business.adobjects.adcreativeobjectstoryspec \
    import AdCreativeObjectStorySpec
from facebook_business.adobjects.adcreativetextdata \
    import AdCreativeTextData
from facebook_business.adobjects.adcreativelinkdata \
    import AdCreativeLinkData

access_token = ''
app_secret = ''
app_id = ''
id = 'act_'
FacebookAdsApi.init(access_token=access_token)


link_data = AdCreativeLinkData()
# # video_data[AdCreativeVideoData.Field.description] = 'My Description'
link_data[AdCreativeLinkData.Field.link] = 'http://allaboutfasionbyvs.wordpress.com'
link_data[AdCreativeLinkData.Field.message] = 'Click Me!'
# text_data[AdCreativeTextData.Field.id] = id

# text_data = AdCreativeTextData()
# # video_data[AdCreativeVideoData.Field.description] = 'My Description'
# text_data[AdCreativeTextData.Field.message] = 'My message'
# # text_data[AdCreativeTextData.Field.id] = id 

object_story_spec = AdCreativeObjectStorySpec()
object_story_spec[AdCreativeObjectStorySpec.Field.page_id] = 706105013086461
object_story_spec[AdCreativeObjectStorySpec.Field.link_data] = link_data


fields = []
params = {
    'title': 'My Test Creative',
    # 'body' : 'My test Ad Creative Body',
    # 'image_hash' : image[AdImage.Field.hash],
    # 'image_url' : 'https://www.facebook.com/Mobile-Gaming-Platform-1961041583957344/?__tn__=kC-R&eid=ARDsDwztxyPTQEtGoPs6_kQ5tfCL18M_YSPMDi4Bae4WL81hsyUzI1NdbN5VyrK4TuNspebzyjCNne48&hc_ref=ARSVO6cdGRTDALByLj_FoBONbsklWRvyJPBSYYbFvwtINwCP54bFZdkhBFHdhKWYAP0&__xts__[0]=68.ARDk8JO77pNKkz1oLl2sLB6lXgU4olzH9ONZXdNrI0h7-J4zC8qVNTQTOivNXzUd1jgcdg66faCS0a53DZchQQGyXAEN1atfVgt0W48HISZ9hr3x8j1P3s9pw2IS9ZSnPQr9cbUX1CUtNPvoD9LRV4d3007Av7tDTBteIAZhiLURGJwLHihOONGskIX8gw8r1nAQtGHhWUrCMY08oTarhnb4CnhW1Iou1YiKTQ',
    # 'objective_source' : 'Piyushs app',
    # 'object_id' : '1961041583957344',
    # 'object_store_url' : 'http://allpositivity.wordpress.com',
    # 'object_story_id' : 'object_story_id',
    'object_story_spec' : object_story_spec,
    # 'object_type' : 'object_type',
    # 'object_url' : 'http://allaboutfasionbyvs.wordpress.com',
    # 'open_link' : 'OPEN_LINK',
}

adcreate = AdAccount(id).create_ad_creative(
    fields = fields,
    params = params,
)

print("Adcreative: ",adcreate)


# fields = []
# params = {
#   'name': 'My Ad',
#   'adset_id': '120330000098905119',
#   'creative': {'creative_id':'23843135687580597'},
# #   'creative': adcreate,
#   'status': 'PAUSED',
# }
# addd = AdAccount(id).create_ad(
#   fields=fields,
#   params=params,
# )

# print(addd)