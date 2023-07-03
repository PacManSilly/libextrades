import { createApp, markRaw } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
import axios from "axios";
import "./assets/index.css";

// axios settings
axios.defaults.baseURL = "http://192.168.1.104:8000/";
// axios.defaults.baseURL = "http://localhost:8000/";
// axios.defaults.baseURL = "https://libextrades.com/";
axios.defaults.headers.post["Content-Type"] = "application/json";
axios.defaults.withCredentials = true;
axios.defaults.timeout = 9000;

const pinia = createPinia();
pinia.use(({ store }) => {
  store.$router = markRaw(router);
});

const app = createApp(App);

app.use(pinia);
app.use(router);

app.mount("#app");
