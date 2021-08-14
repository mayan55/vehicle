"# vehicle" 

Postman collection added. filename `nextlua.postman_collection.json`
<hr/>

####GET
http://localhost:8000/api/vehicle/
````
[
    {
        "vehicle_model": {
            "name": "FOCUS",
            "brand": "FORD",
            "id": 1
        },
        "id": 2,
        "plaka": "34kb1484MM",
        "km": 9000000,
        "sase_no": "kjahdkjhajkdhhadkha",
        "renk": "beyaz"
    }
]

````

<hr/>

####GET 
http://localhost:8000/api/vehicle/id
````
{
    "vehicle_model": {
        "name": "CLİO",
        "brand": "RENAULT",
        "id": 2
    },
    "id": 5,
    "plaka": "ccc",
    "km": 9000000,
    "sase_no": "kjahdkjhajkdhhadkha",
    "renk": "beyaz"
}
````
<hr/>

####POST
http://localhost:8000/api/vehicle/

<br>

```
{
	"vehicle_model_id":1,
	"plaka":"34KB3434",
	"km":250000,
	"sase_no":"kjahdkjhajkdhhadkha",
	"renk":"beyaz"
}
```
<hr/>

####PUT
http://localhost:8000/api/vehicle/id/

<br>

```
{
	"vehicle_model_id":2,
	"plaka":"ccc",
	"km":9000000,
	"sase_no":"kjahdkjhajkdhhadkha",
	"renk":"beyaz"
}
```
<hr/>

####DELETE
http://localhost:8000/api/vehicle/id/
