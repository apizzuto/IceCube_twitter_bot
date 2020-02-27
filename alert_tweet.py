import time, tweepy, gcn

@gcn.handlers.include_notice_types(
    gcn.notice_types.AMON_ICECUBE_HESE,
    gcn.notice_types.AMON_ICECUBE_EHE,
    gcn.notice_types.ICECUBE_ASTROTRACK_GOLD,
    gcn.notice_types.ICECUBE_ASTROTRACK_BRONZE)

def icecube_event_listener(payload, root):
    stream = 
    return

def steamshovel_listener():
    return

def generate_tweet():
    return 


while True:
    gcn.listen(handler=icecube_event_listener())
    steamshovel_listener()
    generate_tweet()
