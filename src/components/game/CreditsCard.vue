<template>
    <v-card color="blue-grey darken-2" class="white--text">
        <div v-for="credit in credits" :key="credit.role">
            <v-card-title>
                <span class="headline">{{credit.role}}</span>
            </v-card-title>
            <v-card-text>
                <ul>
                    <li v-for="(author, i) in credit.authors" :key="credit.role+i+author.name">
                        {{author.name}}
                    </li>
                </ul>
            </v-card-text>
        </div>
    </v-card>
</template>

<style>

</style>

<script>
export default {
    name: "AuthorsCard",
    props: {
        credits: Array,
    }
}
</script>
