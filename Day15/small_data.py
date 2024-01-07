import random
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
        {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },]




rnd_fun_data = []
for num_of_data in range(0, len(data)):    
    rnd_fun_data.append(data[num_of_data]["follower_count"])




data1 = random.choice(rnd_fun_data)
print(data1)




data2 = random.choice(rnd_fun_data)
print(data2)


