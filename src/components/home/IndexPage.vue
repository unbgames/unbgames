<template>
  <div class="header-image">
    <div class="header-text">
      <h1 class="display-4 font-weight-light">UnBGames</h1>
      <p class="font-weight-light">
        Acervo central de jogos feitos na Universidade de Brasilia e em seus campi.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "IndexPage"
};
</script>

<style lang="scss" scoped>
.header-image {
  height: 70vh;
  background-image: linear-gradient(
      to right,
      rgba(#449d48, 0.95),
      rgba(#18332c, 0.95)
    ),
    url("https://user-images.githubusercontent.com/26073710/59325516-c3016e00-8cb9-11e9-8c65-b7e3d39dc296.png");
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;

  .header-text {
    color: white;
    text-align: center;
  }

  p {
    font-size: 20px;
  }
}
</style>

