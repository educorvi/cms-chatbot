## typesense Type

`object` ([Typesense Settings](conf-properties-search-settings-properties-typesense-settings.md))

# typesense Properties

| Property                         | Type      | Required | Nullable       | Defined by                                                                                                                                                                              |
| :------------------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [host](#host)                    | `string`  | Required | cannot be null | [Configuration](conf-properties-search-settings-properties-typesense-settings-properties-host.md "undefined#/properties/search/properties/typesense/properties/host")                   |
| [port](#port)                    | `integer` | Required | cannot be null | [Configuration](conf-properties-search-settings-properties-typesense-settings-properties-port.md "undefined#/properties/search/properties/typesense/properties/port")                   |
| [protocol](#protocol)            | `string`  | Required | cannot be null | [Configuration](conf-properties-search-settings-properties-typesense-settings-properties-protocol.md "undefined#/properties/search/properties/typesense/properties/protocol")           |
| [collection](#collection)        | `string`  | Required | cannot be null | [Configuration](conf-properties-search-settings-properties-typesense-settings-properties-collection.md "undefined#/properties/search/properties/typesense/properties/collection")       |
| [result\_number](#result_number) | `integer` | Required | cannot be null | [Configuration](conf-properties-search-settings-properties-typesense-settings-properties-result_number.md "undefined#/properties/search/properties/typesense/properties/result_number") |
| [result\_size](#result_size)     | `integer` | Required | cannot be null | [Configuration](conf-properties-search-settings-properties-typesense-settings-properties-result_size.md "undefined#/properties/search/properties/typesense/properties/result_size")     |
| [api\_key](#api_key)             | `string`  | Required | cannot be null | [Configuration](conf-properties-search-settings-properties-typesense-settings-properties-api_key.md "undefined#/properties/search/properties/typesense/properties/api_key")             |

## host

Hostname of the Typesense server

`host`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Configuration](conf-properties-search-settings-properties-typesense-settings-properties-host.md "undefined#/properties/search/properties/typesense/properties/host")

### host Type

`string`

## port

Port of the Typesense server

`port`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Configuration](conf-properties-search-settings-properties-typesense-settings-properties-port.md "undefined#/properties/search/properties/typesense/properties/port")

### port Type

`integer`

## protocol

Protocol of the Typesense server

`protocol`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Configuration](conf-properties-search-settings-properties-typesense-settings-properties-protocol.md "undefined#/properties/search/properties/typesense/properties/protocol")

### protocol Type

`string`

### protocol Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | :---------- |
| `"http"`  |             |
| `"https"` |             |

## collection

Name of the Typesense collection

`collection`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Configuration](conf-properties-search-settings-properties-typesense-settings-properties-collection.md "undefined#/properties/search/properties/typesense/properties/collection")

### collection Type

`string`

## result\_number

Number of results returned per query

`result_number`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Configuration](conf-properties-search-settings-properties-typesense-settings-properties-result_number.md "undefined#/properties/search/properties/typesense/properties/result_number")

### result\_number Type

`integer`

## result\_size

Number of tokens before and after highlight

`result_size`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Configuration](conf-properties-search-settings-properties-typesense-settings-properties-result_size.md "undefined#/properties/search/properties/typesense/properties/result_size")

### result\_size Type

`integer`

## api\_key

API key for the Typesense server

`api_key`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Configuration](conf-properties-search-settings-properties-typesense-settings-properties-api_key.md "undefined#/properties/search/properties/typesense/properties/api_key")

### api\_key Type

`string`
