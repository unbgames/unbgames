<template>
  <div class="header-app">
    <router-link to="/">
      <h1 class="text-md-center white--text header-text">UnB Games</h1>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "HeaderMenu"
}
</script>
<style>
.header-app{
  background: black;
  padding: 10px 0;
}
.header-text{
  vertical-align: center;
}
</style>

