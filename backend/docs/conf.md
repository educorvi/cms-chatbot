## Configuration Type

`object` ([Configuration](conf.md))

# Configuration Properties

| Property                           | Type     | Required | Nullable       | Defined by                                                                                        |
| :--------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------ |
| [$schema](#schema)                 | `string` | Optional | cannot be null | [Configuration](conf-properties-schema.md "undefined#/properties/$schema")                        |
| [open\_ai](#open_ai)               | `object` | Required | cannot be null | [Configuration](conf-properties-openai-settings.md "undefined#/properties/open_ai")               |
| [search](#search)                  | Merged   | Required | cannot be null | [Configuration](conf-properties-search-settings.md "undefined#/properties/search")                |
| [websocket](#websocket)            | `object` | Required | cannot be null | [Configuration](conf-properties-websocket-settings.md "undefined#/properties/websocket")          |
| [deepl](#deepl)                    | `object` | Optional | cannot be null | [Configuration](conf-properties-deepl-settings.md "undefined#/properties/deepl")                  |
| [source\_replace](#source_replace) | `object` | Optional | cannot be null | [Configuration](conf-properties-source-url-replacement.md "undefined#/properties/source_replace") |

## $schema

Schema of the configuration file

`$schema`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Configuration](conf-properties-schema.md "undefined#/properties/$schema")

### $schema Type

`string`

### $schema Default Value

The default value is:

```json
"https://educorvi.de/cms-chatbot/conf.schema.yaml"
```

## open\_ai

Settings for the OpenAI API

`open_ai`

*   is required

*   Type: `object` ([OpenAI Settings](conf-properties-openai-settings.md))

*   cannot be null

*   defined in: [Configuration](conf-properties-openai-settings.md "undefined#/properties/open_ai")

### open\_ai Type

`object` ([OpenAI Settings](conf-properties-openai-settings.md))

## search

Settings for information retrieval

`search`

*   is required

*   Type: `object` ([Search Settings](conf-properties-search-settings.md))

*   cannot be null

*   defined in: [Configuration](conf-properties-search-settings.md "undefined#/properties/search")

### search Type

`object` ([Search Settings](conf-properties-search-settings.md))

any of

*   [Search configuration with Typesense](conf-properties-search-settings-anyof-search-configuration-with-typesense.md "check type definition")

*   [Search configuration with ElasticSearch](conf-properties-search-settings-anyof-search-configuration-with-elasticsearch.md "check type definition")

## websocket

Settings for the websocket server

`websocket`

*   is required

*   Type: `object` ([Websocket Settings](conf-properties-websocket-settings.md))

*   cannot be null

*   defined in: [Configuration](conf-properties-websocket-settings.md "undefined#/properties/websocket")

### websocket Type

`object` ([Websocket Settings](conf-properties-websocket-settings.md))

## deepl

Settings for the DeepL API

`deepl`

*   is optional

*   Type: `object` ([DeepL Settings](conf-properties-deepl-settings.md))

*   cannot be null

*   defined in: [Configuration](conf-properties-deepl-settings.md "undefined#/properties/deepl")

### deepl Type

`object` ([DeepL Settings](conf-properties-deepl-settings.md))

## source\_replace

Replaces parts of the source url that is returned to the client

`source_replace`

*   is optional

*   Type: `object` ([Source URL Replacement](conf-properties-source-url-replacement.md))

*   cannot be null

*   defined in: [Configuration](conf-properties-source-url-replacement.md "undefined#/properties/source_replace")

### source\_replace Type

`object` ([Source URL Replacement](conf-properties-source-url-replacement.md))
