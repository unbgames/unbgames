<template>
  <div>
    <v-flex v-for="(game,i) in games" :key="`2${i}`" mx-5>
      <h1 class="title">{{game.year}}</h1>
      <card-carrousel :index_array_year="i" :games="game.games" />    
    </v-flex>
  </div>
</template>

<script>
import json from '@/../utils/db_new.json'
import CardCarousel from '@/components/home/CardCarousel.vue'

export default {
  name: 'GameList',
  data: function () {
    return {
      games: json,
    }
  },
  components: {
    "card-carrousel": CardCarousel
  }
}
</script>
