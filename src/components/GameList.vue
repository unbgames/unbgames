<template>
  <div>
    <hero-app />
    <ul>
      <li v-for="game in games" :key="game.id + game.name">
        <router-link :to="{name: 'game', params: {gameId: game.id, gameJson: game}}">{{game.name}} - {{game.id}}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import json from '../../utils/db.json'
import HeroComponentVue from './HeroComponent.vue';

export default {
  name: 'GameList',
  data: function () {
    return {
      games: json.games
    }
  },
  components: {
    "hero-app": HeroComponentVue
  }
}
</script>
