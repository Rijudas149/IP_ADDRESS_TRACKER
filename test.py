import pygeoip as pg

gip=pg.GeoIP("GeoLiteCity.dat")
res=gip.record_by_addr('72.229.28.185')

for key,val in res.items():
    print('%s : %s' %(key,val))
