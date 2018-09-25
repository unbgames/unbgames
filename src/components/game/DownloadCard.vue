<template>
    <div>
        <v-expansion-panel>
            <v-expansion-panel-content
            >
                <div slot="header"><span class="title font-weight-regular">Download</span></div>
                <v-card>
                    <v-card-text>
                        fdsa
                    </v-card-text>
                </v-card>
            </v-expansion-panel-content>
        </v-expansion-panel>
    </div>
</template>

<style>

</style>

<script>
export default {
    name: "AuthorsCard",
    props: {
        credits: Array,
    },
    data () {
      return {
        items: [
          { title: 'deb', icon: 'dashboard' },
          { title: 'Account', icon: 'account_box' },
          { title: 'Admin', icon: 'gavel' }
        ]
      }
    }
}
</script>
