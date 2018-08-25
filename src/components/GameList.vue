<template>
  <div>
    <hero-app />
    <h1>{{year_title}}</h1>
    <card-carrousel :games="games" />
    <!-- <ul>
      <li v-for="game in games" :key="game.id + game.name">
        <router-link :to="{name: 'game', params: {game_id: game.id, game_json: game}}">{{game.name}} - {{game.id}}</router-link>
      </li>
    </ul> -->
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
