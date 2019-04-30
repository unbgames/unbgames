<template>
  <div>
    <menu-app/>
    <v-container>
      <v-flex>
        <div>
          <h1 class="font-weight-thin display-1">{{game.name}}</h1>
        </div>
      </v-flex>
      <v-layout row wrap>
        <v-flex d-flex xs12 sm12 md8 my-3>
          <carousel :images="game.images"/>
        </v-flex>
        <v-flex
          md3
          :class="{'ma-0': $vuetify.breakpoint.smAndDown, 'ml-4': $vuetify.breakpoint.mdAndUp}"
        >
          <v-flex my-3>
            <download-card :game="game"/>
          </v-flex>
          <game-card :game="game"/>
        </v-flex>
      </v-layout>
      <v-layout row wrap>
        <v-flex xs12 md8 sm12 my-3>
          <description-card
            :game_description="game.description"
            :game_license="game.license"
            :genres="game.genres"
          />
        </v-flex>
        <v-flex
          my-3
          md3
          :class="{'ma-0': $vuetify.breakpoint.smAndDown, 'ml-4': $vuetify.breakpoint.mdAndUp}"
        >
          <credits-card :credits="game.credits"/>
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
import GameCardDescription from "@/components/game/GameCardDescription.vue";
import HeaderMenu from "@/components/HeaderMenu.vue";

export default {
  name: "game",
  components: {
    carousel: GameCarousel,
    "description-card": DescriptionCard,
    "credits-card": CreditsCard,
    "game-card": GameCardDescription,
    "download-card": DownloadCard,
    "menu-app": HeaderMenu
  },
  props: {
    game_id: Number
  },
  computed: {
    game: function() {
      let size = json.games.length;
      for (var i = 0; i <= size; i++) {
        var game = json.games[i].game;
        if (game.id == this.game_id) {
          return game;
        }
      }
    }
  }
};
</script>
