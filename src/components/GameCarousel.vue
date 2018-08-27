<template>
    <v-carousel>
        <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        :src="item.src"
        reverse-transition="fade"
        transition="fade"
        ></v-carousel-item>
    </v-carousel>  
</template>

<script>
import GameCarousel from '@/components/GameCarousel.vue'


export default {
  name: 'game',
  components: {
    'game-carousel': GameCarousel
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
</script>