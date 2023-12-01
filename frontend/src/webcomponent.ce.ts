import {defineCustomElement} from 'vue';
import Chat from "@/components/Chat.vue";

const simple_websocket_chat = defineCustomElement(Chat);

customElements.define('cms-chatbot-webchat', simple_websocket_chat);
