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
| ![Screenshot_20230919-160537_Plus](https://github.com/prateekmaru/india-weather-rest/assets/47496067/0942d2ef-b0c4-4a17-95a1-9ab459480991) | ![Screenshot_20230919-160552_Plus](https://github.com/prateekmaru/india-weather-rest/assets/47496067/0a9000b5-8318-4caf-a19b-35f3eb0525b0) |

| Screenshot 3 | Screenshot 4 |
| ------------ | ------------ |
| ![Screenshot_20230919-160613_Plus](https://github.com/prateekmaru/india-weather-rest/assets/47496067/752a006c-542a-4830-9ea9-08704a27702b) | ![Screenshot_20230919-160619_Plus](https://github.com/prateekmaru/india-weather-rest/assets/47496067/ed421411-b28b-4eba-b8a5-a52b99c057e0) |

| Vector Logo Unofficial Light | Vector Logo Unofficial Dark |
| ------------ | ------------ |
| ![IMD_ALT](https://github.com/prateekmaru/india-weather-rest/assets/47496067/97c2000b-ed93-40d8-a2fc-1e88a5007d04) | ![IMD](https://github.com/prateekmaru/india-weather-rest/assets/47496067/0b98512f-c3b6-4762-b409-c7b7146b372c) |



## Disclaimer
- NOT AFFILIATED TO INDIA METEOROLOGICAL DEPARTMENT IN ANY WAY. ALL DUE CREDITS TO THEM, I'M ONLY PROVIDING A WAY TO ACCESS THE DATA.
- DATA IS PROVIDED AS IS WITHOUT ANY MODIFICATIONS.
- I scrape their website to get this data, and this tool may break as soon as they decide to change their website code. So, do not rely on this tool for critical applications.
