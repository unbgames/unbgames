<template>
  <v-card>
    <v-card color="blue accent-1">
      <v-card-text>
        <span class="title white--text">Downloads</span>
        <div class="u-margin-top">
          <v-layout align-center justify-space-around row wrap>
            <v-flex xs1 md4 sm1>
              <p>
                <span class="mdi mdi-debian icon-holder"></span>
                <a class="link-app" :href="game.Debian[0]">
                  <strong>Debian</strong>
                </a>
              </p>

              <p>
                <span class="mdi mdi-linux icon-holder"></span>
                <a class="link-app" :href="game.RedHat[0]">
                  <strong>RedHat</strong>
                </a>
              </p>
            </v-flex>

            <v-flex xs1 md4 sm1>
              <p>
                <span class="mdi mdi-windows icon-holder"></span>
                <a class="link-app" :href="game.Windows[0]">
                  <strong>Windows</strong>
                </a>
              </p>

              <p>
                <span class="mdi mdi-apple icon-holder"></span>
                <a class="link-app" :href="game.Windows[0]">
                  <strong>Mac OS</strong>
                </a>
              </p>
            </v-flex>
          </v-layout>
        </div>
      </v-card-text>
    </v-card>
  </v-card>
</template>

<script>
export default {
  name: "AuthorsCard",
  props: {
    game: Object
  }
};
</script>

<style>
.u-margin-top {
  margin-top: 2vh;
}

.icon-holder {
  font-size: 20px;
}
</style>
