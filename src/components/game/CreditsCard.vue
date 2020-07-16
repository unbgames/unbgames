<template>
      <div> 
        <v-expansion-panel popout class="green accent-1">
        </v-expansion-panel>
        <tr/>
        <v-expansion-panel popout class="deep-purple lighten-3">
          <v-expansion-panel-content>
            <template v-slot:header>
              <div>Desenvolvedor</div>
            </template>
            <v-card>
              <v-divider light></v-divider>
              <v-card-text v-for="developer in developers">{{developer}}</v-card-text>
            </v-card>
          </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel popout class="blue lighten-3">
          <v-expansion-panel-content>
            <template v-slot:header>
              <div>Artistas</div>
            </template>
            <v-card>
              <v-divider light></v-divider>
              <v-card-text v-for="artist in artists">{{artist}}</v-card-text>
            </v-card>
          </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel popout class="orange lighten-3">
          <v-expansion-panel-content>
            <template v-slot:header>
              <div>Musicos</div>
            </template>
            <v-card>
              <v-divider light></v-divider>
              <v-card-text v-for="musician in musicians">{{musician}}</v-card-text>
            </v-card>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </div>
</template>

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

<style scoped>
p {
  margin-top: 2vh;
}

.u-margin-bottom {
  margin-top: 3vh;
  margin-bottom: -7.5vh;
}
</style>
