<template>
  <div>
    <v-container>
      <v-flex>
        <div>
          <h1 class="font-weight-bold display-1 game-title">{{game.Name}}</h1>
        </div>
      </v-flex>

      <v-layout row wrap>
        <v-flex d-flex xs12 sm12 md12 my-12>
          <carousel :images="game"/>
        </v-flex>
      </v-layout>
    </v-container>

    <v-container>
      <v-layout row wrap>
        <v-flex xs6 lg6 md12 sm12 my-3>
            <v-flex xs12 lg12 mb-3>
              <description-card
                :game_description="game.Description"
                :game_license="game.license"
                :genres="game.Genre"
              />
            <v-flex xs12 lg12 mb-3 my-3>
                        <game-card :game="game"/>
            </v-flex>
            </v-flex>
        </v-flex>
        <v-flex xs6 md12 lg6 sm12 my-3>
            <v-flex xs12 lg12 mb-3 ml-2>
              <credits-card ml-3
                :developers="game.Developers"
                :artists="game.Designers"
                :musicians="game.Musicians"/>
            </v-flex>
            <v-flex xs12 lg12 ml-3>
              <download-card :game="game.Downloads"/>
            </v-flex>
        </v-flex>
      </v-layout>
    </v-container>

    <v-container>
      <v-layout  justify-space-around row wrap>
        <v-flex
          xs12
          md5
          sm5
          my-3
          :class="{'ma-0': $vuetify.breakpoint.smAndDown, 'ml-0': $vuetify.breakpoint.mdAndUp}"
        >
        </v-flex>

        <v-flex xs12 md5 sm5 my-3>

        </v-flex>
        
      </v-layout>
    </v-container>
    
  </div>
</template>

<script>
import json from "@/../utils/db.json";
import GameCarousel from "@/components/GameCarousel.vue";
import DescriptionCard from "@/components/game/DescriptionCard.vue";
import CreditsCard from "@/components/game/CreditsCard.vue";
import DownloadCard from "@/components/game/DownloadCard.vue";
import GameInformation from "@/components/game/GameInformation.vue";

export default {
  name: "game",
  components: {
    "carousel": GameCarousel,
    "description-card": DescriptionCard,
    "credits-card": CreditsCard,
    "game-card": GameInformation,
    "download-card": DownloadCard
  },
  props: {
    game_id: Number
  },
  computed: {
    game: function() {
      let size = json.jogos.length;
      for (let i = 0; i <= size; i++) {
        let jogo = json.jogos[i].jogo;
        if (jogo.ID === this.game_id) {
          return jogo;
        }
      }
    }
  }
};
</script>

<style scoped>

.game-title {
  padding: 3.5vh 0;
}

</style>

