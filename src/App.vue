<template>
  <div id="app">
    <router-view/>
    <footer-app/>
  </div>
</template>

<script>
import Footer from "@/components/Footer.vue";

export default {
  name: "App",
  components: {
    "footer-app": Footer
  }
};
</script>
<style>
body {
  color: #282928;
}

ul,
li {
  list-style: none;
}

#app {
  background: #eeeeee;
}

.link-app {
  color: #282928;
}
</style>
