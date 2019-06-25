<template>
  <div>
   
        <v-layout row wrap>
          <v-flex xs12>
            <v-card color="indigo lighten-1" class="white--text rounded-card">
              <v-layout>
                <v-flex xs8>
                  <v-img class="cover-image" :src="cover_image[0]" alt="Image"></v-img>
                </v-flex>
                <v-flex xs7 align-center>
                  <v-card-title primary-title>
                    <div>
                      <div class="headline">{{name}}</div>
                    </div>
                  </v-card-title>
                </v-flex>
              </v-layout>
              <v-divider light></v-divider>
              <v-card-actions class="pa-3">
                 Quantidade de Prêmios Conquistados
                <v-spacer></v-spacer>
                <v-icon v-for="award in Awards">star_border</v-icon>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
  </div>
</template>

<script>
export default {
  name: "GameCard",
  props: {
    cover_image: Array,
    name: String,
    Awards:Array,
    genre:Array
  }
};
</script>

<style>
.game-card {
  color: #282928;
  background: #e0e0e0;
}
.cover-image {
  max-height: 200px;
  background-size: 100%;
  background-position: center;
}

.rounded-card{
    border-radius:15px;
}
</style>
