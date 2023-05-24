<template>
  <div>
    <form>
      <p>제목 : </p>
      <input type="text" v-model="title">
      <br>
      <p>말머리 :  </p>
      <input type="text" v-model="category">
      <br>
      <p>내용 : </p>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea>
      <br>
      <button @click="putAnnoArticle">수정하기</button>
    </form>
  </div>
</template>

<script>
import axios from "axios"
const baseURL = 'http://127.0.0.1:8000'

export default {
  name: "EditAnnounceArticle",
  data() {
    return {
      article: null,
      title: null,
      content: null,
      category: null,
    }
  },
  created() {
    this.getAnnoArticleDetail()
  },
  methods: {
    getAnnoArticleDetail() {
      const token = this.$store.state.login.token
      axios({
        method: 'GET',
        url: `${baseURL}/articles/announce/${ this.$route.params.id }/`,
        headers: {
          Authorization: `Token ${ token }`
        }
      })
          .then((res) => {
            console.log(res)
            this.article = res.data
            this.title = res.data.title
            this.category = res.data.category
            this.content = res.data.content
            this.$store.commit('SET_FETCHED', res.data)
          })
          .catch((err) => {
            console.log(err)
          })
    },
    putAnnoArticle() {
      const token = this.$store.state.login.token
      const title = this.title
      const category = this.category
      const content = this.content
      const user = this.$store.state.login.userInfo.user
      const username = this.$store.state.login.userInfo.username
      axios({
        method: 'PUT',
        url: `${baseURL}/articles/announce/${ this.$route.params.id }/`,
        data: {
          title, content, category, user, username
        },
        headers: {
          Authorization: `Token ${ token }`
        }
      })
          .then((res) => {
            console.log(res)
          })
          .catch((err) => {
            console.log(err)
          })
      this.$nextTick(() => {
        this.$router.push(`/community/announce/${ this.$route.params.id }`);
      });
    }
  }
}
</script>

<style scoped>

</style>