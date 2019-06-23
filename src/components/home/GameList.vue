<template>
  <v-container>
    <h1 class="display-2 font-weight-light year-title text-xs-left">Todos os Jogos</h1>
    <v-layout align-center justify-space-around row wrap>
      <v-flex md4 v-for="(game,i) in games" :key="`${i}`" ma-5>
        <router-link :to="{name: 'game', params: {game_id: game.jogo.ID, game_json: game}}">
          <game-card :name="game.jogo.Name" :cover_image="game.jogo.Gallery.CoverImage"/>
        </router-link>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import json from "@/../utils/db.json";
import CardCarousel from "@/components/home/CardCarousel.vue";
import GameCard from "@/components/home/GameCard.vue";

export default {
  name: "GameList",
  data: function() {
    return {
      games: json.jogos
    };
  },
  components: {
    "card-carrousel": CardCarousel,
    "game-card": GameCard
  }
};
</script>

<style scoped>
h1 {
  margin: 5vh 2.5vw;
}
</style>
