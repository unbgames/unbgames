<template>
    <div>
        <v-btn large block>
            Download <v-icon right dark>save_alt</v-icon>
        </v-btn>
    </div>
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
