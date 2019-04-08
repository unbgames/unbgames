<template>
  <v-card>
    <v-expansion-panel class="grey lighten-2">
      <v-expansion-panel-content class="grey lighten-2">
        <div slot="header">
          <span class="title font-weight-thin text-uppercase">DOWNLOAD</span>
        </div>
        <v-data-table :headers="headers" :items="game.packs" hide-actions class="elevation-2">
          <template slot="items" slot-scope="props">
            <td class="grey lighten-2">
              <v-icon
                v-if="props.item.platform=='debian'"
                size="18"
                color="red"
              >mdi-{{ props.item.platform }}</v-icon>
              <v-icon
                v-else-if="props.item.platform=='fedora'"
                size="18"
                color="purple"
              >mdi-{{ props.item.platform }}</v-icon>
              <v-icon v-else size="18">mdi-{{ props.item.platform }}</v-icon>
              <a class="link-app" :href="props.item.link">
                <span class="body-1 text-capitalize platform-text">{{ props.item.platform }}</span>
              </a>
            </td>
            <td class="text-xs-left grey lighten-2">{{ props.item.architecture }}</td>
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
