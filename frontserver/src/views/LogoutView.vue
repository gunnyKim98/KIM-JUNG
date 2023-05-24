<template>
  <div></div>
</template>

<script>
export default {
  name: "LogoutView",
  created() {
    this.$store.dispatch('logout')
  }
}
</script>

<style scoped>

</style>