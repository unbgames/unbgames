<template>
    <v-card color="grey lighten-2">
        <div v-for="credit in credits" :key="credit.role">
            <v-card-text>
                <span class="font-weight-light title">{{credit.role}}</span>
                <ul class="authors-names-list">
                    <li v-for="(author, i) in credit.authors" :key="credit.role+i+author.name">
                        <a class="author-link" :href="author.portifolio">{{author.name}}</a>
                    </li>
                </ul>
            </v-card-text>
        </div>
    </v-card>
</template>

<style>
.authors-names-list{
    margin-top: 10px;
}
.author-link {
    color: #282928;
}
</style>

<script>
export default {
    name: "AuthorsCard",
    props: {
        credits: Array,
    }
}
</script>
