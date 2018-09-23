<template>
    <v-card color="blue-grey darken-2" class="white--text">
        <v-card-media
            :src="game.cover_image"
            height="200px"
        ></v-card-media>
        <v-card-text>
            <li>Versão: {{game.version}}</li>
            <span v-for="(award,i) in game.awards" :key="award.type+i">
                <li v-if="award.type=='game_year'">
                    <v-icon>videogame_asset</v-icon> {{award.type_text}} - {{award.position}}
                </li>
                <li v-if="award.type=='devel'">
                    <v-icon>computer</v-icon> {{award.type_text}} - {{award.position}}
                </li>
                <li v-if="award.type=='art'">
                    <v-icon>color_lens</v-icon> {{award.type_text}} - {{award.position}}
                </li>
                <li v-if="award.type=='music'">
                    <v-icon>music_note</v-icon> {{award.type_text}} - {{award.position}}
                </li>
            </span>
        </v-card-text>
        <!-- <v-card-actions>
            <v-btn flat color="orange">Share</v-btn>
        </v-card-actions> -->
    </v-card>  
</template>

<script>
export default {
    name: "GameCardDescription",
    props: {
        game: Object
    }
}
</script>        
          