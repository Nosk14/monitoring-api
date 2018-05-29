# monitoring-api
Just a simple api to store data about home environment

```
[PUT] /data
{
   "zone":"test_zone",
    "data": [
        {
            "time":"2017-09-14T00:00:00",
            "temperature": 22.34,
            "humidity": null
        },
        {
            "time": "2018-09-14T22:33:14",
            "temperature": 18,
            "humidity": 87.5
        }
    ]
}
```