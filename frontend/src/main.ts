import { VueQueryPlugin } from "@tanstack/vue-query";
import { createApp } from "vue";
import App from "./App.vue";
import { router } from "./routes";
import "./style.css";

const app = createApp(App);
app.use(router).use(VueQueryPlugin).mount("#app");
