import os

owm_api_key = os.environ['APIKey']
# На запрос:
# f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}'
# Ответ:
answer_example2 = {
    'coord': {
        'lon': 37.6156,
        'lat': 55.7522
    },
    'weather': [{
        'id': 804,
        'main': 'Clouds',
        'description': 'overcast clouds',
        'icon': '04d'
    }],
    'base':
    'stations',
    'main': {
        'temp': 284.07,
        'feels_like': 283.31,
        'temp_min': 283.39,
        'temp_max': 284.47,
        'pressure': 1015,
        'humidity': 80,
        'sea_level': 1015,
        'grnd_level': 997
    },
    'visibility':
    10000,
    'wind': {
        'speed': 3.34,
        'deg': 95,
        'gust': 5.1
    },
    'clouds': {
        'all': 99
    },
    'dt':
    1663832939,
    'sys': {
        'type': 2,
        'id': 2000314,
        'country': 'RU',
        'sunrise': 1663816456,
        'sunset': 1663860632
    },
    'timezone':
    10800,
    'id':
    524901,
    'name':
    'Moscow',
    'cod':
    200
}

answer_example1 = {
    'coord': {
        'lon': 37.6156,
        'lat': 55.7522
    },
    'weather': [{
        'id': 804,
        'main': 'Clouds',
        'description': 'overcast clouds',
        'icon': '04d'
    }],
    'base':
    'stations',
    'main': {
        'temp': 284.06,
        'feels_like': 283.3,
        'temp_min': 282.9,
        'temp_max': 284.47,
        'pressure': 1015,
        'humidity': 80,
        'sea_level': 1015,
        'grnd_level': 997
    },
    'visibility':
    10000,
    'wind': {
        'speed': 3.34,
        'deg': 95,
        'gust': 5.1
    },
    'clouds': {
        'all': 99
    },
    'dt':
    1663832386,
    'sys': {
        'type': 2,
        'id': 2000314,
        'country': 'RU',
        'sunrise': 1663816456,
        'sunset': 1663860632
    },
    'timezone':
    10800,
    'id':
    524901,
    'name':
    'Moscow',
    'cod':
    200
}

# На запрос:
# request1= "https://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid={api_key}"

