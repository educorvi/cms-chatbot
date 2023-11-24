## open\_ai Type

`object` ([OpenAI Settings](conf-properties-openai-settings.md))

# open\_ai Properties

| Property                           | Type      | Required | Nullable       | Defined by                                                                                                                              |
| :--------------------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| [api\_key](#api_key)               | `string`  | Required | cannot be null | [Configuration](conf-properties-openai-settings-properties-api_key.md "undefined#/properties/open_ai/properties/api_key")               |
| [model](#model)                    | `string`  | Required | cannot be null | [Configuration](conf-properties-openai-settings-properties-model.md "undefined#/properties/open_ai/properties/model")                   |
| [spending\_limit](#spending_limit) | `integer` | Optional | cannot be null | [Configuration](conf-properties-openai-settings-properties-spending_limit.md "undefined#/properties/open_ai/properties/spending_limit") |

## api\_key

OpenAI API Key

`api_key`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Configuration](conf-properties-openai-settings-properties-api_key.md "undefined#/properties/open_ai/properties/api_key")

### api\_key Type

`string`

## model

OpenAI model to use (see <https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo> and <https://platform.openai.com/docs/models/gpt-3-5>)

`model`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Configuration](conf-properties-openai-settings-properties-model.md "undefined#/properties/open_ai/properties/model")

### model Type

`string`

### model Examples

```yaml
gpt-3.5-turbo-16k

```

```yaml
gpt-4-1106-preview

```

## spending\_limit

Monthly spend limit in dollars

`spending_limit`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Configuration](conf-properties-openai-settings-properties-spending_limit.md "undefined#/properties/open_ai/properties/spending_limit")

### spending\_limit Type

`integer`

### spending\_limit Default Value

The default value is:

```json
50
```
