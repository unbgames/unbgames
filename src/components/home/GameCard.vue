<template>
  <v-card class="game-card">
    <v-card-media>
      <img class="cover-image" :src="cover_image" alt="cover_image">
    </v-card-media>
    <v-card-title primary-title>
      <h4 class="title card-text text-truncate">{{name}}</h4>
    </v-card-title>
  </v-card>
</template>

<script>
export default {
  name: "GameCard",
  props: {
    cover_image: String,
    name: String
  }
};
</script>

<style>
.game-card {
  color: #282928;
  background: #e0e0e0;
}
.cover-image {
  max-height: 200px;
  background-size: 100%;
  background-position: center;
}
</style>
