# gpt-frontend

A simple frontend that displays a basic chat ui and connects to gpt-poc-backend via a websocket.

Can be included as a webcomponent:

```html
<cms-chatbot-webchat websocket_url="ws://your-websocket-url"></cms-chatbot-webchat>
...

<script src="cms-chatbot-webchat.js"></script>

```

Build the js file by running:
```shell
yarn run build-webcomponent
```
The js file can be found in the folder `webcomponent_dist`.