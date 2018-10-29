from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adpreview import AdPreview
from facebook_business.adobjects.adimage import AdImage
from facebook_business.api import FacebookAdsApi
from facebook_business.api import FacebookRequest
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject



access_token = 'EAAfe7teo5N0BAJ4enNz346AcZCq8scSS9ybJeb0ZCoDBNF1jDsJi8iHdXC7ePZCVv0I3PCGsw90w9ZARrINBuwUiSl7dSHtWYzNr36hjUh8vSb91MenedZBzV0Uv9w01RdSbqKyWZBDEzX57KELNEfPUokE73DYXb6HGiC6ZBs7P5sR9neoPjKk8XdwdXGwXMD1PjNvyALOegZDZD'
ad_account_id = 'act_2169630839952892'
app_secret = '3b86f20ea08f7fd2a3cc6b2925d1b07b'
page_id = '1961041583957344'
app_id = '2215442238727389'

# self = '23843140412640597'

FacebookAdsApi.init(access_token=access_token)



# fields = []
# params = {
#     'delete_strategy': 'DELETE_OLDEST',
#     'object_count': 1,
#     # 'before_date': 'datetime',
#     # 'objective': 'PAGE_LIKES',
#     # 'status': 'DELETED',
#     # 'run_status_new' : 'DELETED',
#     # 'buying_type': 'AUCTION',
#     # 'name': 'My Campaign',
#     # 'id' : '23843140412640597',
#     # 'id': '23843140412640597',
#     # 'api':'self._api',
# }
# # AdAccount(ad_account_id).delete_campaigns(
# #     # self._isAdSet = True,
# #     fields=fields,
# #     params=params,
# # )

# campaign = Campaign(fbid=23843140412640597, parent_id='act_2169630839952892')
# campaign.update({
#     # AdSet.Field.optimization_goal: AdSet.OptimizationGoal.link_clicks,
#     # AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
#     # AdSet.Field.bid_amount: 200,
#     Campaign.Field.status : Campaign.Status.deleted,
# })
# Campaign.remote_update()

campaign = Campaign(23843140412640597)
campaign.remote_delete()