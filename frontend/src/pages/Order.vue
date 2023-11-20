<script setup lang="ts">
import { Container } from "@/components/ui/container";
import { Separator } from "@/components/ui/separator";
</script>

<template>
  <Container>
    <h1 class="text-5xl text-center font-medium">
      Order #{{ $route.params.id }}
    </h1>
    <Separator class="my-4 bg-zinc-200" />
  </Container>
</template>
