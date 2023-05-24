<template>
  <div>
    <!-- 메인화면 캐러셀 -->
    <div id="carouselIndicators" class="carousel slide container" data-ride="carousel">
      <ol class="carousel-indicators">
        <li
            v-for="(item, index) in carouselItems"
            :key="index"
            :data-target="carouselTarget"
            :data-slide-to="index"
            :class="{ active: index === activeIndex }"
        ></li>
      </ol>
      <div class="carousel-inner">
        <div
            v-for="(item, index) in carouselItems"
            :key="index"
            class="carousel-item"
            :class="{ active: index === activeIndex }"
        >
          <div class="container carousel-box" >
            <div class="row">
              <div class="col-md-6">
                <div class="carousel-content">
                  <h3>{{ item.title }}</h3>
                  <p>{{ item.description }}</p>
                  <button class="btn btn-outline-dark" @click="moveRouter(item.nextrouter
                  )">자세히</button>
                </div>
              </div>
              <div class="col-md-6 imgcontainer">
                <img :src="`${item.imageSrc}`" class="img-fluid" alt="Carousel Image">
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>

    <!-- 게시판 미리보기-->
    <div class="container">
      <div class="row">
        <div class="col">
          <div class="row">
            <div class="col-md-4">
              <b-card title="최신 공지사항" class="mb-3" style="height:254px">
                <ul>
                  <li v-for="(article, idx) in announcearticles" :key="idx"><router-link :to="`/community/announce/${ article.id }`"><a style="color:black;">{{ article.title.length > 13 ? article.title.slice(0, 13) + '...' : article.title }}</a></router-link></li>
                </ul>
                <div class="text-right">
                  <button class="btn btn-outline-dark" @click="$router.push('/community/announce')">더 보기</button>
                </div>
              </b-card>
            </div>
            <div class="col-md-4">
              <b-card title="최신 뉴스" class="mb-3" style="height:254px">
                <ul>
                  <li v-for="(article, idx) in newsarticles" :key="idx"><router-link :to="`/community/newsboard/${ article.id }`"><a style="color:black;">{{ article.title.length > 13 ? article.title.slice(0, 13) + '...' : article.title }}</a></router-link></li>
                </ul>
                <div class="text-right">
                  <button class="btn btn-outline-dark" @click="$router.push('/community/newsboard')">더 보기</button>
                </div>
              </b-card>
            </div>
            <div class="col-md-4">
              <b-card title="최신 유저게시글" class="mb-3" style="height:254px">
                <ul>
                  <li v-for="(article, idx) in userarticles" :key="idx"><router-link :to="`/community/userboard/${ article.id }`"><a style="color:black;">{{ article.title.length > 13 ? article.title.slice(0, 13) + '...' : article.title }}</a></router-link></li>
                </ul>
                <div class="text-right">
                  <button class="btn btn-outline-dark" @click="$router.push('/community/userboard')">더 보기</button>
                </div>
              </b-card>
            </div>
            
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: 'HomeView',
  data() {
    return {
      carouselItems: [
        {
          imageSrc: require('@/assets/seia.jpg'),
          title: '당신에게 필요한 금융 상품을 찾아보세요!',
          description: '42개의 예금 상품과 58개의 적금 상품이 있습니다.',
          nextrouter: 'finlife'
        },
        {
          imageSrc: require('@/assets/ratecalculcarousel.png'),
          title: '환율 정보가 필요하신가요?',
          description: '주요 국가 화폐 간의 환율 계산을 간단하게!',
          nextrouter: 'ratecalcul'
        },
        {
          imageSrc: require('@/assets/logo.png'),
          title: '다른 사람들은 어떻게 자산 관리를 할까?',
          description: '다른 유저들과 소통해보세요!',
          nextrouter: 'community'
        },
      ],
      activeIndex: 0,
      carouselTarget: "#carouselIndicators",
    }
  },
  mounted() {
    setInterval(() => {
      this.activeIndex = (this.activeIndex + 1) % this.carouselItems.length;
    }, 8000);
  },
  computed: {
    ...mapGetters(['isLogin']),
    ...mapGetters(['getUserInfo']),
    announcearticles() {
      return this.$store.getters.anno_sendArticles.slice(-5)
    },
    ...mapGetters(['getUserInfo']),
    newsarticles() {
      return this.$store.getters.news_sendArticles.slice(-5)
    },
    userarticles() {
      return this.$store.getters.sendArticles.slice(-5)
    }
  },
  created() {
    this.getAnnoArticles()
    this.getNewsArticles()
    this.getArticles()
  },
  methods: {
    moveRouter(nextrouter){
      if (nextrouter === 'finlife'){
        this.$router.push('/finlife')
      } else if (nextrouter === 'ratecalcul') {
        this.$router.push('/ratecalcul')
      }else {
        this.$router.push('/community/userboard')
      }
    },
    getAnnoArticles() {
      this.$store.dispatch('anno_getGet')

    },
    getNewsArticles() {
      this.$store.dispatch('news_getGet')
    },
    getArticles() {
      this.$store.dispatch('getGet')
    },
  }
}
</script>

<style scoped>

.back {
  width: 100%;
}

.container {
  margin-top: 10px;
  display: flex;
  flex-wrap: wrap;
  overflow: hidden;
  justify-content: center;
  /* align-items: center; */
}


.row {
  width: 100%;
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;

}

.col {
  width: 30%;
  padding: 10px;
}

.carousel-box {
  width: 100%;
  border: 1px solid black;
  border-radius: 10px;
  height: 500px;
}

.carousel-content {
  margin-top: 50%;
  transform: translateY(-50%);
  white-space: nowrap;
}

.imgcontainer{
  margin-top: auto;
  margin-bottom: auto;
}
</style>
