## search Type

`object` ([Search Settings](conf-properties-search-settings.md))

any of

*   [Search configuration with Typesense](conf-properties-search-settings-anyof-search-configuration-with-typesense.md "check type definition")

*   [Search configuration with ElasticSearch](conf-properties-search-settings-anyof-search-configuration-with-elasticsearch.md "check type definition")

# search Properties

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                    |
| :------------------------------ | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| [engine](#engine)               | `string` | Required | cannot be null | [Configuration](conf-properties-search-settings-properties-engine.md "undefined#/properties/search/properties/engine")                        |
| [typesense](#typesense)         | `object` | Optional | cannot be null | [Configuration](conf-properties-search-settings-properties-typesense-settings.md "undefined#/properties/search/properties/typesense")         |
| [elasticsearch](#elasticsearch) | `object` | Optional | cannot be null | [Configuration](conf-properties-search-settings-properties-elasticsearch-settings.md "undefined#/properties/search/properties/elasticsearch") |

## engine

Search engine to use

`engine`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Configuration](conf-properties-search-settings-properties-engine.md "undefined#/properties/search/properties/engine")

### engine Type

`string`

### engine Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation |
| :---------------- | :---------- |
| `"elasticsearch"` |             |
| `"typesense"`     |             |

## typesense

Settings for the Typesense search engine

`typesense`

*   is optional

*   Type: `object` ([Typesense Settings](conf-properties-search-settings-properties-typesense-settings.md))

*   cannot be null

*   defined in: [Configuration](conf-properties-search-settings-properties-typesense-settings.md "undefined#/properties/search/properties/typesense")

### typesense Type

`object` ([Typesense Settings](conf-properties-search-settings-properties-typesense-settings.md))

## elasticsearch

Settings for the ElasticSearch search engine

`elasticsearch`

*   is optional

*   Type: `object` ([ElasticSearch Settings](conf-properties-search-settings-properties-elasticsearch-settings.md))

*   cannot be null

*   defined in: [Configuration](conf-properties-search-settings-properties-elasticsearch-settings.md "undefined#/properties/search/properties/elasticsearch")

### elasticsearch Type

`object` ([ElasticSearch Settings](conf-properties-search-settings-properties-elasticsearch-settings.md))
