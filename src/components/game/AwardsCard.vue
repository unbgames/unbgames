<template>
  <div v-if="awards.length!=0">
    <div color="grey lighten-2">
      <p>
        <strong>Prêmios conquistados:</strong>
        <br>
      </p>
      <span v-for="(award,i) in awards" :key="i">
        <p class="award-text">{{award}}</p>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: "AwardsCard",
  props: {
    awards: Array
  }
};
</script>        

<style>
.award-text {
  vertical-align: baseline;
  margin-left: 10px;
}
</style>
