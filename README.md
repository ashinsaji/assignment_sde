# Configuration Management API

This API manages configuration requirements for onboarding organizations from various countries. It supports CRUD (Create, Read, Update, Delete) operations on country-specific configurations.

## Running the App

To run the app, you can use the Uvicorn server. Follow the steps below:

1. Install Uvicorn by running the following command in your terminal:

```bash
pip install uvicorn
pip install -r requirements.txt
```

2. Navigate to the root directory of your project.

3. Start the Uvicorn server by running the following command:

```bash
uvicorn main:app --reload
```

This command starts the server and enables auto-reloading, which means any changes you make to the code will automatically be reflected without having to restart the server.

4. Once the server is running, you can access the API endpoints using the appropriate URLs. For example, if you're running the app locally, you can access the endpoints at `http://localhost:8000`.

## Endpoints

### 1. Create Configuration

- Endpoint: /create_configuration/
- Method: POST
- Description: Creates a configuration of a country's onboarding requirements.

#### Request

Body Parameters:

- country_code (string, required): The country code (e.g., "IN", "US").
- requirements (object, required): A dictionary containing the onboarding requirements.

Example:

```json
{
  "country_code": "IN",
  "requirements": {
    "BusinessName": "required",
    "PAN": "required",
    "GSTIN": "required"
  }
}
```

#### Response

Status: 200 OK

Body:

```json
{
  "id": 1,
  "country_code": "IN",
  "requirements": {
    "BusinessName": "required",
    "PAN": "required",
    "GSTIN": "required"
  }
}
```

#### Errors

400 Bad Request: Configuration already exists for this country.

### 2. Get Configuration

- Endpoint: /get_configuration/{country_code}
- Method: GET
- Description: Retrieves the configuration requirements of a country.

#### Request

Path Parameters:

- country_code (string, required): The country code (e.g., "IN", "US").

#### Response

Status: 200 OK

Body:

```json
{
  "id": 1,
  "country_code": "IN",
  "requirements": {
    "BusinessName": "required",
    "PAN": "required",
    "GSTIN": "required"
  }
}
```

#### Errors

404 Not Found: Configuration not found for the specified country.

### 3. Update Configuration

- Endpoint: /update_configuration/
- Method: POST
- Description: Updates the configuration requirements of a country.

#### Request

Body Parameters:

- country_code (string, required): The country code (e.g., "IN", "US").
- requirements (object, required): A dictionary containing the updated onboarding requirements.

Example:

```json
{
  "country_code": "IN",
  "requirements": {
    "BusinessName": "required",
    "PAN": "required",
    "GSTIN": "optional",
    "AdditionalField": "required"
  }
}
```

#### Response

Status: 200 OK

Body:

```json
{
  "id": 1,
  "country_code": "IN",
  "requirements": {
    "BusinessName": "required",
    "PAN": "required",
    "GSTIN": "optional",
    "AdditionalField": "required"
  }
}
```

#### Errors

404 Not Found: Configuration not found for the specified country.

### 4. Delete Configuration

- Endpoint: /delete_configuration/
- Method: DELETE
- Description: Deletes the configuration requirements of a country.

#### Request

Query Parameters:

- country_code (string, required): The country code (e.g., "IN", "US").

Example:

```bash
/delete_configuration/?country_code=IN
```

#### Response

Status: 200 OK

Body:

```json
true
```

#### Errors

404 Not Found: Configuration not found for the specified country.

## Error Handling

The API uses standard HTTP status codes to indicate the success or failure of API requests. In case of errors, the response body includes a JSON object with a descriptive error message.

### Common Errors

- 400 Bad Request: The request data is invalid.
- 404 Not Found: The specified resource was not found.
- 500 Internal Server Error: An unexpected error occurred on the server.

### Example Error Response

Status: 404 Not Found

Body:

```json
{
  "detail": "Configuration not found"
}
```
