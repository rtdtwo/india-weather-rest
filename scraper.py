import requests
from bs4 import BeautifulSoup


def get_station_data(id):
    URL = 'http://city.imd.gov.in/citywx/city_weather.php?id={}'.format(id)

    response = requests.get(URL, verify=False)
    html_text = response.text

    soup = BeautifulSoup(html_text, 'html.parser')

    cells = soup.find_all('td')

    max_temp = cells[4].text.strip()
    max_dep = cells[6].text.strip()
    min_temp = cells[8].text.strip()
    min_dep = cells[10].text.strip()
    rh_0830 = cells[14].text.strip()
    rh_1730 = cells[16].text.strip()

    sunrise = cells[20].text.strip()
    sunset = cells[18].text.strip()
    moonrise = cells[24].text.strip()
    moonset = cells[22].text.strip()

    day1_date = cells[31].font.text.strip()
    day1_max = cells[33].font.text.strip()
    day1_min = cells[32].font.text.strip()
    day1_forecast = cells[35].font.text.strip()

    day2_date = cells[36].font.text.strip()
    day2_max = cells[38].font.text.strip()
    day2_min = cells[37].font.text.strip()
    day2_forecast = cells[40].font.text.strip()

    day3_date = cells[41].font.text.strip()
    day3_max = cells[43].font.text.strip()
    day3_min = cells[42].font.text.strip()
    day3_forecast = cells[45].font.text.strip()

    day4_date = cells[46].font.text.strip()
    day4_max = cells[48].font.text.strip()
    day4_min = cells[47].font.text.strip()
    day4_forecast = cells[50].font.text.strip()

    day5_date = cells[51].font.text.strip()
    day5_max = cells[53].font.text.strip()
    day5_min = cells[52].font.text.strip()
    day5_forecast = cells[55].font.text.strip()

    day6_date = cells[56].font.text.strip()
    day6_max = cells[58].font.text.strip()
    day6_min = cells[57].font.text.strip()
    day6_forecast = cells[60].font.text.strip()

    day7_date = cells[61].font.text.strip()
    day7_max = cells[63].font.text.strip()
    day7_min = cells[62].font.text.strip()
    day7_forecast = cells[65].font.text.strip()

    return {
        'temperature': {
            'max': {
                'value': float(max_temp),
                'departure': float(max_dep)
            },
            'min': {
                'value': float(min_temp),
                'departure': float(min_dep)
            }
        },
        'humidity': {
            'morning': float(rh_0830),
            'evening': float(rh_1730)
        },
        'astronomical': {
            'sunrise': sunrise,
            'sunset': sunset,
            'moonrise': moonrise,
            'moonset': moonset
        },
        'forecast': [
            {
                'day': 1,
                'date': day1_date,
                'max': float(day1_max),
                'min': float(day1_min),
                'condition': day1_forecast
            },
            {
                'day': 2,
                'date': day2_date,
                'max': float(day2_max),
                'min': float(day2_min),
                'condition': day2_forecast
            },
            {
                'day': 3,
                'date': day3_date,
                'max': float(day3_max),
                'min': float(day3_min),
                'condition': day3_forecast
            },
            {
                'day': 4,
                'date': day4_date,
                'max': float(day4_max),
                'min': float(day4_min),
                'condition': day4_forecast
            },
            {
                'day': 5,
                'date': day5_date,
                'max': float(day5_max),
                'min': float(day5_min),
                'condition': day5_forecast
            },
            {
                'day': 6,
                'date': day6_date,
                'max': float(day6_max),
                'min': float(day6_min),
                'condition': day6_forecast
            },
            {
                'day': 7,
                'date': day7_date,
                'max': float(day7_max),
                'min': float(day7_min),
                'condition': day7_forecast
            }
        ]
    }
