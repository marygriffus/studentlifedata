"""
PyLab 19 March 2016
Analyzing JSON and US Passport Data with python3
Valid passportIssuanceByCalendarYear
https://catalog.data.gov/dataset/passportissuancebycalendaryear
"""

#### Imports

import os
import json
try:
    from urllib.request import urlopen ## python3

except ImportError:
    print('python2 alert')
    from urllib import urlopen ## python2

### Constants

url = 'https://www.quandl.com/api/v3/datasets/FED/RXI_US_N_A_UK/data.json?api_key=EokXzvzzx1wvJV9xGzmk'
currency_json = 'currency.json'

if not os.path.isfile(currency_json):
    f = urlopen(url)
    text = f.read()
    decoded_text = text.decode('utf8')
    data =  json.loads(decoded_text)
    print('Requested JSON and converted to python dictionary')

    with open(currency_json, 'w+') as f:
        json.dump(data, f)
    print('Saved JSON to file')

else:
    with open(currency_json, 'r+') as f:
        data = json.load(f)
    print('File {fn} opened. Time to get to work.'.format(fn=currency_json))


print "Date         Value"
for i in xrange(0,len(data['dataset_data']['data'])):
    print data['dataset_data']['data'][i][0], "  ", data['dataset_data']['data'][i][1] 

#print(data)

#print(type(data))

#print(len(data))

#print(data[0]['Count'])

total = 0
count1 = 0
total1= 0
count2 = 0
for year_dict in data:
    #print(year_dict['Count'])
    if year_dict['Year'] >= 2002:
        total = total + year_dict['Count']
        count1 += 1
    else:
        total1 += year_dict['Count']
        count2 += 1

print(total/count1 >= total1/count2)

#print(total)

#print(total/len(data))



### Questions


### What data type is 'data'? What operations can we do on it?



### How many years are in this dataset?



### What is the total number of passports issues in this data set?



### What is number of passports issues in the last ten years? What is the average number issued per year since then?



### Since 2001, has the average number of passports increased or decreased since then?



# PART II


#USAcceptanceFacilities for passports
# https://catalog.data.gov/dataset/usacceptancefacilities

# url2 = 'https://cadatacatalog.state.gov/storage/f/2013-11-24T20:52:39.651Z/facilities.json'


### Write a small script to save this json file to a file. (hint look at code above)
### Advanced: can you write this script as a function? (code reuser)


### How many facilities are in this dataset?


### How many states?


### Ask a question of this data.


### can you convert this to a csv file and create a map using Google maps?
### https://www.google.com/maps/d/u/0/?hl=en_US&app
