<template>
  <div class="game">
    <carousel/>
    <ul>
      <li v-for="(value, key, index) in game" :key="value+index+key">
        {{key}}: {{value}}
        <img v-if="key=='cover_image'" :src="value" />
      </li>
    </ul>
  </div>
</template>

<script>
import json from '@/../utils/db.json'
import GameCarousel from '@/components/GameCarousel.vue'

export default {
  name: 'game',
  components: {
    'carousel': GameCarousel
  },
  data: function () {
    return {
      game: json.games[this.game_id]
    }
  },
  props: {
    game_id: Number
  }
}
</script>
