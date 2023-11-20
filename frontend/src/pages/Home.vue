<script setup lang="ts">
import { Container } from "@/components/ui/container";
import { Button } from "@/components/ui/button";
import { useMutation } from "@tanstack/vue-query";
import { useRouter } from "vue-router";

const router = useRouter();

const startOrderMutation = useMutation({
  mutationFn: () => {
    return Promise.resolve({ id: 1 });
  },
  onSuccess: (data) => {
    router.push(`/order/${data.id}`);
  },
});

function startOrder() {
  startOrderMutation.mutate();
}
</script>

<template>
  <Container>
    <h1 class="text-5xl text-center font-medium">Order Sushi</h1>
    <div class="flex justify-center">
      <Button size="lg" @click="startOrder">Start Ordering</Button>
    </div>
  </Container>
</template>
