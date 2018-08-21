<template>
  <div>
    <ul>
      <li v-for="game in games" :key="game.id + game.name">
        <router-link :to="{name: 'game', params: {gameId: game.id, gameJson: game}}">{{game.name}} - {{game.id}}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import json from "../../utils/db.json"
// import axios from "axios";

export default {
  name: "GameList",
  data: function() {
    return {
      games: json.games
    };
  },
  // mounted() {
  //   var url = "http://localhost:3000/games";
  //   axios
  //     .get(url)
  //     .then(response => {
  //       this.games = response.data;
  //       console.log(this.games)
  //     })
  //     .catch(function(error) {
  //       console.log(error);
  //     });
  // }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
</style>
