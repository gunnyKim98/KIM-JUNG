<template>
<div class="container">
    <hr>
    <div>
      <div style="margin-bottom:10px;">
         <a  href="#" @click="$router.push('/community/newsboard')" style="color:green;">[커뮤니티] 뉴스게시판 >></a>
      </div>

      <h3  style="padding: 10px;">{{ article?.title }}</h3>
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
      <button class="btn btn-outline-dark" @click="putNewsArticleDetail">수정</button>
      <button class="btn btn-outline-dark" @click="deleteNewsArticleDetail">삭제</button>
    </div>
    <hr>
          <!--  유저게시판 댓글  -->
      <div  style="margin: 10px" v-for="comment in commentsList" :key="comment.id">
        <div v-if="article?.id === comment?.articles">
          <span>  {{ comment.username }} : {{ comment.content }}  </span>
   
          <button class="btn btn-outline-dark" v-if="comment.user === getUserInfo.id || getUserInfo.is_superuser === true" @click="deleteNewsComment(comment.id)">삭제</button>
        </div>
      </div>
    <div>
      <form>
        <textarea style="width: 400px ;height:50px; resize: none;" type="text" v-model="newComment"></textarea>
        <button class="btn btn-outline-dark" @click="newsCreateComment">작성</button>
      </form>
    </div>
    </div>



</template>

<script>
import {mapGetters} from "vuex";
import axios from "axios";
const baseURL = 'http://127.0.0.1:8000'
export default {
  name: "DetailNewsBoard",
  components: {
  },
  data() {
    return {
      article: null,
      newComment: null,
      userIsAuthor: false
    }
  },
  computed: {
    ...mapGetters(['getUserInfo']),
    commentsList() {
      return this.$store.getters.news_sendComments
    }
  },
  created() {
    this.getNewsArticleDetail(),
    this.NewsCommentsList()
  },
  methods: {
    getNewsArticleDetail() {
      axios({
        method: 'GET',
        url: `${baseURL}/articles/news/${ this.$route.params.id }/`,
      })
          .then((res) => {
            console.log(res)
            this.article = res.data
            this.$store.commit('NEWS_SET_FETCHED', res.data)
          })
          .catch((err) => {
            console.log(err)
          })
    },
    putNewsArticleDetail() {
      this.$router.push(`/community/newsboard/edit/${ this.$route.params.id }/`)
    },
    deleteNewsArticleDetail() {
      axios({
        method: 'DELETE',
        url: `${baseURL}/articles/news/${ this.$route.params.id }/`,
      })
          .then((res) => {
            console.log(res)
            this.article = res.data
            this.$router.push('/community/newsboard')
          })
          .catch((err) => {
            console.log(err)
          })
    },
    NewsCommentsList() {
      this.$store.dispatch('news_getComments')
    },
    newsCreateComment() {
      const user = this.getUserInfo.id
      const username = this.getUserInfo.nickname
      const content = this.newComment
      const token = this.$store.state.login.token
      console.log(`${baseURL}/articles/news/${ this.$route.params.id }/comments/`)
      axios({
        method: 'POST',
        url: `${baseURL}/articles/news/${ this.$route.params.id }/comments/`,
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
    deleteNewsComment(id) {
      const token = this.$store.state.login.token
      axios({
        method: 'DELETE',
        url: `${baseURL}/articles/news/comments/${ id }/`,
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
  margin-top: 100px ;
  margin-bottom: 100px ;
}

.contentbox {
  min-height: 300px;
  font-size: 17px;
}


</style>