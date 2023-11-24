import { VueQueryPlugin } from "@tanstack/vue-query";
import { createHead } from "@unhead/vue";
import { createApp } from "vue";
import App from "./App.vue";
import { router } from "./routes";
import "./style.css";

const app = createApp(App);
const head = createHead();
app.use(router).use(head).use(VueQueryPlugin).mount("#app");
