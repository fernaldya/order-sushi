<script setup lang="ts">
import { Container } from "@/components/ui/container";
</script>

<template>
  <Container>
    <div class="flex justify-center gap-1 my-2">
      <div class="p-2 text-xs h-20 w-20 bg-zinc-50 shadow">bg-zinc-50</div>
      <div class="p-2 text-xs h-20 w-20 bg-zinc-100 shadow">bg-zinc-100</div>
      <div class="p-2 text-xs h-20 w-20 bg-zinc-200 shadow">bg-zinc-200</div>
      <div class="p-2 text-xs h-20 w-20 bg-zinc-300 shadow">bg-zinc-300</div>
      <div class="p-2 text-xs h-20 w-20 bg-zinc-400 shadow">bg-zinc-400</div>
      <div class="p-2 text-xs h-20 w-20 bg-zinc-500 shadow">bg-zinc-500</div>
      <div
        class="p-2 text-xs h-20 w-20 bg-zinc-600 text-primary-foreground shadow"
      >
        bg-zinc-600
      </div>
      <div
        class="p-2 text-xs h-20 w-20 bg-zinc-700 text-primary-foreground shadow"
      >
        bg-zinc-700
      </div>
      <div
        class="p-2 text-xs h-20 w-20 bg-zinc-800 text-primary-foreground shadow"
      >
        bg-zinc-800
      </div>
    </div>
  </Container>
</template>
