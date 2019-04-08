<template>
  <v-carousel>
    <v-carousel-item v-for="(item,i) in images" :key="i" :src="item.src"></v-carousel-item>
  </v-carousel>
</template>

<script>
import GameCarousel from "@/components/GameCarousel.vue";

export default {
  name: "game",
  components: {
    "game-carousel": GameCarousel
  },
  props: {
    images: Array
  }
};
</script>