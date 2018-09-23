<template>
  <v-carousel>
    <v-carousel-item
      v-for="(item,i) in items"
      :key="i"
      :src="item.src"
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
  data () {
    return {
      items: [
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg'
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg'
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg'
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg'
        },
        {
          src: 'http://lorempixel.com/640/480'
        },
        {
        "src": "https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg",
        "name": "Huel",
        "is_gallery": false
      },
      {
        "src": "https://cdn.vuetifyjs.com/images/carousel/sky.jpg",
        "name": "Huelfdsa",
        "is_gallery": false
      },
      {
        "src": "https://cdn.vuetifyjs.com/images/carousel/sky.jpg",
        "name": "Huelfdsafd",
        "is_gallery": false
      },
      {
        "src": "https://cdn.vuetifyjs.com/images/carousel/sky.jpg",
        "name": "Huelfdsafdfds",
        "is_gallery": false
      },
      {
        "src": "https://cdn.vuetifyjs.com/images/carousel/sky.jpg",
        "name": "Huelfdsafdasdf",
        "is_gallery": false
      }
      ],
    }
  },
  props: {
    images: Array
  }
}
</script>