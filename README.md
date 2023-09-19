# india-weather-rest
A RESTful API to access weather data from the India Meteorological Department.

## Motivation
I built this because IMD weather data is super hard to access. Even for a layman, it is surprising that I need to click on a very hidden link in small text at the bottom of their homepage to access a map where I can see all this data. Also, unlike many other datasets that have been made available to the public via open APIs by the government, weather data is still unavailable even though it is public information. It is truly unfortunate to see our weather data being made increasingly difficult to access, whereas other agencies like NOAA make all their data easy to access or parse via code.

## How to run?
- This API webserver is built using Flask.
- Install Python and Pip.
- Install all dependencies by running `pip install -r requirements.txt`
- Run the app: `python3 app.py`

## API Doc
See ![API Documentation](https://github.com/rtdtwo/india-weather-rest/blob/main/APIDoc.md) for HTTP endpoints and sample outputs.

## Station support
Request inclusion of new stations in ![this issue](https://github.com/rtdtwo/india-weather-rest/issues/1).

## Telegram Bot Screenshots
| Screenshot 1 | Screenshot 2 |
| ------------ | ------------ |
| ![Screenshot_20230919-160537_Plus](https://github.com/prateekmaru/india-weather-rest/assets/47496067/84635050-4e8c-41cd-b734-e4f1c0799d25) | ![Screenshot_20230919-160552_Plus](https://github.com/prateekmaru/india-weather-rest/assets/47496067/8937542c-4369-4b5a-a75a-295cf301deb6) |

| Screenshot 3 | Screenshot 4 |
| ------------ | ------------ |
| ![Screenshot_20230919-160613_Plus](https://github.com/prateekmaru/india-weather-rest/assets/47496067/fd2c1632-6bc5-4145-b584-97e8af75bbd2) | ![Screenshot_20230919-160619_Plus](https://github.com/prateekmaru/india-weather-rest/assets/47496067/b0ef5cb0-20fc-4f38-9d55-329a19cf92b5) |

| Vector Logo Unofficial Light | Vector Logo Unofficial Dark |
| ------------ | ------------ |
| ![IMD_ALT](https://github.com/prateekmaru/india-weather-rest/assets/47496067/fd9d0f6a-71b0-43f0-b85f-7763e8c9849d) | ![IMD](https://github.com/prateekmaru/india-weather-rest/assets/47496067/b733d035-73f1-476a-acb0-7ab9308b1aae) |


## Disclaimer
- NOT AFFILIATED TO INDIA METEOROLOGICAL DEPARTMENT IN ANY WAY. ALL DUE CREDITS TO THEM, I'M ONLY PROVIDING A WAY TO ACCESS THE DATA.
- DATA IS PROVIDED AS IS WITHOUT ANY MODIFICATIONS.
- I scrape their website to get this data, and this tool may break as soon as they decide to change their website code. So, do not rely on this tool for critical applications.
