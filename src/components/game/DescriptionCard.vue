<template>
       <v-expansion-panel>
    <v-expansion-panel-content class="indigo lighten-2 white--text" >
      <template v-slot:header>
        <div class="text-sm-center headline">Descrição</div>
        
      </template>
      <v-card>
        <v-card-text>{{game_description}}</v-card-text>
      </v-card>
    </v-expansion-panel-content>
  </v-expansion-panel>

</template>
<style>
.description-text {
  margin-top: 10px;
}
.genres-card {
  padding: 5px 15px;
}
</style>

<script>
export default {
  name: "DescriptionCard",
  props: {
    game_description: String,
    game_license: Object,
    genres: Array
  }
};
</script>

<style>
.description-text {
  margin-top: 10px;
}
.genres-card {
  padding: 5px 15px;
}
</style>
