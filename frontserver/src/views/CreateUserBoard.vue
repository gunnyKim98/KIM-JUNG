<template>
  <div class="container">
    <h2>게시글 작성</h2>
      <b-form @submit.prevent="newArticle">
        <b-form-group label="제목">
          <b-form-input v-model.trim="title"></b-form-input>
        </b-form-group>
        <b-form-group label="카테고리">
          <b-form-select  v-model="category">
           <option v-for="(item, idx) in selectcategory" :key="idx" :value="item">{{ item }}</option>
          </b-form-select>
        </b-form-group>
        <b-form-group label="내용">
          <b-form-textarea v-model="content" rows="10"></b-form-textarea>
        </b-form-group>
        <b-button class="btn btn-outline-dark" type="submit" variant="light">작성 완료</b-button>
      </b-form>
  </div>

</template>

<script>
import { mapGetters } from "vuex"
import axios from "axios";
const baseURL = 'http://127.0.0.1:8000'

export default {
  name: "CreateUserBoard",
  data() {
    return {
      title: null,
      content: null,
      category: null,
      userData: [],
      selectcategory: ['자유','재테크','리뷰','Q&A','유머',]
    }
  },
  computed: {
    ...mapGetters(['getUserInfo'])

  },
  created() {
  },
  methods: {
    newArticle() {
      // const user = this.getUserInfo.id
      // const username = this.getUserInfo.username
      // console.log(user)
      console.log(this.$store.state.login.token)
      const token = this.$store.state.login.token
      const title = this.title
      const content = this.content
      const category = this.category

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
        url: `${baseURL}/articles/community/`,
        data: {title, content, category },
        headers: {
          Authorization: `Token ${ token }`
        }
      })
        .then(() => {
          // console.log(res)
          this.$router.push('/community/userboard')
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