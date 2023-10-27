# Settlement Types

Supports registering, viewing, and updating settlement types.

## Register a new settlement type

**Request**:

`POST` `/api/v1/settlements/settlement-type/`

Parameters:

 Name | Type   | Required | Description                                    
------|--------|----------|------------------------------------------------
 name | string | Yes      | Name of the settlement type e.g. "Condominio". 

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
201 Created

{
  "id": 3,
  "name": "RANCHO"
}
```

## List settlement types

**Request**:

`GET` `api/v1/settlements/settlement-types/`

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
      "name": "COLONIA"
    }
  ]
}
```




## Get a settlement type's information

**Request**:

`GET` `api/v1/settlements/settlement-types/:id`

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
      "name": "COLONIA"
    }
  ]
}
```

## Update settlement type information

**Request**:

`PUT/PATCH` `api/v1/settlements/settlement-types/:id`

Parameters:

 Name | Type   | Description                                    
------|--------|------------------------------------------------
 name | string | Name of the settlement type e.g. "Condominio". 

*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": 1,
  "name": "COLONIA"
}
```
