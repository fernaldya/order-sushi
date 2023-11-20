import HomePage from "@/pages/Home.vue";
import ComponentsPage from "@/pages/Components.vue";
import OrderPage from "@/pages/Order.vue";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: HomePage,
  },
  {
    path: "/components",
    component: ComponentsPage,
  },
  {
    path: "/order/:id",
    component: OrderPage,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export { router };
