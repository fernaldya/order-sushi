<script setup lang="ts">
import { Button } from "@/components/ui/button";
import { Container } from "@/components/ui/container";
import { Separator } from "@/components/ui/separator";
import { useHead } from "@unhead/vue";
import { useRoute } from "vue-router";
import groupBy from "lodash.groupby";

const route = useRoute();
const orders = [
  {
    id: 1,
    creator: "Anonymous Koala",
    quantity: 1,
    sessionId: parseInt(route.params.id as string, 10),
    mealId: 1,
    meal: {
      id: 1,
      name: "Salmon Aburi Sushi",
      price: 25000,
    },
  },
];
const groupedOrders = groupBy(orders, "creator");

useHead({
  title: `Order #${route.params.id} | Order Sushi`,
});

const share = async () => {
  await navigator.clipboard.writeText(window.location.href);
};
</script>

<template>
  <Container>
    <div class="flex justify-between mb-6">
      <Button variant="outline" @click="share">Share</Button>
      <Button>Finalize</Button>
    </div>

    <h1 class="text-5xl text-center font-medium">
      Order #{{ $route.params.id }}
    </h1>
    <Separator class="my-4 bg-zinc-200" />
    <section>
      <div v-for="(order, i) in orders">
        <p class="font-medium mb-2" v-if="i === 0">by {{ order.creator }}</p>
        <p>{{ order.quantity }}x {{ order.meal.name }}</p>
      </div>
    </section>
  </Container>
</template>
