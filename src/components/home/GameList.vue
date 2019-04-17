<template>
  <div>
    <v-container grid-list-xl text-xs-center>
      <v-layout row wrap>
        <v-flex xs10 offset-xs1>
          <v-tabs v-model="active" color="black" dark slider-color="yellow">
            <v-tab v-for="n in 5" :key="n" ripple> {{year-n}}</v-tab>
            <v-tab-item v-for="n in 5" :key="n">
              <v-card flat>
                <v-card-text>{{ text }}</v-card-text>
              </v-card>
            </v-tab-item>
          </v-tabs>
          <div class="text-xs-center mt-3">
            <v-btn @click="next">next tab</v-btn>
          </div>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        active: null,
        year:2019,
        text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
      }
    },
    methods: {
      next () {
        const active = parseInt(this.active)
        this.active = (active < 2 ? active + 1 : 0)
      }
    }
  }
</script>

<style>
.card-carousel {
  text-decoration: none;
}
.year-title {
  margin: 15px 0 10px 0;
}
</style>
