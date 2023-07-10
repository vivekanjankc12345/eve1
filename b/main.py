def max_s(a):
    max=0
    for item in a:
        if(max<item["salary"]):
            max=item["salary"]
            for item in a:
                if(max==item["salary"]):
                    return item
                



employess=[{"name":"jhon","salary":3000,"designation":"developer"},
     {"name":"emma","salary":4000,"designation":"manager"},
     {"name":"kelly","salary":3500,"designation":"tester"},]   
print(max_s(employess))             