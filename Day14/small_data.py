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

# data1 = random.choice()
# print(data1)

def rnd_data():
    for num_of_data in range(0, len(data)):
        rnd_fun_data = []
        rnd_fun_data.append(data[num_of_data]["follower_count"])
    return rnd_fun_data

print(rnd_data())