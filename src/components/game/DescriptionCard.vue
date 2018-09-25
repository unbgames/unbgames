<template>
    <v-card color="grey lighten-2">
        <v-card-text>
            <span class="font-weight-light title">Descrição</span>
            <p class="description-text">{{game_description}}</p>
        </v-card-text>
        <v-card-actions v-if="genres.length!=0">
            <strong>Gêneros:</strong> 
            <span  class="genres-btn" v-for="(genre,i) in genres" :key="genre+i">
                <v-btn color="green light-4 white--text"  round small>{{genre}}</v-btn>
            </span>
        </v-card-actions>
    </v-card>
</template>

<style>
.description-text{
    margin-top: 10px; 
}
.genres-btn{
    margin: 0 7px;
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
}
</script>
