<script setup lang="ts">
import logo from "@/assets/order-sushi.png";
import { Button } from "@/components/ui/button";
import { Container } from "@/components/ui/container";
import { Footer } from "@/components/ui/footer";
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
    <div class="flex flex-col items-center gap-6">
      <h1 class="text-5xl text-center font-medium">Order Sushi</h1>
      <img :src="logo" class="rounded-full w-[200px] h-[200px] object-cover" />
      <Button size="lg" @click="startOrder">Start Ordering</Button>
    </div>
  </Container>
  <Footer float />
</template>
