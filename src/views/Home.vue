<template>
  <div class="home">
    <hero-component/>
    <game-list/>
  </div>
</template>

<script>
import GameList from "@/components/home/GameList.vue";
import HeroComponent from "@/components/home/HeroComponent.vue";

export default {
  name: "home",
  components: {
    "game-list": GameList,
    "hero-component": HeroComponent
  }
};
</script>
