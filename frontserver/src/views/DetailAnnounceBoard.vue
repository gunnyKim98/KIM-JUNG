<template>
  <div class="container">
    <hr>
    <div>
      <div style="margin-bottom:10px;">
         <a  href="#" @click="$router.push('/community/announce')" style="color:green;">[커뮤니티] 공지사항 >></a>
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
    <div v-if="getUserInfo.id === article?.user || getUserInfo.is_superuser === true">
      <button class="btn btn-outline-dark" @click="putAnnoArticleDetail">수정하기</button>
      <button class="btn btn-outline-dark" @click="deleteAnnoArticleDetail">삭제하기</button>
    </div>
    <hr>
    <br>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import axios from "axios";

const baseURL = 'http://127.0.0.1:8000'
export default {
  name: "DetailAnnounceBoard",
  components: {

  },
  data() {
    return {
      article: null,
      comments: null,
      userIsAuthor: false
    }
  },
  computed: {
    ...mapGetters(['getUserInfo']),
  },
  created() {
    this.getAnnoArticleDetail()
  },
  methods: {
    getAnnoArticleDetail() {
      console.log(1)
      axios({
        method: 'GET',
        url: `${baseURL}/articles/announce/${ this.$route.params.id }/`,
      })
          .then((res) => {
            console.log(res)
            this.article = res.data
            this.$store.commit('ANNO_SET_FETCHED', res.data)
          })
          .catch((err) => {
            console.log(err)
          })
    },
    putAnnoArticleDetail() {
      this.$router.push(`/community/announce/edit/${ this.$route.params.id }/`)
    },
    deleteAnnoArticleDetail() {
      axios({
        method: 'DELETE',
        url: `${baseURL}/articles/announce/${ this.$route.params.id }/`,
      })
          .then((res) => {
            console.log(res)
            this.article = res.data
            this.$router.push('/community/announce')
          })
          .catch((err) => {
            console.log(err)
          })
    },
  }
}
</script>

<style scoped>
.btn{
  margin: 10px;
  width: 90px;;
  height: 35px;
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