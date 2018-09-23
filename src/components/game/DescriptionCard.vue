<template>
    <v-card color="blue-grey darken-2" class="white--text">
        <v-card-title>
            <span class="headline">Descrição</span>
        </v-card-title>
        <v-card-text>
            {{game_description}}
        </v-card-text>
        <v-card-actions>
            <v-btn flat color="orange">{{game_license}}</v-btn>
            <v-btn flat color="orange">Explore</v-btn>
        </v-card-actions>
    </v-card>
</template>

<style>

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
