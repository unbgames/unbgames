<template>
  <div class="header-app">
    <router-link class="text-xs-center white--text header-text" to="/">
      <h1 class="font-weight-thin text-uppercase">UnB Games</h1>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "HeaderMenu"
};
</script>
<style>
.header-app {
  background: #282928;
  padding: 10px 0;
}
.header-text {
  vertical-align: center;
  text-decoration: none;
  color: red;
}
</style>

