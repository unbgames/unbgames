<template>
  <v-parallax class="header-image">
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
          <v-btn class="mx-0" outline color="white" large>Saiba mais!</v-btn>
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

<style lang="scss" scoped>
.header-image {
  background-image: linear-gradient(
      to right bottom,
      rgba(#4caf50, 1),
      rgba(#1f4037, 1)
    )
}
</style>

