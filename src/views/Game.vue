<template>
  <div class="game">
    Este é o game
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

export default {
  name: 'game',
  components: {},
  data: function () {
    return {
      game: json.games[this.gameId]
    }
  },
  props: {
    gameId: Number
  }
}
</script>
