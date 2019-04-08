<template>
  <v-card color="grey lighten-2">
    <v-card-text>
      <p>
        <strong>Versão do jogo:</strong>
        {{game.version}}
      </p>
      <p>
        <strong>Ano de lançamento:</strong>
        {{game.year}}
      </p>
      <p>
        <strong>Repositório Oficial:</strong>
        <br>
        <a class="link-app" :href="game.repository">{{game.name}}</a>
      </p>
      <awards-card :awards="game.awards"></awards-card>
    </v-card-text>
  </v-card>
</template>

<script>
import AwardsCard from "./AwardsCard.vue";

export default {
  name: "GameCardDescription",
  props: {
    game: Object
  },
  components: {
    "awards-card": AwardsCard
  }
};
</script>        
<style>
.data-content {
  margin: 5px 0;
  vertical-align: baseline;
}
.icon-content {
  padding: 2px;
}
</style>
