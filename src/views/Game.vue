<template>
  <v-container>
    <v-flex>
      <div>
        <h1>{{game.name}}</h1>
        <h2>{{game.semester}} / {{game.year}}</h2>
      </div>
    </v-flex>
    <v-layout row wrap>
      <v-flex d-flex xs12 sm12 md8 my-3>
        <carousel :images="game.items"/>
      </v-flex>
      <v-flex md3 :class="{'ma-0': $vuetify.breakpoint.smAndDown, 'ml-4': $vuetify.breakpoint.mdAndUp}">
        <v-flex my-3>
          <download-card :game="game"/>
        </v-flex>
        <game-card :game="game"/>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs12 md8 sm12 my-3>
        <description-card :game_description="game.description" :game_license="game.license" />
      </v-flex>
      <v-flex my-3 :class="{'ma-0': $vuetify.breakpoint.smAndDown, 'ml-4': $vuetify.breakpoint.mdAndUp}">
        <credits-card :credits="game.credits"/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import json from '@/../utils/db.json'
import GameCarousel from '@/components/GameCarousel.vue'
import DescriptionCard from '@/components/game/DescriptionCard.vue'
import CreditsCard from '@/components/game/CreditsCard.vue'
import DownloadCard from '@/components/game/DownloadCard.vue'
import GameCardDescription from '@/components/game/GameCardDescription.vue'

export default {
  name: 'game',
  components: {
    'carousel': GameCarousel,
    'description-card': DescriptionCard,
    'credits-card': CreditsCard,
    'game-card': GameCardDescription,
    'download-card': DownloadCard
  },
  data: function () {
    return {
      game: json.games[this.game_id]
    }
  },
  props: {
    game_id: Number
  }
}
// <!-- <carousel/> -->
//     <ul>
//       <li v-for="(value, key, index) in game" :key="value+index+key">
//         {{key}}: {{value}}
//         <img v-if="key=='cover_image'" :src="value" />
//       </li>
//     </ul>
</script>
