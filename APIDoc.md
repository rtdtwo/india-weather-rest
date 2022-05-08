# API Documentation

## Response Formats
### Success
- `code`: `Int` variable containing HTTP code (20x).
- `result`: The result of the call, could be an object, array, or any other valid JSON.

### Failure
- `code`: `Int` variable containing HTTP code (40x or 50x).
- `msg`: `String` variable containing error message.


## Station

### `GET` : Get All Stations 
```
/station/all
```

```
{
	"code": 200,
	"result": [{
		"jurisdiction": "Pune",
		"region": "Maharashtra",
		"station": "Shivajinagar",
		"stationId": 43063
	}, {
		"jurisdiction": "Mumbai",
		"region": "Maharashtra",
		"station": "Santacruz",
		"stationId": 43003
	}, {
		"jurisdiction": "Mumbai",
		"region": "Maharashtra",
		"station": "Colaba",
		"stationId": 43057
	}]
}
```

### `GET` : Get Station 
```
/station/<int:id>
```

```
{
	"code": 200,
	"result": {
		"jurisdiction": "Pune",
		"region": "Maharashtra",
		"station": "Shivajinagar",
		"stationId": 43063
	}
}
```

## Weather

### `GET` : Station Weather 
```
/weather/<int:stationId>
```

```
{
	"code": 200,
	"results": {
		"astronomical": {
			"moonrise": "12:44",
			"moonset": "01:19",
			"sunrise": "06:03",
			"sunset": "18:59"
		},
		"forecast": [{
			"condition": "Mainly clear sky becoming partly cloudy towards afternoon or evening",
			"date": "08-May",
			"day": 1,
			"max": 39.0,
			"min": 21.0
		}, {
			"condition": "Mainly clear sky becoming partly cloudy towards afternoon or evening",
			"date": "09-May",
			"day": 2,
			"max": 39.0,
			"min": 21.0
		}, {
			"condition": "Partly cloudy sky",
			"date": "10-May",
			"day": 3,
			"max": 38.0,
			"min": 22.0
		}, {
			"condition": "Partly cloudy sky",
			"date": "11-May",
			"day": 4,
			"max": 38.0,
			"min": 22.0
		}, {
			"condition": "Partly cloudy sky",
			"date": "12-May",
			"day": 5,
			"max": 37.0,
			"min": 23.0
		}, {
			"condition": "Partly cloudy sky",
			"date": "13-May",
			"day": 6,
			"max": 37.0,
			"min": 23.0
		}, {
			"condition": "Partly cloudy sky",
			"date": "14-May",
			"day": 7,
			"max": 37.0,
			"min": 23.0
		}],
		"humidity": {
			"evening": 23.0,
			"morning": 46.0
		},
		"temperature": {
			"max": {
				"departure": 2.0,
				"value": 39.6
			},
			"min": {
				"departure": -1.0,
				"value": 21.4
			}
		}
	}
}
```
