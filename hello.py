# import pyshorteners

# def url_short(url):
    
#     shortner = pyshorteners.Shortener('Bitly')
#     short_url = shortner.short(url)
    
    
#     return short_url
    

def random_name(names, ages):
    output = []
    
    for name, age in zip(names, ages): 
        
        output.append({'name':name, 'age':age})
        
        return output
    
names = ['rajan', 'naman']
ages =[31, 21]

result = random_name(names, ages)

print(result)


