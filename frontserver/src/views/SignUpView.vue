<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username"> id : </label>
      <input type="text" id="username" v-model="username"><br>
<!--      <br>-->
<!--      <label for="email"> Email : </label>-->
<!--      <input type="text" id="email" v-model="email">-->
      <br>
      <label for="password1"> 비밀번호 : </label>
      <input type="password" id="password1" v-model="password1"><br>
      <br>
      <label for="password2"> 비밀번호 확인 : </label>
      <input type="password" id="password2" v-model="password2">
      <br>
      <label for="nickname"> 닉네임 : </label>
      <input type="text" id="nickname" v-model="nickname">
      <br>
      <label for="age"> 나이 : </label>
      <input type="number" id="age" v-model="age">
      <br>
      <label for="sex"> 성별 : </label>
      <input type="text" id="sex" v-model="sex">
      <br>
      <label for="earn"> 연간 소득 : </label>
      <input type="number" id="earn" v-model="earn">

      <br>
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      // email: null,
      password1: null,
      password2: null,
      nickname: null,
      age: null,
      sex: null,
      earn: null,
    }
  },
  methods: {
    signUp() {
      console.log('signup')
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      // const email = this.email
      const nickname = this.nickname
      const age = this.age
      const sex = this.sex
      const earn = this.earn

      const payload = {
        username, password1, password2, nickname, age, sex, earn, //email
      }

      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>
