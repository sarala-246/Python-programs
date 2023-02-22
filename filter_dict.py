def filterdict(d):
    key1={}
    for k,v in d.items():
        if v < 20000:
            key1[k]=v
    return key1
d={'Jack': 12000, 'Max': 20000, 'Hack': 19000, 'Nack': 80000}
print(filterdict(d))
