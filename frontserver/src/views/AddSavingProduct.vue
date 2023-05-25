<template>
  <div class="container">
    <h3 style="margin-bottom: 10px">적금 상품 등록</h3>
    <form @submit.prevent="postSavingProduct">
      <p>상품명 : {{ title }}</p>
      <p>판매자 : {{ bank }}</p>

      <p><label class="label" for="password2"> 가입액 : </label>
      <input type="number" name="total" id="total" v-model="total" style="margin-left: 10px;"> (만원)</p>

      <p>가입자 : {{ getUserInfo.username }}</p>
      <p>나이 : {{ getUserInfo.age }}</p>
      <p>연간 소득 : {{ getUserInfo.earn }} 만원</p>

      <br>
      <div class="text-center" style="margin-top:10px">
       <input class="btn btn-outline-dark" type="submit" value="상품가입" >
      </div>
    </form>
  </div>
  
</template>

<script>
import {mapGetters} from "vuex";
import axios from "axios";
const baseURL = 'http://127.0.0.1:8000'

export default {
  name: "AddSavingProduct",
  data() {
    return {
      title: this.$route.params.title,
      bank: this.$route.params.bank,
      total: null,
    }
  },
  computed: {
    ...mapGetters(['getUserInfo']),
  },
  created() {

  },
  methods: {
    postSavingProduct() {
      console.log(this.$store.state.login.token)
      const token = this.$store.state.login.token
      const title = this.title
      const content = this.bank
      const cost = this.total
      const userInfo = this.getUserInfo
      const username = this.getUserInfo.user


      axios({
        method: 'POST',
        url: `${baseURL}/users/my_saving/${userInfo.id}/`,
        data: {
          'title': title,
          'content': content,
          'username': username,
          'cost': cost,
          'earn' : userInfo.earn,
          'age' : userInfo.age
        },
        headers: {
          Authorization: `Token ${ token }`
        }
      })
          .then(() => {
            this.$store.dispatch('profileDetail')
          })
          .catch((err) => {
            console.log(err)
          })
      this.$nextTick(() => {
        this.$router.push('/finlife');
      });
    }

  },
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
</style>