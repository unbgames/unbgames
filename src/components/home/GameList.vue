<template>
  <div>
    <v-flex v-for="(game,i) in games" :key="`${i}`" ma-5>
      <h1 class="display-2 font-weight-light year-title">Jogos de {{game.game.Year}}</h1>
      <card-carrousel class="card-carousel" :index_array_year="i" :games="game"/>
    </v-flex>
  </div>
</template>

<script>
import json from "@/../utils/db.json";
import CardCarousel from "@/components/home/CardCarousel.vue";

export default {
  name: "GameList",
  data: function() {
    return {
      games: json.games
    };
  },
  components: {
    "card-carrousel": CardCarousel
  }
};
</script>

<style>
.card-carousel {
  text-decoration: none;
}
.year-title {
  margin: 15px 0 10px 0;
}
</style>
