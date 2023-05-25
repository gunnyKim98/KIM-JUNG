<template>
    <div class="container">

      <hr>
      <div style="margin-bottom:10px;">
         <a  href="#" @click="$router.push('/profile')" style="color:green;">프로필로 >></a>
      </div>
      <h3 style="padding: 10px;">회원 정보 수정</h3>
      <b-form @submit.prevent="userInfoChange">
      <hr>
      <div class="contentbox">
        <label for="nickname" style="margin-left: 30px;">닉네임 : </label>
        <input type="text" id="nickname" v-model.trim="nickname">
        <p style="margin-left: 30px;">아이디 : {{ username }}</p>
        <p style="margin-left: 30px;">이름 : {{ first_name }} {{ last_name }}</p>
        <p style="margin-left: 30px;">나이 : {{ age }}</p>
        <p style="margin-left: 30px;">성별 : {{ sex }}</p>
        <label for="earn" style="margin-left: 30px;">소득 : </label>
        <input type="number" id="earn" v-model.trim="earn">
        
        </div>
        <input class="btn btn-outline-dark" style="margin-left: 30px;" type="submit" id="submit" value="수정 완료">
      </b-form>
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
      username: this.$store.state.login.userInfo.username,
      nickname: this.$store.state.login.userInfo.nickname,
      age: this.$store.state.login.userInfo.age,
      earn: this.$store.state.login.userInfo.earn,
      first_name: this.$store.state.login.userInfo.first_name,
      last_name: this.$store.state.login.userInfo.last_name,
      sex: this.$store.state.login.userInfo.sex,
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
      const sex = this.sex

      console.log(token, username, nickname, age, earn)
      axios({
        method: 'POST',
        url: `${baseURL}/users/change/`,
        data: {
          username, nickname, age, earn, sex
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
.container {
  width: 600px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  margin-top: 100px ;
  margin-bottom: 100px ;
}
</style>