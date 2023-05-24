<template>
  <div>

    <form @submit.prevent="userInfoChange">
<!--      <label for="username">id : </label>-->
<!--      <br>-->
<!--      <input type="text" id="username" v-model.trim="username">-->
      <br>
      <label for="nickname">닉네임 : </label>
      <br>
      <input type="text" id="nickname" v-model.trim="nickname">
      <br>
<!--      <label for="last_name">성 : </label>-->
<!--      <br>-->
<!--      <input type="text" id="last_name" v-model.trim="last_name">-->
<!--      <br>-->
<!--      <label for="first_name">이름 : </label>-->
<!--      <br>-->
<!--      <input type="text" id="first_name" v-model.trim="first_name">-->
<!--      <br>-->
<!--      <label for="age">나이 : </label>-->
<!--      <br>-->
<!--      <input type="number" id="age" v-model.trim="age">-->
<!--      <br>-->
      <label for="earn">소득 : </label>
      <br>
      <input type="number" id="earn" v-model.trim="earn">
      <br>
      <input type="submit" id="submit">
    </form>

  </div>
</template>

<script>
import axios from "axios";
import {mapGetters} from "vuex";
const baseURL = 'http://127.0.0.1:8000'
export default {
  name: "EditProfileView",
  data() {
    return {
      // username: this.$store.state.login.userInfo.username,
      user: this.$store.state.login.userInfo,
      nickname: this.$store.state.login.userInfo.nickname,
      age: this.$store.state.login.userInfo.age,
      earn: this.$store.state.login.userInfo.earn,
      first_name: this.$store.state.login.userInfo.first_name,
      last_name: this.$store.state.login.userInfo.last_name,
    }
  },
  computed: {
    ...mapGetters(['getUserInfo']),
  },
  methods: {
    userInfoChange() {
      const token = this.$store.state.login.token
      const userdata = this.getUserInfo
      const username = userdata.username
      // const first_name = this.first_name
      // const last_name = this.last_name
      const nickname = this.nickname
      const age = this.age
      const earn = this.earn
      console.log(1)
      console.log(token, username, nickname, age, earn)
      axios({
        method: 'POST',
        url: `${baseURL}/users/change/`,
        data: {
          username, nickname, age, earn
        },
        headers: {
          Authorization: `Token ${ token }`
        }
      })
        .then((res) => {
          console.log(res)
          this.$store.dispatch('profileDetail')
        })
        .catch((err) => {
          console.log(err)
        })
      this.$nextTick(() => {
        this.$router.push('/profile')
      })
    }
  }
}
</script>

<style scoped>

</style>