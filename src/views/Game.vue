<template>
  <div class="game">
    Este é o game
    <ul>
      <li v-for="(value, key, index) in game" :key="value+index">
        {{key}}: {{value}}
      </li>
    </ul>
  </div>
</template>

<script>

import axios from "axios";

export default {
  name: "game",
  components: {},
  data: function() {
    return {
      game: {}
    };
  },
  props: {
    gameId: Number,
  },
  mounted() {
    var url = "http://localhost:3000/games/" + this.gameId;
    axios
      .get(url)
      .then(response => {
        this.game = response.data;
        console.log(this.game);
      })
      .catch(function(error) {
        console.log(error);
      });
  }
};
</script>
