# Municipalities

Supports registering, viewing, and updating municipalities.

## Register a new municipality

**Request**:

`POST` `/api/v1/municipality/`

Parameters:

 Name | Type   | Required | Description                               
------|--------|----------|-------------------------------------------
 key  | string | Yes      | Municipality identifier (not primary key) 
 name | string | Yes      | Municipality name                         

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
201 Created

{
    "id": 1,
    "key": "039",
    "name": "Monterrey"
}
```

## List of municipalities

**Request**:

`GET` `/api/v1/municipalities/`

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
            "id": 1,
            "key": "039",
            "name": "Monterrey"
        }
    ]
}
```

## Get a municipality information

**Request**:

`GET` `/api/v1/municipalities/:id`

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
            "id": 1,
            "key": "039",
            "name": "Monterrey"
        }
    ]
}
```

## Update municipality's information

**Request**:

`PUT/PATCH` `/api/v1/municipalities/:id`

Parameters:

 Name | Type   | Description                             
------|--------|-----------------------------------------
 key  | string | Municipality identifier (not primary key) 
 name | string | Municipality name                         
                        

*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
    "id": 1,
    "key": "039",
    "name": "Monterrey"
}
```
