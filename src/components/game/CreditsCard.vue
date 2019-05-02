<template>
  <v-container class="u-margin-bottom">
    <v-layout align-center justify-space-around row wrap>
      <v-flex xs1 md4 sm1>
        <v-card-text class="text-xs-center">
          <span class="font-weight-light title authors-names-list">Desenvolvedores</span>
          <p  v-for="developer in developers">{{developer}}</p>
        </v-card-text>
      </v-flex>

      <v-flex xs1 md4 sm1>
        <v-card-text class="text-xs-center">
          <span class="font-weight-light title authors-names-list">Artistas</span>
          <p v-for="artist in artists">{{artist}}</p>
        </v-card-text>
      </v-flex>

      <v-flex xs1 md4 sm1>
        <v-card-text class="text-xs-center">
          <span class="font-weight-light title authors-names-list">Musicos</span>
          <p v-for="musician in musicians">{{musician}}</p>
        </v-card-text>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<style scoped>
p {
  margin-top: 2vh;
}

.u-margin-bottom{
  margin-top: 3vh;
  margin-bottom: -7.5vh;
}
</style>

<script>
export default {
  name: "AuthorsCard",
  props: {
    developers: Array,
    artists: Array,
    musicians: Array
  }
};
</script>
