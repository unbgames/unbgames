<template>
    <v-parallax src="https://cdn.vuetifyjs.com/images/parallax/material.jpg">
    <v-container fill-height>
      <v-layout align-center>
        <v-flex text-xs-center>
          <h3 class="display-3">UnBGames</h3>
          <span class="subheading">
            Lorem ipsum dolor sit amet, pri veniam forensibus id.
            Vis maluisset molestiae id, ad semper lobortis cum.
            At impetus detraxit incorrupte usu, repudiare assueverit ex eum,
            ne nam essent vocent admodum.
          </span>
          <v-divider class="my-4"></v-divider>
          <v-btn class="mx-0" color="primary" large>
            Saiba mais!
          </v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </v-parallax>
</template>

<script>
export default {
  name: "HeroComponent"
};
</script>