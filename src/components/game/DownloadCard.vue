<template>
    <v-card color="grey lighten-2">
        <v-expansion-panel>
            <v-expansion-panel-content>                
                <div slot="header"><span class="title font-weight-thin text-uppercase">DOWNLOAD</span></div>
                <v-data-table
                    :headers="headers"
                    :items="game.packs"
                    hide-actions
                    class="elevation-2"
                >
                    <template slot="items" slot-scope="props">
                    <td>
                        <v-icon v-if="props.item.platform=='debian'" size="18" color="red">mdi-{{ props.item.platform }}</v-icon>
                        <v-icon v-else-if="props.item.platform=='fedora'" size="18" color="purple">mdi-{{ props.item.platform }}</v-icon>
                        <v-icon v-else size="18">mdi-{{ props.item.platform }}</v-icon>
                        <a class="link-app" :href="props.item.link">
                            <span class="body-1 text-capitalize platform-text">{{ props.item.platform }}</span>
                        </a>
                    </td>
                        <td class="text-xs-left">{{ props.item.architecture }}</td>
                    </template>
                </v-data-table>
            </v-expansion-panel-content>
        </v-expansion-panel>
    </v-card>
</template>

<style>
.platform-text {
    font-size: 1.2em;
    padding: 5px;
}
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
