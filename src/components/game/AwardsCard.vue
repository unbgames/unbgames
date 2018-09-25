<template>
    <div v-if="awards.length!=0">
        <div color="grey lighten-2">
            <p>
                <strong>Prêmios conquistados:</strong><br>
            </p>
            <span v-for="(award,i) in awards" :key="award.type+i">
                <div class="data-content subheading award-items" v-if="award.type=='game_year'">
                    <v-icon color="green light-4" size="20" class="icon-content">mdi-xbox-controller</v-icon>
                    <span class="award-text">{{award.position}} - {{award.type_text}}</span>
                </div>
                <div class="data-content subheading award-items text-truncate" v-if="award.type=='devel'">
                    <v-icon color="green light-4" size="20" class="icon-content">computer</v-icon>
                    <v-tooltip>
                        <span slot="activator" class="award-text">{{award.position}} - {{award.type_text}}</span>
                        <span>{{award.type_text}}</span>
                    </v-tooltip>
                </div>
                <div class="data-content subheading award-items" v-if="award.type=='art'">
                    <v-icon color="green light-4" size="20" class="icon-content">color_lens</v-icon>
                    <span  class="award-text">{{award.position}} - {{award.type_text}}</span>
                </div>
                <div class="data-content subheading award-items" v-if="award.type=='music'">
                    <v-icon color="green light-4" size="20" class="icon-content">music_note</v-icon>
                    <span class="award-text">{{award.position}} - {{award.type_text}}</span>
                </div>
            </span>
        </div>
    </div>
</template>

<script>
export default {
    name: "AwardsCard",
    props: {
        awards: Array
    }
}
</script>        

<style>
.award-text {
    vertical-align: baseline;
    margin-left: 10px;
}
</style>
