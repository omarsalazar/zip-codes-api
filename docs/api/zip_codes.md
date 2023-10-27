# Zip Codes

Supports registering and viewing zip codes.

## Register a new zip code

**Request**:

`POST` `/api/v1/zip-code/`

Parameters:

 Name           | Type   | Required | Description                            
----------------|--------|----------|----------------------------------------
 zip_code       | string | Yes      | Zip Code identifier (not primary key)  
 locality       | string | Yes      | Federal entity name                    
 federal_entity | int    | Yes      | primary key of a federal_entity object 
 municipality   | int    | Yes      | primary key of a municipality object   

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
201 Created
{
  "id": 1,
  "zip_code": "64000",
  "locality": "Monterrey",
  "federal_entity": 1,
  "municipality": 1
}
```

## List of zip codes

**Request**:

`GET` `api/v1/zip-codes/`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "count": 3349,
  "next": "http://0.0.0.0:8000/api/v1/zip-codes/?page=2",
  "previous": null,
  "results": [
    {
      "zip_code": "64000",
      "locality": "MONTERREY",
      "federal_entity": {
        "key": "19",
        "name": "NUEVO LEÓN",
        "code": null
      },
      "municipality": {
        "key": "39",
        "name": "Monterrey"
      },
      "settlements": [
        {
          "key": "0001",
          "name": "Monterrey Centro",
          "zone_type": "Urbano",
          "settlement_type": {
            "name": "COLONIA"
          }
        },
        {
          "key": "3429",
          "name": "La Finca",
          "zone_type": "Urbano",
          "settlement_type": {
            "name": "CONDOMINIO"
          }
        }
      ]
    },
    {
      "zip_code": "64010",
      "locality": "MONTERREY",
      "federal_entity": {
        "key": "19",
        "name": "NUEVO LEÓN",
        "code": null
      },
      "municipality": {
        "key": "39",
        "name": "Monterrey"
      },
      "settlements": [
        {
          "key": "0011",
          "name": "Obrera",
          "zone_type": "Urbano",
          "settlement_type": {
            "name": "COLONIA"
          }
        }
      ]
    }
  ]
}
```

## Get a zip code information

**Request**:

`GET` `api/v1/zip-codes/?zip-code=:zip_code`

Query Parameters:

 Name     | Type   | Required | Description                           
----------|--------|----------|---------------------------------------
 zip_code | string | No       | Zip Code identifier (not primary key) 

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "zip_code": "64000",
      "locality": "MONTERREY",
      "federal_entity": {
        "key": "19",
        "name": "NUEVO LEÓN",
        "code": null
      },
      "municipality": {
        "key": "39",
        "name": "Monterrey"
      },
      "settlements": [
        {
          "key": "0001",
          "name": "Monterrey Centro",
          "zone_type": "Urbano",
          "settlement_type": {
            "name": "COLONIA"
          }
        },
        {
          "key": "3429",
          "name": "La Finca",
          "zone_type": "Urbano",
          "settlement_type": {
            "name": "CONDOMINIO"
          }
        }
      ]
    }
  ]
}
```
