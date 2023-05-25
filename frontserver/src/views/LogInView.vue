<template>
  <div class="container">
    
    <form @submit.prevent="login">
      <label class="label" for="username">id : </label>
      <input type="text" id="username" v-model="username"><br>

      <label class="label" for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <div class="text-center" style="margin-top: 10px">
        <input class="btn btn-outline-dark" type="submit" value="로그인">
      </div>
    </form>


  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)

    },

  }
}
</script>

<style scoped>
.container {
  width: 350px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  margin-top: 100px;
  margin-bottom: 100px;
  
}

.label{
  width: 100px;
  font-size: 16px;;
}

.btn{
  width: 80%;
  
}
</style>