<template>
  <div>
      <!-- swiper -->
      <swiper :options="swiper_option">
        <swiper-slide v-for="game in games" :key="game.id + game.name">
          <router-link :to="{name: 'game', params: {game_id: game.id, game_json: game}}">
            <card-game :name="game.name" :cover_image="game.cover_image" />
          </router-link>
        </swiper-slide>
        <div class="swiper-pagination" slot="pagination"></div>
        <div class="swiper-button-prev" slot="button-prev"></div>
        <div class="swiper-button-next" slot="button-next"></div>
      </swiper>
  </div>
</template>

<script>
// require styles
import "swiper/dist/css/swiper.css";
import { swiper, swiperSlide } from "vue-awesome-swiper";
import CardGame from "@/components/CardGame.vue";

export default {
  components: {
    swiper,
    swiperSlide,
    "card-game": CardGame
  },
  data() {
    return {
      swiper_option: {
        slidesPerView: 4,
        spaceBetween: 25,
        slidesPerGroup: 4,
        loop: true,
        loopFillGroupWithBlank: true,
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        },
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev'
        }
      }
    }
  },
  props: {
    games: Object
  }
};
</script>