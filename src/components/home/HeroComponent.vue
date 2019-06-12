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
  height: 75vh;
  background-image: linear-gradient(
      to right,
    rgba(#449D48, 0.95),
    rgba(#18332C, 0.95)
    ),
    url('https://user-images.githubusercontent.com/26073710/59325516-c3016e00-8cb9-11e9-8c65-b7e3d39dc296.png');
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;

  .header-text {
    color: white;
    text-align: center;
  }
}
</style>

