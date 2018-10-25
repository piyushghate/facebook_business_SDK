from facebook_business.adobjects.adset import AdSet
# from facebook_business.adobjects.targeting import Targeting
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
# adset.update({
#     AdSet.Field.name: 'My Ad Set',
#     AdSet.Field.campaign_id: 23843112406190495,
#     AdSet.Field.daily_budget: 1000,
#     AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
#     AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
#     AdSet.Field.bid_amount: 2,
#     AdSet.Field.targeting: {
#         Targeting.Field.geo_locations: {
#             'countries': ['IN'],
#         },
#     },
# })

# adset.remote_create(params={
#     'status': AdSet.Status.paused,
# })
# print(adset)

# geo_locations: {
#             'countries': ['IN'],
#         }

access_token = ''
id = 'act_'

FacebookAdsApi.init(access_token=access_token)

fields = []
params = {
  'name': 'First Ad Set',
  'campaign_id': '120330000098904819',
  # 'campaign': 'My campaign',
  'billing_event': 'LINK_CLICKS',
  'optimization_goal': 'LINK_CLICKS',
  'promoted_object': '{"page_id": "706105013086461"}',
  'daily_budget': '20000',
  'bid_amount': '2',
  'targeting' : {'geo_locations':{'countries':['IN']}},
  'status': 'PAUSED',
}

adset = AdAccount(id).create_ad_set(
    fields = fields,
    params = params,
)

print(adset)