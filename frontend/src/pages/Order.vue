<script setup lang="ts">
import { Button } from "@/components/ui/button";
import { Container } from "@/components/ui/container";
import { Separator } from "@/components/ui/separator";
import { useHead } from "@unhead/vue";
import { useRoute } from "vue-router";

const route = useRoute();

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
  </Container>
</template>
