<template>
  <v-card color="deep-purple accent-1">
    <v-layout row wrap>
          <v-flex xs12>
            <v-card color="deep-purple accent-1" class="white--text">
              <v-layout row>
                <v-flex xs12>
                  <v-card-title primary-title>
                    <div>
                      <div class="headline">Informações do Jogo</div>
                      <br>
                      <div><strong>Versão do jogo</strong>: {{game.Version}}</div>
                      <br>
                      <div><i class="fas fa-calendar-check"></i><strong> -Ano de lançamento:</strong> {{game.Year}}</div>
                      <br>
                      <div><strong><i class="fab fa-github"></i> -Repositório Oficial:</strong></div>
                      <a class="link-app" :href="game.Repository">{{game.Name}}</a>
                      <br><br>
                      <div v-if="game.Awards.length!=0">
                      <div color="grey lighten-2">
                        <p>
                          <i class="fas fa-trophy"></i>
                          <strong> -Prêmios conquistados:</strong>
                          <br>
                        </p>
                        <span v-for="(award,i) in game.Awards" :key="i">
                          <p class="award-text">{{award}}</p>
                        </span>
                      </div>
  </div>    
  
                    </div>
                  </v-card-title>
                </v-flex>
               
              </v-layout>
              <v-divider light></v-divider>
            </v-card>
          </v-flex>
        </v-layout>

  </v-card>
</template>

<script>


export default {
  name: "GameInformation",
  props: {
    game: Object
  },
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
