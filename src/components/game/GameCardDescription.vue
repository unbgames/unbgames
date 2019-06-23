<template>
  <v-card color="grey lighten-2">
    <v-layout row wrap>
          <v-flex xs12>
            <v-card color="purple" class="white--text">
              <v-layout row>
                <v-flex xs7>
                  <v-card-title primary-title>
                    <div>
                      <div class="headline">Informações do Jogo</div>
                      <div class=""><strong>Versão do jogo</strong>: {{game.Version}}</div>
                      <br>
                      <div><i class="fas fa-calendar-check"></i><strong> -Ano de lançamento:</strong> {{game.Year}}</div>
                      <br>
                      <div><strong><i class="fab fa-github"></i> -Repositório Oficial:</strong></div>
                      <a class="link-app" :href="game.Repository">{{game.Name}}</a>
                      <br><br>
                      <awards-card :awards="game.Awards"></awards-card>                    
  
                    </div>
                  </v-card-title>
                </v-flex>
                <v-flex xs5>
                  <v-img
                    src="https://cdn.vuetifyjs.com/images/cards/halcyon.png"
                    height="125px"
                    contain
                  ></v-img>
                </v-flex>
              </v-layout>
              <v-divider light></v-divider>
              <v-card-actions class="pa-3">
                Rate this album
                <v-spacer></v-spacer>
                <v-icon>star_border</v-icon>
                <v-icon>star_border</v-icon>
                <v-icon>star_border</v-icon>
                <v-icon>star_border</v-icon>
                <v-icon>star_border</v-icon>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>

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
