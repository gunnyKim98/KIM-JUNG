<template>
  <div>
    <div>
      <h1>적금 상품 등록</h1>
    </div>
    <form>
      <p>상품명: {{ title }}</p>
      <p>판매자: {{ bank }}</p>
      <p>가입액: <input type="number" name="total" id="total" v-model="total"> 만원</p>
      <p>가입자: {{ getUserInfo.username }}</p>
      <p>연령: {{ getUserInfo.age }}</p>
      <p>소득: {{ getUserInfo.earn }}</p>
      <button @click="postSavingProduct">상품 가입</button>
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

</style>