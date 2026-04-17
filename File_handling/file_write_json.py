import json
data =[
{"id":1,"first_name":"Nina","last_name":"Silverstone","email":"nsilverstone0@mozilla.com","gender":"Female","ip_address":"188.107.146.41"},
{"id":2,"first_name":"Skylar","last_name":"Wrennall","email":"swrennall1@scientificamerican.com","gender":"Male","ip_address":"105.106.136.33"},
{"id":3,"first_name":"Eva","last_name":"Suggitt","email":"esuggitt2@google.cn","gender":"Female","ip_address":"246.245.203.224"},
{"id":4,"first_name":"Diane","last_name":"Elms","email":"delms3@usnews.com","gender":"Female","ip_address":"211.23.250.247"},
{"id":5,"first_name":"Renado","last_name":"Lapping","email":"rlapping4@hp.com","gender":"Male","ip_address":"81.177.200.225"},
{"id":6,"first_name":"Sonnnie","last_name":"Vidler","email":"svidler5@multiply.com","gender":"Female","ip_address":"181.228.165.75"},
{"id":7,"first_name":"Sheena","last_name":"Hawkett","email":"shawkett6@yelp.com","gender":"Female","ip_address":"133.42.205.254"},
{"id":8,"first_name":"Darcy","last_name":"Sabberton","email":"dsabberton7@unblog.fr","gender":"Female","ip_address":"199.173.132.70"},
{"id":9,"first_name":"Elspeth","last_name":"Dubbin","email":"edubbin8@tiny.cc","gender":"Female","ip_address":"157.177.97.182"},
{"id":10,"first_name":"Lars","last_name":"Danielis","email":"ldanielis9@goo.ne.jp","gender":"Male","ip_address":"88.155.180.203"},
{"id":11,"first_name":"Ellsworth","last_name":"Divell","email":"edivella@tumblr.com","gender":"Male","ip_address":"9.66.211.97"},
{"id":12,"first_name":"Blake","last_name":"Goffe","email":"bgoffeb@skyrock.com","gender":"Female","ip_address":"158.36.224.142"},
{"id":13,"first_name":"Jenica","last_name":"Loney","email":"jloneyc@cocolog-nifty.com","gender":"Female","ip_address":"30.120.78.201"},
{"id":14,"first_name":"Serge","last_name":"Olivier","email":"solivierd@unesco.org","gender":"Male","ip_address":"120.205.62.78"},
{"id":15,"first_name":"Lilly","last_name":"Costa","email":"lcostae@ted.com","gender":"Female","ip_address":"179.60.181.219"},
{"id":16,"first_name":"Raphael","last_name":"O'Scollain","email":"roscollainf@1688.com","gender":"Male","ip_address":"141.62.89.218"},
{"id":17,"first_name":"Verla","last_name":"Quarrie","email":"vquarrieg@thetimes.co.uk","gender":"Female","ip_address":"209.115.188.204"},
]
with open("data.json","w") as fp:
    line=json.dump(data,fp)
    print("file updated successfully")