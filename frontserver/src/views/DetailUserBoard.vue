<template>
<div class="container">
    <hr>
    <div>
      <div style="margin-bottom:10px;">
         <a  href="#" @click="$router.push('/community/userboard')" style="color:green;">[커뮤니티] 유저게시판 >></a>
      </div>

      <h3  style="padding: 10px;">[{{article?.category}}] {{ article?.title }}</h3>
      <h6 class="text-right">작성자 : {{ article?.username  }}</h6>
      <hr>
      <div class="contentbox">
          <p style="padding: 30px;">{{ article?.content }}</p>
      </div>
      <hr>
      <div class="text-right" style="padding:0px;"> 
        <p style="padding:0px;">작성시간 : {{ article?.created_at.slice(0,4) }}년 {{ article?.created_at.slice(5,7) }}월 {{ article?.created_at.slice(8,10) }}일 {{ article?.created_at.slice(11,13) }}시 {{ article?.created_at.slice(14,16) }}분 </p>
        <p style="padding:0px;">최근수정 : {{ article?.updated_at.slice(0,4) }}년 {{ article?.updated_at.slice(5,7) }}월 {{ article?.updated_at.slice(8,10) }}일 {{ article?.updated_at.slice(11,13) }}시 {{ article?.updated_at.slice(14,16) }}분</p>
      </div>
      <hr>


    </div>
    <div class="text-right" v-if="getUserInfo.id === article?.user || getUserInfo.is_superuser === true">
      <button class="btn btn-outline-dark" @click="putArticleDetail">수정</button>
      <button class="btn btn-outline-dark" @click="deleteArticleDetail">삭제</button>
    </div>
    <hr>
          <!--  유저게시판 댓글  -->
      <div v-for="comment in commentsList" :key="comment.id">
        <div v-if="article?.id === comment?.article">
          <span>  {{ comment.username }}  </span> |
          <span>  {{ comment.content }}  </span>
          <button class="btn btn-outline-dark" v-if="comment.user === getUserInfo.id || getUserInfo.is_superuser === true" @click="deleteComment(comment.id)">삭제</button>
        </div>
      </div>
    <div>
      <form>
        <textarea style="width: 400px ;height:50px; resize: none;" type="text" v-model="newComment"></textarea>
        <button class="btn btn-outline-dark" @click="createComment">작성</button>
      </form>
    </div>
    </div>

  


</template>

<script>
import axios from 'axios'
import {mapGetters} from "vuex";
const baseURL = 'http://127.0.0.1:8000'


export default {
  name: "DetailUserBoard",
  components: {
  },
  data() {
    return {
      article: null,
      newComment: null,
      userIsAuthor: false,
    }
  },
  computed: {
    ...mapGetters(['getUserInfo']),
    commentsList() {
      return this.$store.getters.sendComments
    }
  },
  created() {
    this.getArticleDetail(),
    this.CommentsList()

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
          this.$store.commit('SET_FETCHED', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    putArticleDetail() {
      this.$router.push(`/community/userboard/edit/${ this.$route.params.id }/`)
    },
    deleteArticleDetail() {
      const token = this.$store.state.login.token
      axios({
        method: 'DELETE',
        url: `${baseURL}/articles/community/${ this.$route.params.id }/`,
        headers: {
          Authorization: `Token ${ token }`
        }
      })
        .then((res) => {
          console.log(res)
          this.article = res.data
          this.$router.push('/community/userboard')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    CommentsList() {
      this.$store.dispatch('getComments')
    },
    createComment() {
      const user = this.getUserInfo.id
      const username = this.getUserInfo.nickname
      const content = this.newComment
      const token = this.$store.state.login.token
      console.log(`${baseURL}/articles/community/${ this.$route.params.id }/comments/`)
      axios({
        method: 'POST',
        url: `${baseURL}/articles/community/${ this.$route.params.id }/comments/`,
        data: {
          user, username, content
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
    },
    deleteComment(id) {
      const token = this.$store.state.login.token
      axios({
        method: 'DELETE',
        url: `${baseURL}/articles/community/comments/${ id }/`,
        data: {
        },
        headers: {
          Authorization: `Token ${ token }`
        }
      })
          .then((res) => {
            console.log(res)
            location.reload()
          })
          .catch((err) => {
            console.log(err)
          })
    }
  }
}
</script>

<style scoped>
.btn{
  margin-left: 10px;
  margin-bottom: 5px;
  font-size: 12px;
  width: 50px;;
  height: 28px;
  text-align: center;
}

.container {
  width: 600px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
}

.contentbox {
  min-height: 300px;
  font-size: 17px;
}


</style>