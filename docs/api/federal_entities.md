# Federal Entities

Supports registering, viewing, and updating federal entities.

## Register a new federal entity

**Request**:

`POST` `/api/v1/federal-entity/`

Parameters:

 Name | Type   | Required | Description                                 
------|--------|----------|---------------------------------------------
 key  | string | Yes      | Federal Entity identifier (not primary key) 
 name | string | Yes      | Federal entity name                         
 code | string | No       | Empty field                                 

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
201 Created
{
  "id": 1,
  "key": "19",
  "name": "NUEVO LEÓN",
  "code": null
}
```

## List of federal entities

**Request**:

`GET` `api/v1/federal-entities/`

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
      "key": "19",
      "name": "NUEVO LEÓN",
      "code": "nan"
    }
  ]
}
```

## Get a federal entity information

**Request**:

`GET` `api/v1/federal-entities/:id`

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
      "key": "19",
      "name": "NUEVO LEÓN",
      "code": "nan"
    }
  ]
}
```

## Update federal entity's information

**Request**:

`PUT/PATCH` `api/v1/federal-entities/:id`

Parameters:

 Name | Type   | Description                                 
------|--------|---------------------------------------------
 key  | string | Federal entity identifier (not primary key) 
 name | string | Federal entity name                         
 code | string | Empty field                                 

*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": 1,
  "key": "19",
  "name": "NUEVO LEÓN",
  "code": null
}
```
