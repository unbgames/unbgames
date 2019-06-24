<template>
  <v-footer dark height="auto">
    <v-layout align-center justify-center column fill-height>
      <v-flex lg12 md12>
        <v-card-text class="white--text justify-center u-margin-top">
          <h4>Acervo central de jogos feitos na Universidade de Brasilia e em seus campi</h4>
        </v-card-text>
      </v-flex>

      <v-flex lg12 md12>
        <v-card-text class="px-0">Universidade de Brasília</v-card-text>
      </v-flex>

      <v-flex md12>
        <v-card-text>
          <a href="https://github.com/unbgames/unbgames/issues">
            <img
              src="https://img.shields.io/github/issues-closed/unbgames/unbgames.svg?style=popout&colorA=212121&logo=github&colorB=4caf50&logoColor=F7F7F7&logoWidth=15"
            >
          </a>
        </v-card-text>
      </v-flex>

      <v-flex xs12>
        <p>Copyright © 2018 UnB Games</p>
      </v-flex>
    </v-layout>
  </v-footer>
</template>

<script>
export default {
  name: "Footer"
};
</script>

<style scoped>
.u-margin-top {
  margin-top: 2vh;
}
</style>

