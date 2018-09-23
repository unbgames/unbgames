<template>
  <v-container>
    <v-layout row wrap>
      <v-flex xs12 my-3>
        <div>
          <h1>{{game.name}}</h1>
          <h2>{{game.semester}} / {{game.year}}</h2>
        </div>
      </v-flex>
      <v-flex xs8 mb-4>
        <carousel :images="game.items"/>
      </v-flex>
      <v-flex xs3 ml-3>
        <ul>
          <li v-for="(value, key, index) in game" :key="value+index+key">
            {{key}}: {{value}}
            <!-- <img v-if="key=='cover_image'" :src="value" /> -->
          </li>
        </ul>
      </v-flex>
      <v-flex fluid>
        <description-card :game_description="game.description" :game_license="game.license" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import json from '@/../utils/db.json'
import GameCarousel from '@/components/GameCarousel.vue'
import DescriptionCard from '@/components/game/DescriptionCard.vue'

export default {
  name: 'game',
  components: {
    'carousel': GameCarousel,
    'description-card': DescriptionCard,
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
