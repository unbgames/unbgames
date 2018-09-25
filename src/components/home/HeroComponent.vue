<template>
    <div id="particles-js">
      <div class="test">  
          <v-layout>
            <v-flex text-xs-center>
              <h3 class="display-3 white--text">UnBGames</h3>
              <span class="subheading white--text">
                Lorem ipsum dolor sit amet, pri veniam forensibus id.
                Vis maluisset molestiae id, ad semper lobortis cum.
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
body, html {
    height: 100%;
}

#particles-js { 
    /* The image used */
    background-image: url("https://github.com/unbgames/Wenova/raw/master/res/readme/menu1.png");

    /* Full height */
    height: 100%; 
    max-height: auto;

    /* Center and scale the image nicely */
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}
.test {
  position: relative;
  z-index: 999;
  padding-top: 50px;
}
@media only screen and (min-width: 600px) {
  #particles-js { 
    /* The image used */
    background-image: url("https://github.com/unbgames/Wenova/raw/master/res/readme/menu1.png");

    /* Full height */
    height: 50%; 
    max-height: 500px;

    /* Center and scale the image nicely */
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}
  .test {
    position: absolute;
    z-index: 999;
    margin: 3% 40%;
  }
}
</style>