# Ответ:
answer_example1 = {
    'cod':
    '200',
    'message':
    0,
    'cnt':
    40,
    'list': [{
        'dt':
        1663837200,
        'main': {
            'temp': 283.48,
            'feels_like': 282.34,
            'temp_min': 283.48,
            'temp_max': 286.33,
            'pressure': 1022,
            'sea_level': 1022,
            'grnd_level': 936,
            'humidity': 68,
            'temp_kf': -2.85
        },
        'weather': [{
            'id': 800,
            'main': 'Clear',
            'description': 'clear sky',
            'icon': '01d'
        }],
        'clouds': {
            'all': 1
        },
        'wind': {
            'speed': 2.6,
            'deg': 72,
            'gust': 3.55
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-22 09:00:00'
    }, {
        'dt':
        1663848000,
        'main': {
            'temp': 286.26,
            'feels_like': 285.09,
            'temp_min': 286.26,
            'temp_max': 288.36,
            'pressure': 1021,
            'sea_level': 1021,
            'grnd_level': 935,
            'humidity': 56,
            'temp_kf': -2.1
        },
        'weather': [{
            'id': 800,
            'main': 'Clear',
            'description': 'clear sky',
            'icon': '01d'
        }],
        'clouds': {
            'all': 5
        },
        'wind': {
            'speed': 3.1,
            'deg': 71,
            'gust': 2.43
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-22 12:00:00'
    }, {
        'dt':
        1663858800,
        'main': {
            'temp': 288.04,
            'feels_like': 286.81,
            'temp_min': 288.04,
            'temp_max': 288.04,
            'pressure': 1019,
            'sea_level': 1019,
            'grnd_level': 934,
            'humidity': 47,
            'temp_kf': 0
        },
        'weather': [{
            'id': 801,
            'main': 'Clouds',
            'description': 'few clouds',
            'icon': '02d'
        }],
        'clouds': {
            'all': 19
        },
        'wind': {
            'speed': 3.41,
            'deg': 71,
            'gust': 2.74
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-22 15:00:00'
    }, {
        'dt':
        1663869600,
        'main': {
            'temp': 281.55,
            'feels_like': 280.96,
            'temp_min': 281.55,
            'temp_max': 281.55,
            'pressure': 1020,
            'sea_level': 1020,
            'grnd_level': 933,
            'humidity': 72,
            'temp_kf': 0
        },
        'weather': [{
            'id': 801,
            'main': 'Clouds',
            'description': 'few clouds',
            'icon': '02n'
        }],
        'clouds': {
            'all': 22
        },
        'wind': {
            'speed': 1.51,
            'deg': 137,
            'gust': 3.52
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-22 18:00:00'
    }, {
        'dt':
        1663880400,
        'main': {
            'temp': 280.59,
            'feels_like': 280.59,
            'temp_min': 280.59,
            'temp_max': 280.59,
            'pressure': 1022,
            'sea_level': 1022,
            'grnd_level': 934,
            'humidity': 72,
            'temp_kf': 0
        },
        'weather': [{
            'id': 800,
            'main': 'Clear',
            'description': 'clear sky',
            'icon': '01n'
        }],
        'clouds': {
            'all': 0
        },
        'wind': {
            'speed': 1.3,
            'deg': 214,
            'gust': 1.48
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-22 21:00:00'
    }, {
        'dt':
        1663891200,
        'main': {
            'temp': 279.56,
            'feels_like': 278.7,
            'temp_min': 279.56,
            'temp_max': 279.56,
            'pressure': 1022,
            'sea_level': 1022,
            'grnd_level': 934,
            'humidity': 70,
            'temp_kf': 0
        },
        'weather': [{
            'id': 800,
            'main': 'Clear',
            'description': 'clear sky',
            'icon': '01n'
        }],
        'clouds': {
            'all': 0
        },
        'wind': {
            'speed': 1.5,
            'deg': 215,
            'gust': 1.48
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-23 00:00:00'
    }, {
        'dt':
        1663902000,
        'main': {
            'temp': 278.83,
            'feels_like': 277.99,
            'temp_min': 278.83,
            'temp_max': 278.83,
            'pressure': 1021,
            'sea_level': 1021,
            'grnd_level': 933,
            'humidity': 65,
            'temp_kf': 0
        },
        'weather': [{
            'id': 800,
            'main': 'Clear',
            'description': 'clear sky',
            'icon': '01n'
        }],
        'clouds': {
            'all': 0
        },
        'wind': {
            'speed': 1.41,
            'deg': 216,
            'gust': 1.39
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-23 03:00:00'
    }, {
        'dt':
        1663912800,
        'main': {
            'temp': 279.9,
            'feels_like': 279.15,
            'temp_min': 279.9,
            'temp_max': 279.9,
            'pressure': 1022,
            'sea_level': 1022,
            'grnd_level': 934,
            'humidity': 68,
            'temp_kf': 0
        },
        'weather': [{
            'id': 800,
            'main': 'Clear',
            'description': 'clear sky',
            'icon': '01d'
        }],
        'clouds': {
            'all': 0
        },
        'wind': {
            'speed': 1.45,
            'deg': 229,
            'gust': 1.34
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-23 06:00:00'
    }, {
        'dt':
        1663923600,
        'main': {
            'temp': 287.32,
            'feels_like': 286.07,
            'temp_min': 287.32,
            'temp_max': 287.32,
            'pressure': 1021,
            'sea_level': 1021,
            'grnd_level': 935,
            'humidity': 49,
            'temp_kf': 0
        },
        'weather': [{
            'id': 800,
            'main': 'Clear',
            'description': 'clear sky',
            'icon': '01d'
        }],
        'clouds': {
            'all': 0
        },
        'wind': {
            'speed': 1.46,
            'deg': 51,
            'gust': 1.55
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-23 09:00:00'
    }, {
        'dt':
        1663934400,
        'main': {
            'temp': 290.48,
            'feels_like': 289.26,
            'temp_min': 290.48,
            'temp_max': 290.48,
            'pressure': 1019,
            'sea_level': 1019,
            'grnd_level': 935,
            'humidity': 38,
            'temp_kf': 0
        },
        'weather': [{
            'id': 800,
            'main': 'Clear',
            'description': 'clear sky',
            'icon': '01d'
        }],
        'clouds': {
            'all': 3
        },
        'wind': {
            'speed': 2.02,
            'deg': 50,
            'gust': 2.26
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-23 12:00:00'
    }, {
        'dt':
        1663945200,
        'main': {
            'temp': 290.22,
            'feels_like': 289.11,
            'temp_min': 290.22,
            'temp_max': 290.22,
            'pressure': 1017,
            'sea_level': 1017,
            'grnd_level': 933,
            'humidity': 43,
            'temp_kf': 0
        },
        'weather': [{
            'id': 802,
            'main': 'Clouds',
            'description': 'scattered clouds',
            'icon': '03d'
        }],
        'clouds': {
            'all': 38
        },
        'wind': {
            'speed': 1.86,
            'deg': 58,
            'gust': 1.99
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-23 15:00:00'
    }, {
        'dt':
        1663956000,
        'main': {
            'temp': 283.45,
            'feels_like': 282.36,
            'temp_min': 283.45,
            'temp_max': 283.45,
            'pressure': 1018,
            'sea_level': 1018,
            'grnd_level': 932,
            'humidity': 70,
            'temp_kf': 0
        },
        'weather': [{
            'id': 803,
            'main': 'Clouds',
            'description': 'broken clouds',
            'icon': '04n'
        }],
        'clouds': {
            'all': 54
        },
        'wind': {
            'speed': 1.25,
            'deg': 202,
            'gust': 1.88
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-23 18:00:00'
    }, {
        'dt':
        1663966800,
        'main': {
            'temp': 282.7,
            'feels_like': 281.55,
            'temp_min': 282.7,
            'temp_max': 282.7,
            'pressure': 1019,
            'sea_level': 1019,
            'grnd_level': 932,
            'humidity': 70,
            'temp_kf': 0
        },
        'weather': [{
            'id': 804,
            'main': 'Clouds',
            'description': 'overcast clouds',
            'icon': '04n'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 2.35,
            'deg': 210,
            'gust': 2.69
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-23 21:00:00'
    }, {
        'dt':
        1663977600,
        'main': {
            'temp': 282.6,
            'feels_like': 281.32,
            'temp_min': 282.6,
            'temp_max': 282.6,
            'pressure': 1019,
            'sea_level': 1019,
            'grnd_level': 932,
            'humidity': 66,
            'temp_kf': 0
        },
        'weather': [{
            'id': 804,
            'main': 'Clouds',
            'description': 'overcast clouds',
            'icon': '04n'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 2.5,
            'deg': 209,
            'gust': 3.3
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-24 00:00:00'
    }, {
        'dt':
        1663988400,
        'main': {
            'temp': 283.14,
            'feels_like': 282.08,
            'temp_min': 283.14,
            'temp_max': 283.14,
            'pressure': 1018,
            'sea_level': 1018,
            'grnd_level': 932,
            'humidity': 71,
            'temp_kf': 0
        },
        'weather': [{
            'id': 804,
            'main': 'Clouds',
            'description': 'overcast clouds',
            'icon': '04n'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 2.33,
            'deg': 197,
            'gust': 3.74
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-24 03:00:00'
    }, {
        'dt':
        1663999200,
        'main': {
            'temp': 283.3,
            'feels_like': 282.43,
            'temp_min': 283.3,
            'temp_max': 283.3,
            'pressure': 1017,
            'sea_level': 1017,
            'grnd_level': 931,
            'humidity': 79,
            'temp_kf': 0
        },
        'weather': [{
            'id': 804,
            'main': 'Clouds',
            'description': 'overcast clouds',
            'icon': '04d'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 1.93,
            'deg': 196,
            'gust': 3.41
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-24 06:00:00'
    }, {
        'dt':
        1664010000,
        'main': {
            'temp': 287.83,
            'feels_like': 286.97,
            'temp_min': 287.83,
            'temp_max': 287.83,
            'pressure': 1017,
            'sea_level': 1017,
            'grnd_level': 932,
            'humidity': 62,
            'temp_kf': 0
        },
        'weather': [{
            'id': 804,
            'main': 'Clouds',
            'description': 'overcast clouds',
            'icon': '04d'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 1.15,
            'deg': 128,
            'gust': 2.27
        },
        'visibility':
        10000,
        'pop':
        0.25,
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-24 09:00:00'
    }, {
        'dt':
        1664020800,
        'main': {
            'temp': 284.27,
            'feels_like': 283.84,
            'temp_min': 284.27,
            'temp_max': 284.27,
            'pressure': 1016,
            'sea_level': 1016,
            'grnd_level': 930,
            'humidity': 92,
            'temp_kf': 0
        },
        'weather': [{
            'id': 501,
            'main': 'Rain',
            'description': 'moderate rain',
            'icon': '10d'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 0.7,
            'deg': 111,
            'gust': 1.8
        },
        'visibility':
        4350,
        'pop':
        0.73,
        'rain': {
            '3h': 6.68
        },
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-24 12:00:00'
    }, {
        'dt':
        1664031600,
        'main': {
            'temp': 283.86,
            'feels_like': 283.57,
            'temp_min': 283.86,
            'temp_max': 283.86,
            'pressure': 1015,
            'sea_level': 1015,
            'grnd_level': 929,
            'humidity': 99,
            'temp_kf': 0
        },
        'weather': [{
            'id': 502,
            'main': 'Rain',
            'description': 'heavy intensity rain',
            'icon': '10d'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 0.9,
            'deg': 42,
            'gust': 1.51
        },
        'visibility':
        1677,
        'pop':
        1,
        'rain': {
            '3h': 17.04
        },
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-24 15:00:00'
    }, {
        'dt':
        1664042400,
        'main': {
            'temp': 283.72,
            'feels_like': 283.42,
            'temp_min': 283.72,
            'temp_max': 283.72,
            'pressure': 1015,
            'sea_level': 1015,
            'grnd_level': 929,
            'humidity': 99,
            'temp_kf': 0
        },
        'weather': [{
            'id': 501,
            'main': 'Rain',
            'description': 'moderate rain',
            'icon': '10n'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 1.34,
            'deg': 51,
            'gust': 2.25
        },
        'visibility':
        3654,
        'pop':
        1,
        'rain': {
            '3h': 9.89
        },
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-24 18:00:00'
    }, {
        'dt':
        1664053200,
        'main': {
            'temp': 283.5,
            'feels_like': 283.18,
            'temp_min': 283.5,
            'temp_max': 283.5,
            'pressure': 1015,
            'sea_level': 1015,
            'grnd_level': 929,
            'humidity': 99,
            'temp_kf': 0
        },
        'weather': [{
            'id': 500,
            'main': 'Rain',
            'description': 'light rain',
            'icon': '10n'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 0.92,
            'deg': 6,
            'gust': 1.51
        },
        'visibility':
        3219,
        'pop':
        1,
        'rain': {
            '3h': 2.67
        },
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-24 21:00:00'
    }, {
        'dt':
        1664064000,
        'main': {
            'temp': 283.6,
            'feels_like': 283.29,
            'temp_min': 283.6,
            'temp_max': 283.6,
            'pressure': 1014,
            'sea_level': 1014,
            'grnd_level': 928,
            'humidity': 99,
            'temp_kf': 0
        },
        'weather': [{
            'id': 804,
            'main': 'Clouds',
            'description': 'overcast clouds',
            'icon': '04n'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 1.01,
            'deg': 7,
            'gust': 1.48
        },
        'visibility':
        3057,
        'pop':
        0.8,
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-25 00:00:00'
    }, {
        'dt':
        1664074800,
        'main': {
            'temp': 283.71,
            'feels_like': 283.41,
            'temp_min': 283.71,
            'temp_max': 283.71,
            'pressure': 1013,
            'sea_level': 1013,
            'grnd_level': 927,
            'humidity': 99,
            'temp_kf': 0
        },
        'weather': [{
            'id': 804,
            'main': 'Clouds',
            'description': 'overcast clouds',
            'icon': '04n'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 0.94,
            'deg': 19,
            'gust': 1.44
        },
        'visibility':
        3058,
        'pop':
        0.45,
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-25 03:00:00'
    }, {
        'dt':
        1664085600,
        'main': {
            'temp': 283.8,
            'feels_like': 283.51,
            'temp_min': 283.8,
            'temp_max': 283.8,
            'pressure': 1013,
            'sea_level': 1013,
            'grnd_level': 927,
            'humidity': 99,
            'temp_kf': 0
        },
        'weather': [{
            'id': 804,
            'main': 'Clouds',
            'description': 'overcast clouds',
            'icon': '04d'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 0.73,
            'deg': 27,
            'gust': 0.92
        },
        'visibility':
        3168,
        'pop':
        0.37,
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-25 06:00:00'
    }, {
        'dt':
        1664096400,
        'main': {
            'temp': 284.61,
            'feels_like': 284.34,
            'temp_min': 284.61,
            'temp_max': 284.61,
            'pressure': 1013,
            'sea_level': 1013,
            'grnd_level': 928,
            'humidity': 97,
            'temp_kf': 0
        },
        'weather': [{
            'id': 804,
            'main': 'Clouds',
            'description': 'overcast clouds',
            'icon': '04d'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 0.59,
            'deg': 62,
            'gust': 0.89
        },
        'visibility':
        7918,
        'pop':
        0.37,
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-25 09:00:00'
    }, {
        'dt':
        1664107200,
        'main': {
            'temp': 286.94,
            'feels_like': 286.7,
            'temp_min': 286.94,
            'temp_max': 286.94,
            'pressure': 1012,
            'sea_level': 1012,
            'grnd_level': 927,
            'humidity': 89,
            'temp_kf': 0
        },
        'weather': [{
            'id': 500,
            'main': 'Rain',
            'description': 'light rain',
            'icon': '10d'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 0.84,
            'deg': 71,
            'gust': 1.99
        },
        'visibility':
        10000,
        'pop':
        0.53,
        'rain': {
            '3h': 0.76
        },
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-25 12:00:00'
    }, {
        'dt':
        1664118000,
        'main': {
            'temp': 286.73,
            'feels_like': 286.49,
            'temp_min': 286.73,
            'temp_max': 286.73,
            'pressure': 1011,
            'sea_level': 1011,
            'grnd_level': 927,
            'humidity': 90,
            'temp_kf': 0
        },
        'weather': [{
            'id': 500,
            'main': 'Rain',
            'description': 'light rain',
            'icon': '10d'
        }],
        'clouds': {
            'all': 92
        },
        'wind': {
            'speed': 1.01,
            'deg': 351,
            'gust': 1.43
        },
        'visibility':
        9633,
        'pop':
        0.53,
        'rain': {
            '3h': 0.55
        },
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-25 15:00:00'
    }, {
        'dt':
        1664128800,
        'main': {
            'temp': 284.92,
            'feels_like': 284.66,
            'temp_min': 284.92,
            'temp_max': 284.92,
            'pressure': 1013,
            'sea_level': 1013,
            'grnd_level': 927,
            'humidity': 96,
            'temp_kf': 0
        },
        'weather': [{
            'id': 500,
            'main': 'Rain',
            'description': 'light rain',
            'icon': '10n'
        }],
        'clouds': {
            'all': 95
        },
        'wind': {
            'speed': 0.42,
            'deg': 69,
            'gust': 0.81
        },
        'visibility':
        8035,
        'pop':
        0.49,
        'rain': {
            '3h': 0.27
        },
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-25 18:00:00'
    }, {
        'dt':
        1664139600,
        'main': {
            'temp': 284.45,
            'feels_like': 284.12,
            'temp_min': 284.45,
            'temp_max': 284.45,
            'pressure': 1013,
            'sea_level': 1013,
            'grnd_level': 928,
            'humidity': 95,
            'temp_kf': 0
        },
        'weather': [{
            'id': 804,
            'main': 'Clouds',
            'description': 'overcast clouds',
            'icon': '04n'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 0.36,
            'deg': 274,
            'gust': 0.87
        },
        'visibility':
        10000,
        'pop':
        0.02,
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-25 21:00:00'
    }, {
        'dt':
        1664150400,
        'main': {
            'temp': 284.13,
            'feels_like': 283.76,
            'temp_min': 284.13,
            'temp_max': 284.13,
            'pressure': 1013,
            'sea_level': 1013,
            'grnd_level': 928,
            'humidity': 95,
            'temp_kf': 0
        },
        'weather': [{
            'id': 804,
            'main': 'Clouds',
            'description': 'overcast clouds',
            'icon': '04n'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 0.85,
            'deg': 245,
            'gust': 1
        },
        'visibility':
        10000,
        'pop':
        0.02,
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-26 00:00:00'
    }, {
        'dt':
        1664161200,
        'main': {
            'temp': 282.95,
            'feels_like': 282.5,
            'temp_min': 282.95,
            'temp_max': 282.95,
            'pressure': 1013,
            'sea_level': 1013,
            'grnd_level': 927,
            'humidity': 94,
            'temp_kf': 0
        },
        'weather': [{
            'id': 803,
            'main': 'Clouds',
            'description': 'broken clouds',
            'icon': '04n'
        }],
        'clouds': {
            'all': 71
        },
        'wind': {
            'speed': 1.57,
            'deg': 229,
            'gust': 1.75
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-26 03:00:00'
    }, {
        'dt':
        1664172000,
        'main': {
            'temp': 282.99,
            'feels_like': 282.34,
            'temp_min': 282.99,
            'temp_max': 282.99,
            'pressure': 1012,
            'sea_level': 1012,
            'grnd_level': 926,
            'humidity': 92,
            'temp_kf': 0
        },
        'weather': [{
            'id': 803,
            'main': 'Clouds',
            'description': 'broken clouds',
            'icon': '04d'
        }],
        'clouds': {
            'all': 76
        },
        'wind': {
            'speed': 1.78,
            'deg': 198,
            'gust': 2.04
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-26 06:00:00'
    }, {
        'dt':
        1664182800,
        'main': {
            'temp': 287.62,
            'feels_like': 287.08,
            'temp_min': 287.62,
            'temp_max': 287.62,
            'pressure': 1012,
            'sea_level': 1012,
            'grnd_level': 927,
            'humidity': 75,
            'temp_kf': 0
        },
        'weather': [{
            'id': 804,
            'main': 'Clouds',
            'description': 'overcast clouds',
            'icon': '04d'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 1.16,
            'deg': 168,
            'gust': 2.66
        },
        'visibility':
        10000,
        'pop':
        0.04,
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-26 09:00:00'
    }, {
        'dt':
        1664193600,
        'main': {
            'temp': 289.92,
            'feels_like': 289.17,
            'temp_min': 289.92,
            'temp_max': 289.92,
            'pressure': 1010,
            'sea_level': 1010,
            'grnd_level': 926,
            'humidity': 58,
            'temp_kf': 0
        },
        'weather': [{
            'id': 500,
            'main': 'Rain',
            'description': 'light rain',
            'icon': '10d'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 0.95,
            'deg': 206,
            'gust': 3.86
        },
        'visibility':
        10000,
        'pop':
        0.2,
        'rain': {
            '3h': 0.19
        },
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-26 12:00:00'
    }, {
        'dt':
        1664204400,
        'main': {
            'temp': 288.83,
            'feels_like': 288.15,
            'temp_min': 288.83,
            'temp_max': 288.83,
            'pressure': 1009,
            'sea_level': 1009,
            'grnd_level': 925,
            'humidity': 65,
            'temp_kf': 0
        },
        'weather': [{
            'id': 500,
            'main': 'Rain',
            'description': 'light rain',
            'icon': '10d'
        }],
        'clouds': {
            'all': 100
        },
        'wind': {
            'speed': 1.61,
            'deg': 213,
            'gust': 4.17
        },
        'visibility':
        10000,
        'pop':
        0.31,
        'rain': {
            '3h': 0.2
        },
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-26 15:00:00'
    }, {
        'dt':
        1664215200,
        'main': {
            'temp': 283.63,
            'feels_like': 282.93,
            'temp_min': 283.63,
            'temp_max': 283.63,
            'pressure': 1009,
            'sea_level': 1009,
            'grnd_level': 924,
            'humidity': 84,
            'temp_kf': 0
        },
        'weather': [{
            'id': 804,
            'main': 'Clouds',
            'description': 'overcast clouds',
            'icon': '04n'
        }],
        'clouds': {
            'all': 85
        },
        'wind': {
            'speed': 2.81,
            'deg': 215,
            'gust': 3.92
        },
        'visibility':
        10000,
        'pop':
        0.19,
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-26 18:00:00'
    }, {
        'dt':
        1664226000,
        'main': {
            'temp': 282.65,
            'feels_like': 281.14,
            'temp_min': 282.65,
            'temp_max': 282.65,
            'pressure': 1009,
            'sea_level': 1009,
            'grnd_level': 923,
            'humidity': 87,
            'temp_kf': 0
        },
        'weather': [{
            'id': 803,
            'main': 'Clouds',
            'description': 'broken clouds',
            'icon': '04n'
        }],
        'clouds': {
            'all': 68
        },
        'wind': {
            'speed': 2.87,
            'deg': 205,
            'gust': 3.92
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-26 21:00:00'
    }, {
        'dt':
        1664236800,
        'main': {
            'temp': 283.33,
            'feels_like': 282.6,
            'temp_min': 283.33,
            'temp_max': 283.33,
            'pressure': 1007,
            'sea_level': 1007,
            'grnd_level': 922,
            'humidity': 84,
            'temp_kf': 0
        },
        'weather': [{
            'id': 803,
            'main': 'Clouds',
            'description': 'broken clouds',
            'icon': '04n'
        }],
        'clouds': {
            'all': 84
        },
        'wind': {
            'speed': 2.67,
            'deg': 204,
            'gust': 3.46
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-27 00:00:00'
    }, {
        'dt':
        1664247600,
        'main': {
            'temp': 282.46,
            'feels_like': 281.05,
            'temp_min': 282.46,
            'temp_max': 282.46,
            'pressure': 1006,
            'sea_level': 1006,
            'grnd_level': 921,
            'humidity': 86,
            'temp_kf': 0
        },
        'weather': [{
            'id': 802,
            'main': 'Clouds',
            'description': 'scattered clouds',
            'icon': '03n'
        }],
        'clouds': {
            'all': 34
        },
        'wind': {
            'speed': 2.66,
            'deg': 205,
            'gust': 3.37
        },
        'visibility':
        10000,
        'pop':
        0,
        'sys': {
            'pod': 'n'
        },
        'dt_txt':
        '2022-09-27 03:00:00'
    }, {
        'dt':
        1664258400,
        'main': {
            'temp': 283.63,
            'feels_like': 282.9,
            'temp_min': 283.63,
            'temp_max': 283.63,
            'pressure': 1005,
            'sea_level': 1005,
            'grnd_level': 920,
            'humidity': 83,
            'temp_kf': 0
        },
        'weather': [{
            'id': 802,
            'main': 'Clouds',
            'description': 'scattered clouds',
            'icon': '03d'
        }],
        'clouds': {
            'all': 36
        },
        'wind': {
            'speed': 2.18,
            'deg': 209,
            'gust': 3.78
        },
        'visibility':
        10000,
        'pop':
        0.08,
        'sys': {
            'pod': 'd'
        },
        'dt_txt':
        '2022-09-27 06:00:00'
    }],
    'city': {
        'id': 3163858,
        'name': 'Zocca',
        'coord': {
            'lat': 44.34,
            'lon': 10.99
        },
        'country': 'IT',
        'population': 4593,
        'timezone': 7200,
        'sunrise': 1663822972,
        'sunset': 1663866893
    }
}
