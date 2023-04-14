def get_baskets_left(thousands, loaves):
    
    # http://www.biblegateway.com/passage/?search=mark%208:19-21&version=NIV
    
    if thousands == loaves:
        return 12
    else:
        return loaves

temp_loaves = int(input('How many loaves?: '))    
temp_thousands = int(input('How many thousands of people?: '))
print('{} baskets left over.'.format(get_baskets_left(temp_thousands, temp_loaves)))