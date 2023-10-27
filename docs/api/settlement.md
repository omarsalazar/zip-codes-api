# Settlements

Supports registering, viewing, and updating settlements.

## Register a new settlement

**Request**:

`POST` `/api/v1/settlement/`

Parameters:

 Name            | Type    | Required | Description                             
-----------------|---------|----------|-----------------------------------------
 key             | string  | Yes      | Settlement identifier (not primary key) 
 name            | string  | Yes      | Settlement name                         
 zone_type       | string  | Yes      | Type of the settlement (URBANO/RURAL)   
 settlement_type | integer | Yes      | primary key of a settlement_type object 
 zip_code        | integer | Yes      | primary key of a zip_code object        

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
201 Created

{
  "id": 4,
  "key": "0001",
  "name": "Monterrey Centro",
  "zone_type": "Urbano",
  "settlement_type": 1,
  "zip_code": 1
}
```

## Get a settlement's information

**Request**:

`GET` `api/v1/settlements/:id`

Parameters:

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
      "id": 3,
      "key": "3429",
      "name": "La Finca",
      "zone_type": "Urbano",
      "settlement_type": 2,
      "zip_code": 1
    }
  ]
}
```

## List settlements

**Request**:

`GET` `api/v1/settlements/`

Parameters:

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
      "id": 3,
      "key": "3429",
      "name": "La Finca",
      "zone_type": "Urbano",
      "settlement_type": 2,
      "zip_code": 1
    }
  ]
}
```



## Update settlement's information

**Request**:

`PUT/PATCH` `api/v1/settlements/:id`

Parameters:

 Name            | Type    | Description                             
-----------------|---------|-----------------------------------------
 key             | string  | Settlement identifier (not primary key) 
 name            | string  | Settlement name                         
 zone_type       | string  | Type of the settlement (URBANO/RURAL)   
 settlement_type | integer | primary key of a settlement_type object 
 zip_code        | integer | primary key of a zip_code object        

*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": 4,
  "key": "0001",
  "name": "Monterrey Centro",
  "zone_type": "Urbano",
  "settlement_type": 1,
  "zip_code": 1
}
```
