<template>
    <div id="particles-js">
      <div class="test">  
          <v-layout align-center>
            <v-flex text-xs-center>
              <h3 class="display-3 white--text">UnBGames</h3>
              <span class="subheading white--text">
                Lorem ipsum dolor sit amet, pri veniam forensibus id.
                Vis maluisset molestiae id, ad semper lobortis cum.
                At impetus detraxit incorrupte usu, repudiare assueverit ex eum,
                ne nam essent vocent admodum.
              </span>
              <v-divider class="my-4"></v-divider>
              <v-btn class="mx-0" color="green lighten-1" large>
                Saiba mais!
              </v-btn>
            </v-flex>
          </v-layout>
      </div>
      <vue-particles
        color="#dedede"
        :particleOpacity="0.7"
        :particlesNumber="80"
        shapeType="circle"
        :particleSize="4"
        linesColor="#dedede"
        :linesWidth="1"
        :lineLinked="true"
        :lineOpacity="0.4"
        :linesDistance="150"
        :moveSpeed="3"
        :hoverEffect="true"
        hoverMode="grab"
        :clickEffect="true"
        clickMode="push"
      ></vue-particles>
  </div>
</template>

<script>
export default {
  name: "HeroComponent"
};
</script>

<style>
#particles-js {
  background-image: url("https://github.com/unbgames/Wenova/raw/master/res/readme/menu1.png");
  max-height: 33em;
}
@media only screen and (min-width: 600px)  {    
  .test{
    position: absolute;
    z-index: 999;
    margin: 100px;
  }
}
</style>
