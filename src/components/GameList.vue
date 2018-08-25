<template>
  <div>
    <hero-app />
    <v-flex v-for="i in 3" :key="`2${i}`" mx-5>
      <h1>{{year_title}}</h1>
      <card-carrousel :games="games" />    
    </v-flex>
  </div>
</template>

<script>
import json from '../../utils/db.json'
import HeroComponentVue from './HeroComponent.vue';
import CardCarousel from '@/components/CardCarousel.vue'

export default {
  name: 'GameList',
  data: function () {
    return {
      games: json.games,
      year_title: '1/2018'
    }
  },
  components: {
    "hero-app": HeroComponentVue,
    "card-carrousel": CardCarousel
  }
}
</script>
