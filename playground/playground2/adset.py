from facebook_business.adobjects.targetingsearch import TargetingSearch
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.targeting import Targeting
import datetime
from facebook_business.adobjects.adset import AdSet


access_token = 'EAAfe7teo5N0BAPNFh0LZC8R6mbXZCgjzZAN38UblWSmoeuVNexCahFuDUt9z2i4VxypwdRDkYZBXEoss5qW5dmSSpQPx9NbIfzeCtLOaa3mqwSIOKQJVRjDPCuWyt0qnqwSQH0ZC8MSm4xoAqZCC2RGMwFkvUtjYH0AhtrCo4OttYKkVmfND51ssp4BPPzdqANceHlFxzmaQZDZD'
app_secret = '3b86f20ea08f7fd2a3cc6b2925d1b07b'
app_id = '2215442238727389'
id = 'act_2169630839952892'
FacebookAdsApi.init(access_token=access_token)

# params = {
#     'q': 'baseball',
#     'type': 'adinterest',
# }

# resp = TargetingSearch.search(params=params)
# # print(resp)




targeting = {
    Targeting.Field.geo_locations: {
        Targeting.Field.countries: ['US'],
    },
    # Targeting.Field.interests: resp,
}


print(targeting)

# Adset:
today = datetime.date.today()
start_time = str(today + datetime.timedelta(weeks=1))
end_time = str(today + datetime.timedelta(weeks=2))

adset = AdSet(parent_id=id)
adset.update({
    AdSet.Field.name: 'My Ad Set',
    AdSet.Field.campaign_id: 23843136612450597,
    AdSet.Field.daily_budget: 100000,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
    AdSet.Field.bid_amount: 2,
    AdSet.Field.targeting: targeting,
    AdSet.Field.start_time: start_time,
    AdSet.Field.end_time: end_time,
})

adset.remote_create(params={
    'status': AdSet.Status.paused,
})

print(adset)