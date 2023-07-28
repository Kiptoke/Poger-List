USER_TABLE = {
    'kaavya': 'h9wxnd3xvrfdfjv7r9p3ihz68', 
    'musa': '315qfzr3gmd5m4mkjoprzwsny7cq', 
    'andrew': '31fhaf5kxu7r4p3fr5r2klb5d23a', 
    'natasha': '31d6s5qq4uxpm6ucmue2p3ykb37q', 
    'naveen': '31giifsv5jaavljfciuappzifs3u', 
    'aman': 'blackupblackup5', 
    'kushal': 'kush_p', 
    'faiyaz': 'je1mzixeidgq3qxp5v10r4iih', 
    'renny': 'rennylop',
    'billy': 'freezercune',
    'val': 'lwbl3eraki1c231y7yp06f7mn'
}

def convertMS(ms):
    seconds=int(ms/1000)%60
    minutes=int(ms/(1000*60))%60
    return minutes, "{:02d}".format(seconds)