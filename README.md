# A00444846_django

For Changing Database you have to change it in `settings.py`

You have to create blank database with name 'hoteldb'

SQL query: `create database hoteldb;`


#### GET API: http://127.0.0.1:8000/HotelList/


Response:
``` 
[
    {
        "id": 1,
        "name": "pratik",
        "price": 111.0
    }
] 
```



#### POST API: http://127.0.0.1:8000/HotelList/

Body:
``` 
{
    "id":2,
    "name":"pratik",
    "price":111
}
```

Response: 
```
{
    "Message": "Saved successfully"
}
```
