#!/usr/bin/python
#!coding:utf-8
import CloudFlare
 
 
cf = CloudFlare.CloudFlare(email='ay1681688@gmail.com', token='7688003357becab6a6d79389a338c4bf170fa')
 
 
new_ip=open('ip.txt','rb').read().strip()
 
zones=open('domains.txt','rb').readlines()
zones=[zone.strip() for zone in zones if zone.strip()!='']
 
 
for zone in zones:
    print "正在处理域名%s"%zone
    zone_id=cf.zones.get(params={"name":zone})[0]["id"]
    record=cf.zones.dns_records.get(zone_id)
    A_records = [r for r in record if r['type']=='A' and r['content']!=new_ip]
    A_record_ids = [r['id'] for r in A_records]
 
#######记录的IP和要更换的一致不执行
    if len(A_record_ids) ==0:
        continue
 
#######要添加的记录
    data=[{'name':zone,'type':'A','content':new_ip,'proxied':False},
          {'name':'ag','type':'A','content':new_ip,'proxied':False}]
 
#####删除A记录
    for A_record_id in A_record_ids:
        cf.zones.dns_records.delete(zone_id,A_record_id)
#####添加修改后的A记录
    try:
        for dd in data:
            cf.zones.dns_records.post(zone_id,data=dd)
    except:
        print "修改$s A记录失败!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"%zone
        print "\r\n"
        continue
