## elasticsearch Type

`object` ([ElasticSearch Settings](conf-properties-search-settings-properties-elasticsearch-settings.md))

# elasticsearch Properties

| Property                         | Type      | Required | Nullable       | Defined by                                                                                                                                                                                      |
| :------------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [url](#url)                      | `string`  | Required | cannot be null | [Configuration](conf-properties-search-settings-properties-elasticsearch-settings-properties-url.md "undefined#/properties/search/properties/elasticsearch/properties/url")                     |
| [index](#index)                  | `string`  | Required | cannot be null | [Configuration](conf-properties-search-settings-properties-elasticsearch-settings-properties-index.md "undefined#/properties/search/properties/elasticsearch/properties/index")                 |
| [result\_number](#result_number) | `integer` | Required | cannot be null | [Configuration](conf-properties-search-settings-properties-elasticsearch-settings-properties-result_number.md "undefined#/properties/search/properties/elasticsearch/properties/result_number") |
| [result\_size](#result_size)     | `integer` | Required | cannot be null | [Configuration](conf-properties-search-settings-properties-elasticsearch-settings-properties-result_size.md "undefined#/properties/search/properties/elasticsearch/properties/result_size")     |

## url

URL of the ElasticSearch server

`url`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Configuration](conf-properties-search-settings-properties-elasticsearch-settings-properties-url.md "undefined#/properties/search/properties/elasticsearch/properties/url")

### url Type

`string`

## index

Name of the ElasticSearch index

`index`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Configuration](conf-properties-search-settings-properties-elasticsearch-settings-properties-index.md "undefined#/properties/search/properties/elasticsearch/properties/index")

### index Type

`string`

## result\_number

Number of results returned per query

`result_number`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Configuration](conf-properties-search-settings-properties-elasticsearch-settings-properties-result_number.md "undefined#/properties/search/properties/elasticsearch/properties/result_number")

### result\_number Type

`integer`

## result\_size

Number of characters per result

`result_size`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Configuration](conf-properties-search-settings-properties-elasticsearch-settings-properties-result_size.md "undefined#/properties/search/properties/elasticsearch/properties/result_size")

### result\_size Type

`integer`
