#!/6d79389a338c4bf170fausr/bin/python
#!coding:utf-8
import CloudFlare
import re
 
cf = CloudFlare.CloudFlare(email='ay1681688@gmail.com', token='7688003357becab6a6d79389a338c4bf170fa') 
 
cname_record=open('ip.txt','rb').read().strip()
 
zones=open('domains.txt','rb').readlines()
zones=[zone.strip() for zone in zones if zone.strip()!='']
 
print zones
for zone in zones:
    #zone = "www."+zone 
    print '正在处理%s'%zone
#    print(cf.zones.get(params={"name":zone}))
    zone_id=cf.zones.get(params={"name":zone})[0]["id"]
    record=cf.zones.dns_records.get(zone_id)
###   @记录
    A_record = [r for r in record if r['type']=='A' and r['name']==zone]
 
###   www记录
#    A_record = [r for r in record if r['type']=='A' and r['name']=='www.'+zone]
 
 
    if not A_record:
###   @记录
        data={'name':zone,'type':'A','content':cname_record,'proxied':True}
###   www记录
#        data={'name':'www.'+zone,'type':'A','content':cname_record,'proxied':True}
        cf.zones.dns_records.post(zone_id,data=data)
        continue
    A_record_id = A_record[0]['id']
    data={'content':cname_record,'proxied':True}

