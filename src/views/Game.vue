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
        <v-flex d-flex xs12 sm12 md12 my-12>
          <carousel :images="game.images"/>
        </v-flex>
      </v-layout>
    </v-container>
    <v-container>
      <v-layout row wrap>
        <v-flex xs12 md12 sm12 my-3>
          <description-card
            :game_description="game.description"
            :game_license="game.license"
            :genres="game.genres"
          />

          <credits-card :credits="game.credits"/>
        </v-flex>
      </v-layout>
    </v-container>
    <v-container>
      <v-layout align-center justify-space-around row wrap>
        <v-flex
          xs12
          md5
          sm5
          my-3
          :class="{'ma-0': $vuetify.breakpoint.smAndDown, 'ml-0': $vuetify.breakpoint.mdAndUp}"
        >
          <game-card :game="game"/>
        </v-flex>
        <v-flex xs12 md5 sm5 my-3>
          <download-card :game="game"/>
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
      for (var i = 0, size = json.length; i < size; i++) {
        var game = json[i].games.find(game => game.id === this.game_id);
        if (game != undefined) break;
      }
      return game;
    }
  }
};
</script>
