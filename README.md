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

## Disclaimer
- NOT AFFILIATED TO INDIA METEOROLOGICAL DEPARTMENT IN ANY WAY. ALL DUE CREDITS TO THEM, I'M ONLY PROVIDING A WAY TO ACCESS THE DATA.
- DATA IS PROVIDED AS IS WITHOUT ANY MODIFICATIONS.
- I scrape their website to get this data, and this tool may break as soon as they decide to change their website code. So, do not rely on this tool for critical applications.
