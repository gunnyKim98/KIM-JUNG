<template>
  <div class="container">
    <h3 style="margin-bottom: 10px">회원가입</h3>
    <form @submit.prevent="signUp">
      <label class="label" for="username"> id : </label>
      <input type="text" id="username" v-model="username"><br>

      <label class="label" for="password1"> 비밀번호 : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label class="label" for="password2"> 비밀번호 확인 : </label>
      <input type="password" id="password2" v-model="password2">

      <label class="label" for="nickname"> 닉네임 : </label>
      <input type="text" id="nickname" v-model="nickname">

      <label class="label" for="age"> 나이 : </label>
      <input type="number" id="age" v-model="age">

      <label class="label" for="age"> 성별 : </label>
      <select id="gender" v-model="sex" style="height:30px;">
      <option value="male">남성</option>
      <option value="female">여성</option>
      </select>
      <br>
      <label class="label" for="earn"> 연간 소득 : </label>
      <input type="number" id="earn" v-model="earn">

      <br>
      <div class="text-center" style="margin-top:10px">
       <input class="btn btn-outline-dark" type="submit" value="회원가입">
      </div>
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

<style scoped>
.container {
  width: 400px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  font-size: 16px;
  margin-top: 100px ;
  margin-bottom: 100px ;
}

.label{
  width: 120px;
}

.btn{
  width: 80%;
}

</style>