<template>
  <swiper :options="swiper_option">
    <swiper-slide v-for="game in games" :key="game.ID + game.Name">
      <router-link
        class="card-carousel"
        :to="{name: 'game', params: {game_id: game.ID, game_json: game}}"
      >
        <game-card :name="game.Name" :cover_image="game.Gallery.CoverImage[0]"/>
      </router-link>
    </swiper-slide>
    <div class="swiper-button-prev" slot="button-prev"></div>
    <div class="swiper-button-next" slot="button-next"></div>
  </swiper>
</template>

<script>
import "swiper/dist/css/swiper.css";
import { swiper, swiperSlide } from "vue-awesome-swiper";
import GameCard from "@/components/home/GameCard.vue";

export default {
  components: {
    swiper: swiper,
    "swiper-slide": swiperSlide,
    "game-card": GameCard
  },
  data() {
    return {
      swiper_option: {
        slidesPerView: 4,
        spaceBetween: 25,
        slidesPerGroup: 4,
        loop: true,
        loopFillGroupWithBlank: false,
        pagination: {
          el: ".swiper-pagination",
          clickable: true
        },
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev"
        },
        breakpoints: {
          1024: {
            slidesPerView: 4,
            spaceBetween: 40
          },
          960: {
            slidesPerView: 2,
            spaceBetween: 30
          },
          600: {
            slidesPerView: 1,
            spaceBetween: 20
          }
        }
      }
    };
  },
  props: {
    games: Object
  }
};
</script>