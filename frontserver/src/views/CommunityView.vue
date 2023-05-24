<template>
  <div>

  </div>
</template>

<script>


export default {
  name: "CommunityView",

  data() {
    return {
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    articles() {
      return this.$store.getters.sendArticles
    }
  },
  created() {
    this.authorization()
  },
  methods: {
    authorization() {
      if (this.isLogin) {
        console.log('Hello World')
      } else {
        alert('로그인이 필요한 페이지...')
        this.$router.push('/login')
      }
    },

  },
}
</script>

<style scoped>

</style>