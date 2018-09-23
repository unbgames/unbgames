<template>
    <v-card>
        <v-card-media
            :src="cover_image"
            height="200px"
        ></v-card-media>
        <v-card-title primary-title>
            <div>
                <h4 class="headline mb-0">{{name}}</h4>
            </div>
        </v-card-title>
        <!-- <v-card-actions>
            <v-btn flat color="orange">Share</v-btn>
        </v-card-actions> -->
    </v-card>  
</template>

<script>
export default {
    name: "GameCard",
    props: {
        cover_image: String,
        name: String
    }
}
</script>        
          