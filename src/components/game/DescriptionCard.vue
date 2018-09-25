<template>
    <v-card color="blue-grey darken-2" class="white--text">
        <v-card-text>
            <span class="font-weight-light title">Descrição</span>
            <p class="description-text">{{game_description}}</p>
        </v-card-text>
        <!-- <v-card-actions>
            <v-btn flat color="orange">{{game_license}}</v-btn>
            <v-btn flat color="orange">Explore</v-btn>
        </v-card-actions> -->
    </v-card>
</template>

<style>
.description-text{
    margin-top: 10px; 
}
</style>

<script>
export default {
    name: "DescriptionCard",
    props: {
        game_description: String,
        game_license: Object
    }
}
</script>
