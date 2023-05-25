<template>
  <div class="container">
    <h2>공지 작성</h2>
      <b-form @submit.prevent="newAnnoArticle">
        <b-form-group label="제목">
          <b-form-input v-model.trim="title"></b-form-input>
        </b-form-group>
        <b-form-group label="내용">
          <b-form-textarea v-model="content" rows="10"></b-form-textarea>
        </b-form-group>
        <b-button class="btn btn-outline-dark" type="submit" variant="light">작성 완료</b-button>
      </b-form>
  </div>
</template>

<script>

import {mapGetters} from "vuex";
import axios from "axios";

const baseURL = 'http://127.0.0.1:8000'
export default {
  name: "CreateAnnounceBoard",
  data() {
    return {
      title: null,
      content: null,
      userData: [],
    }
  },
  computed: {
    ...mapGetters(['getUserInfo'])

  },
  created() {
  },
  methods: {
    newAnnoArticle() {
      console.log(this.$store.state.login.token)
      const token = this.$store.state.login.token
      const title = this.title
      const content = this.content

      if (!title) {
        alert('제목 입력해주세요')
        console.log(title)
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${baseURL}/articles/announce/`,
        data: {title, content },
        headers: {
          Authorization: `Token ${ token }`
        }
      })
          .then(() => {
            // console.log(res)
            this.$router.push('/community/announce')
          })
          .catch((err) => {
            console.log(err)
          })
    },
    getUserData() {
      this.userData = this.$store.state.userInfo

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
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  margin-top: 100px ;
  margin-bottom: 100px ;
}
</style>

