<template>
    <v-card color="blue-grey darken-2" class="white--text">
        <v-card-text>
            <p><strong>Versão do jogo:</strong> {{game.version}}</p>
            <p><strong>Ano de lançamento:</strong> {{game.year}}</p>
            <p>
                <strong>Repositório Oficial:</strong><br>
                <a class="link-app" :href="game.repository">{{game.name}}</a>
            </p>
            <p><strong> icone - Multiplayer</strong></p>
            <p><strong>Gêneros:</strong> 
            <span v-for="(genre,i) in game.genres" :key="genre+i">
                <v-btn round small dark>{{genre}}</v-btn>
            </span>
            </p>
            <span v-for="(award,i) in game.awards" :key="award.type+i">
                <div class="data-content" v-if="award.type=='game_year'">
                    <v-icon class="icon-content">mdi-xbox-controller</v-icon>
                    {{award.type_text}} - {{award.position}}
                </div>
                <div class="data-content" v-if="award.type=='devel'">
                    <v-icon class="icon-content">computer</v-icon> {{award.type_text}} - {{award.position}}
                </div>
                <div class="data-content" v-if="award.type=='art'">
                    <v-icon class="icon-content">color_lens</v-icon> {{award.type_text}} - {{award.position}}
                </div>
                <div class="data-content" v-if="award.type=='music'">
                    <v-icon class="icon-content">music_note</v-icon> {{award.type_text}} - {{award.position}}
                </div>
            </span>
        </v-card-text>
        <!-- <v-card-actions>
            <v-btn flat color="orange">Share</v-btn>
        </v-card-actions> 
            
        -->
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
<style>
.data-content {
    margin: 5px 0;
    vertical-align: baseline;
}
.icon-content {
    padding: 2px;
}
</style>
