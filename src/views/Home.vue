<template>
  <div class="home">
    <hero-app/>
    <game-list/>
  </div>
</template>

<script>
import GameList from "@/components/home/GameList.vue";
import HeroComponentVue from "@/components/home/HeroComponent.vue";

export default {
  name: "home",
  components: {
    "game-list": GameList,
    "hero-app": HeroComponentVue
  }
};
</script>
