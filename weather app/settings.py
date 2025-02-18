import os

def save_city(city):
    settings_dir = os.path.dirname(__file__)
    city_file_path = os.path.join(settings_dir, 'city.txt')
    with open(city_file_path, 'wb') as f:
        f.write(city.encode('utf-8'))

def load_city():
    settings_dir = os.path.dirname(__file__)
    city_file_path = os.path.join(settings_dir, 'city.txt')
    try:
        with open(city_file_path, 'rb') as f:
            return f.read().decode('utf-8').strip()
    except FileNotFoundError:
        return 'New York'  # Default city

def get_states_and_cities():
    return {
        'Alabama': ['Birmingham', 'Montgomery', 'Mobile', 'Huntsville', 'Tuscaloosa'],
        'Alaska': ['Anchorage', 'Fairbanks', 'Juneau', 'Sitka', 'Ketchikan'],
        'Arizona': ['Phoenix', 'Tucson', 'Mesa', 'Chandler', 'Scottsdale'],
        'Arkansas': ['Little Rock', 'Fort Smith', 'Fayetteville', 'Springdale', 'Jonesboro'],
        'California': ['Los Angeles', 'San Diego', 'San Jose', 'San Francisco', 'Fresno'],
        'Colorado': ['Denver', 'Colorado Springs', 'Aurora', 'Fort Collins', 'Lakewood'],
        'Connecticut': ['Bridgeport', 'New Haven', 'Stamford', 'Hartford', 'Waterbury'],
        'Delaware': ['Wilmington', 'Dover', 'Newark', 'Middletown', 'Smyrna'],
        'Florida': ['Jacksonville', 'Miami', 'Tampa', 'Orlando', 'St. Petersburg'],
        'Georgia': ['Atlanta', 'Augusta', 'Columbus', 'Savannah', 'Athens'],
        'Hawaii': ['Honolulu', 'Hilo', 'Kailua', 'Kapolei', 'Kaneohe'],
        'Idaho': ['Boise', 'Meridian', 'Nampa', 'Idaho Falls', 'Pocatello'],
        'Illinois': ['Chicago', 'Aurora', 'Naperville', 'Joliet', 'Rockford'],
        'Indiana': ['Indianapolis', 'Fort Wayne', 'Evansville', 'South Bend', 'Carmel'],
        'Iowa': ['Des Moines', 'Cedar Rapids', 'Davenport', 'Sioux City', 'Iowa City'],
        'Kansas': ['Wichita', 'Overland Park', 'Kansas City', 'Topeka', 'Olathe'],
        'Kentucky': ['Louisville', 'Lexington', 'Bowling Green', 'Owensboro', 'Covington'],
        'Louisiana': ['New Orleans', 'Baton Rouge', 'Shreveport', 'Lafayette', 'Lake Charles'],
        'Maine': ['Portland', 'Lewiston', 'Bangor', 'South Portland', 'Auburn'],
        'Maryland': ['Baltimore', 'Frederick', 'Rockville', 'Gaithersburg', 'Bowie'],
        'Massachusetts': ['Boston', 'Worcester', 'Springfield', 'Lowell', 'Cambridge'],
        'Michigan': ['Detroit', 'Grand Rapids', 'Warren', 'Sterling Heights', 'Ann Arbor'],
        'Minnesota': ['Minneapolis', 'Saint Paul', 'Rochester', 'Duluth', 'Bloomington'],
        'Mississippi': ['Jackson', 'Gulfport', 'Southaven', 'Biloxi', 'Hattiesburg'],
        'Missouri': ['Kansas City', 'Saint Louis', 'Springfield', 'Columbia', 'Independence'],
        'Montana': ['Billings', 'Missoula', 'Great Falls', 'Bozeman', 'Butte'],
        'Nebraska': ['Omaha', 'Lincoln', 'Bellevue', 'Grand Island', 'Kearney'],
        'Nevada': ['Las Vegas', 'Henderson', 'Reno', 'North Las Vegas', 'Sparks'],
        'New Hampshire': ['Manchester', 'Nashua', 'Concord', 'Derry', 'Dover'],
        'New Jersey': ['Newark', 'Jersey City', 'Paterson', 'Elizabeth', 'Edison'],
        'New Mexico': ['Albuquerque', 'Las Cruces', 'Rio Rancho', 'Santa Fe', 'Roswell'],
        'New York': ['New York City', 'Buffalo', 'Rochester', 'Yonkers', 'Syracuse'],
        'North Carolina': ['Charlotte', 'Raleigh', 'Greensboro', 'Durham', 'Winston-Salem'],
        'North Dakota': ['Fargo', 'Bismarck', 'Grand Forks', 'Minot', 'West Fargo'],
        'Ohio': ['Columbus', 'Cleveland', 'Cincinnati', 'Toledo', 'Akron'],
        'Oklahoma': ['Oklahoma City', 'Tulsa', 'Norman', 'Broken Arrow', 'Lawton'],
        'Oregon': ['Portland', 'Salem', 'Eugene', 'Gresham', 'Hillsboro'],
        'Pennsylvania': ['Philadelphia', 'Pittsburgh', 'Allentown', 'Erie', 'Reading'],
        'Rhode Island': ['Providence', 'Warwick', 'Cranston', 'Pawtucket', 'East Providence'],
        'South Carolina': ['Charleston', 'Columbia', 'North Charleston', 'Mount Pleasant', 'Rock Hill'],
        'South Dakota': ['Sioux Falls', 'Rapid City', 'Aberdeen', 'Brookings', 'Watertown'],
        'Tennessee': ['Nashville', 'Memphis', 'Knoxville', 'Chattanooga', 'Clarksville'],
        'Texas': ['Houston', 'San Antonio', 'Dallas']
    }
