<template>
    <div class="container">
    <h2>게시글 수정</h2>
      <b-form @submit.prevent="newArticle">
        <b-form-group label="제목">
          <b-form-input v-model.trim="title"></b-form-input>
        </b-form-group>
        <b-form-group label="내용">
          <b-form-textarea v-model="content" rows="10"></b-form-textarea>
        </b-form-group>
        <b-button class="btn btn-outline-dark" @click="putUserArticle" variant="light">수정 완료</b-button>
      </b-form>
  </div>
</template>

<script>
import axios from "axios"
const baseURL = 'http://127.0.0.1:8000'
export default {
  name: "EditUserArticle",
  data() {
    return {
      article: null,
      title: null,
      content: null,
      category: null,
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      const token = this.$store.state.login.token
      axios({
        method: 'GET',
        url: `${baseURL}/articles/community/${ this.$route.params.id }/`,
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
    putUserArticle() {
      const token = this.$store.state.login.token
      const title = this.title
      const category = this.category
      const content = this.content
      const user = this.$store.state.login.userInfo.user
      const username = this.$store.state.login.userInfo.username
      axios({
        method: 'PUT',
        url: `${baseURL}/articles/community/${ this.$route.params.id }/`,
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
        this.$router.push(`/community/userboard/${ this.$route.params.id }`);
      });
    }
  }
}
</script>

<style scoped>
.container {
  width: 600px;
  margin: 0 auto;
  justify-content: center;
  align-items: center;
}
</style>