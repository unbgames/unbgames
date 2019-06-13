<template>
  <v-card color="grey lighten-2">
    <v-card-text>
      <span class="title font-weight-light">Informações do Jogo</span>
      <div class="u-margin-top">
      <p>
        <strong>Versão do jogo:</strong>
        {{game.Version}}
      </p>
      <p>
        <strong>Ano de lançamento:</strong>
        {{game.Year}}
      </p>
      <p>
        <strong>Repositório Oficial:</strong>
        <br>
        <a class="link-app" :href="game.Repository">{{game.Name}}</a>
      </p>
      <awards-card :awards="game.Awards"></awards-card>
      </div>
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

.u-margin-top {
  margin-top: 2vh;
}
</style>
