<template>
  <div class="home">
    <GameList/>
  </div>
</template>

<script>
// @ is an alias to /src
import GameList from '@/components/GameList.vue'

export default {
  name: 'home',
  components: {
    GameList
  }
}
</script>
