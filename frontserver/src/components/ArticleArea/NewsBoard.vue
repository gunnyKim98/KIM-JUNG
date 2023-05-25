<template>
  <div class="container">
    <h3 style="margin:10px;">뉴스게시판</h3>
    
      <div style="white-space: nowrap; display: flex;">
        <div style="flex: 1;">
          <button class="btn btn-outline-dark" @click="$router.push('/community/announce')">공지사항</button>
          <button disabled class="btn btn-outline-dark" @click="$router.push('/community/newsboard')">뉴스게시판</button>
          <button class="btn btn-outline-dark" @click="$router.push('/community/userboard')">유저게시판</button>
        </div>
        <div style="text-align: right;">
          <button class="btn btn-outline-dark float-right"  @click="newArticle">글 작성</button>
        </div>
      </div>

    <!-- 초기화면. 검색하지 않은 상태 -->
    <div v-if="!searchState" class="table-container">
      <table class="table" style="white-space: nowrap; width:1350px;">
        <thead>
        <tr>
          <th style="width: 10%;">글 번호</th>
          <th style="width: 15%">말머리</th>
          <th style="width: 40%;">제목</th>
          <th style="width: 20%;">작성자</th>
          <th style="width: 15%;">작성 날짜</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(article, idx) in articles" :key="article.id">
          <td>{{ idx + 1 }}</td>
          <td>뉴스</td>
          <td ><router-link :to="`/community/newsboard/${ article.id }`"><a style="color:black;">{{article.title}}</a></router-link></td>
          <td>{{article.username}}</td>
          <td>{{article.created_at.slice(0,10)}}</td>
        </tr>
        </tbody>
      </table>
    </div>

    <!-- 검색화면. -->
        <div v-if="searchState" class="table-container">
      <table class="table" style="white-space: nowrap; width:1350px;">
        <thead>
        <tr>
          <th style="width: 10%;">글 번호</th>
          <th style="width: 15%">말머리</th>
          <th style="width: 40%;">제목</th>
          <th style="width: 20%;">작성자</th>
          <th style="width: 15%;">작성 날짜</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(article, idx) in searcharticles" :key="article.id">
          <td>{{ idx + 1 }}</td>
          <td>뉴스</td>
          <td ><router-link :to="`/community/newsboard/${ article.id }`"><a style="color:black;">{{article.title}}</a></router-link></td>
          <td>{{article.username}}</td>
          <td>{{article.created_at.slice(0,10)}}</td>
        </tr>
        </tbody>
      </table>
    </div>

    <!-- 검색 바 -->
    <div class="searchbar">
      <select v-model="selectedSearchCategory" class="custom-select">
        <option v-for="(item,idx) in searchCategory" :key="idx" :value="item">{{item}}</option>
      </select>
      <input style="margin:10px;" type="text" v-model="searchQuery">
      <button class="btn btn-outline-dark" @click="searchArtcle">검색</button>
      <button class="btn btn-outline-dark" @click="viewAllArticles">전체 글 보기</button>

    </div>

  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: 'NewsBoard',
  data(){
    return{
      searchState: false,
      searchCategory: ['선택안함', '제목+내용', '제목만', '작성자'],
      selectedSearchCategory: '선택안함',
      searchQuery: '',
      searcharticles: []
    }
  },
  computed: {
    ...mapGetters(['getUserInfo']),
    articles() {
      return this.$store.getters.news_sendArticles
    },
    ...mapGetters(['isLogin'])
  },
  created() {
    this.getNewsArticles()
  },
  methods:{
    getNewsArticles() {
      this.$store.dispatch('news_getGet')
    },
    newArticle() {
      if (!this.isLogin){
        alert('로그인이 필요한 서비스입니다.')
        this.$router.push('/login')
        return
      }
      if (!this.getUserInfo.is_superuser && !this.getUserInfo.is_staff){
        alert('일반유저는 뉴스 게시글을 작성할 수 없습니다.')
        return
      }  
      this.$router.push('/community/newsboard/create')
    },
    makeSearchCategory(){
      this.selected
    },
    searchArtcle(){
      if (this.selectedSearchCategory === '선택안함'){
        alert('검색 카테고리를 선택해주세요.')
        return
      }

      if (this.searchQuery.length === 0){
        alert('검색어를 입력해주세요.')
        return
      }

      const articles = this.$store.state.newsboard.news_articles
      let searcharticlelist = []
      const searchqueries = this.searchQuery.split(' ')
      if (this.selectedSearchCategory === '제목+내용'){
        for (let i of articles){
          const searchtitlebool = searchqueries.some(substring => i.title.includes(substring))
          const searchcontentbool = searchqueries.some(substring => i.content.includes(substring))
          if (searchtitlebool || searchcontentbool){
            searcharticlelist.push(i)
          }
        }
        if (searcharticlelist.length === 0){
            alert('검색 결과가 없습니다.')
            return
          }
      } else if (this.selectedSearchCategory === '제목만') {
        for (let i of articles){
          const searchtitlebool = searchqueries.some(substring => i.title.includes(substring))
          if (searchtitlebool){
            searcharticlelist.push(i)
          }
        } 
        if (searcharticlelist.length === 0){
            alert('검색 결과가 없습니다.')
            return
          }
      } else {
        for (let i of articles){
          const searchuserbool = searchqueries.some(substring => i.username.includes(substring))
          if (searchuserbool){
            searcharticlelist.push(i)
          }
        } 
        if (searcharticlelist.length === 0){
          alert('검색 결과가 없습니다.')
          return
        }
      }

      this.searcharticles = searcharticlelist
      this.searchState = true
      
    },
    viewAllArticles(){
      this.searchState = false
    }
  }
}

</script>

<style scoped>
.container {
  width: 1350px;
  margin: 0 auto;
  justify-content: center;
  align-items: center;
}

.table-container {
  display: flex;
  justify-content: center;
  text-align: center;
}

.custom-select {
  width: 150px; /* 원하는 크기로 조정 */
  height: 40px; /* 원하는 크기로 조정 */
  font-size: 16px; /* 원하는 글꼴 크기로 조정 */
  margin: 10px;
}

.searchbar{
  display: flex;
  justify-content: center;
  text-align: center;
}

.btn{
  margin: 10px;
}
</style>