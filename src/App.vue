<template>
  <div id="app">
    <menu-app />
    <router-view/>
    <footer-app />
  </div>
</template>

<script>
import Footer from '@/components/Footer.vue';
import HeaderMenu from '@/components/HeaderMenu.vue';

export default {
  name: "App",
  components: {
    "footer-app": Footer,
    "menu-app": HeaderMenu
  }
}


</script>
<style>
a {
  text-decoration: none;  
}

ul, li {
  list-style: none;
}

#app {
  background: #B0A4A2;
}
</style>
