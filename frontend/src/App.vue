<script setup lang="ts">
import { Container } from "@/components/ui/container";
</script>

<template>
  <Container>
    <h1 class="text-5xl font-semibold text-center text-primary">Order Sushi</h1>
  </Container>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
