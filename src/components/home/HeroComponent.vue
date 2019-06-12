<template>
  <div class="header-image">
    <div class="header-text">
       <h3 class="display-3">UnBGames</h3>
      <p>Acervo central de jogos feitos na Universidade de Brasilia e em seus campi.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "HeroComponent"
};
</script>

<style lang="scss" scoped>
.header-image {
  height: 70vh;
  background-image: linear-gradient(
    to right bottom,
    rgba(#4caf50, 1),
    rgba(#1f4037, 1)
  );
  display: flex;
  justify-content: center;
  align-items: center;

  .header-text {
    color: white;
    text-align: center;
  }
}
</style>

