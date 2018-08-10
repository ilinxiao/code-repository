
"""
某商店规定：3个空汽水瓶可以换1瓶汽水。小张手上有10个空汽水瓶，她最多可以换多少瓶汽水喝？
"""
bottle = 10
radio = 8 #exchange radio
soda = 0
while bottle > 0 :
    exchange_soda, bottle = bottle // radio, bottle % radio
    soda += exchange_soda
    if bottle != 0:
        bottle += exchange_soda 
    print('exchange soda:%d, total soda:%d, remaining bottle:%d' % (exchange_soda, soda, bottle))
    if bottle > 0 and bottle < radio:
        print('remaining number of bottle little radio, can exchange one more.')
        soda+=1
        bottle = 0
        
print('soda number:%d' % soda)