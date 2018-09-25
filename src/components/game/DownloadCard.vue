<template>
    <div>
        <v-expansion-panel>
            <v-expansion-panel-content>
                <div slot="header"><span class="title font-weight-regular">Download</span></div>
                <v-data-table
                    :headers="headers"
                    :items="game.packs"
                    hide-actions
                    class="elevation-1"
                >
                    <template slot="items" slot-scope="props">
                    <td>
                        <a class="link-app" :href="props.item.link">
                            <v-icon color="white darken-2">mdi-{{ props.item.platform }}</v-icon> {{ props.item.platform }}
                        </a>
                    </td>
                        <td class="text-xs-left">{{ props.item.architecture }}</td>
                    </template>
                </v-data-table>
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
    game: Object
  },
  data() {
    return {
      headers: [
        {
          text: "Plataforma",
          align: "left",
          sortable: false,
          value: "platform"
        },
        {
          text: "Arquitetura",
          sortable: false,
          value: "architecture"
        }
      ]
    };
  }
};
</script>
