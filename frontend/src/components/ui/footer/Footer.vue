<script setup lang="ts">
import { cn } from "@/lib/utils";

interface Props {
  float?: boolean;
}

const year = new Date().getFullYear();

withDefaults(defineProps<Props>(), { float: false });
</script>

<template>
  <footer
    :class="
      cn('flex justify-center items-center px-2.5 h-10 w-full', {
        'fixed bottom-0': float,
      })
    "
  >
    <p>©{{ year }} Order Sushi. All rights reserved</p>
  </footer>
</template>
