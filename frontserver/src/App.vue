<template>
  <div id="app">
    <div>
      <div v-if="isLogin">
        <b-nav tabs>
          <b-nav-item class="nomargin" @click="$router.push('/')"><img  src="@/assets/main/mainlogo.png" alt="" class="img-fluid nomargin"></b-nav-item>
          <b-nav-item class="nomargin" @click="$router.push('/finlife')"><img  src="@/assets/main/productlogo.png" alt="" class="img-fluid nomargin"></b-nav-item>
          <b-nav-item class="nomargin" @click="$router.push('/ratecalcul')"><img  src="@/assets/main/exchangelogo.png" alt="" class="img-fluid nomargin"></b-nav-item>
          <b-nav-item class="nomargin" @click="$router.push('/searchmap')"><img  src="@/assets/main/searchmaplogo.png" alt="" class="img-fluid nomargin"></b-nav-item>
          <b-nav-item class="nomargin" @click="$router.push('/community/userboard')"><img  src="@/assets/main/communitylogo.png" alt="" class="img-fluid nomargin"></b-nav-item>

          <b-col class="text-right">
            <p id="hellouser">안녕하세요 {{ getUserInfo.nickname }} 님!</p>
          </b-col>

          <b-nav-item class="nomargin" @click="$router.push('/profile')"><img  src="@/assets/main/editprofilelogo.png" alt="" class="img-fluid nomargin"></b-nav-item>
          <b-nav-item class="nomargin" @click="logout"><img  src="@/assets/main/signoutlogo.png" alt="" class="img-fluid nomargin"></b-nav-item>
        </b-nav>
      </div>

      <div v-if="!isLogin">
        <b-nav tabs>
          <b-nav-item class="nomargin" @click="$router.push('/')"><img  src="@/assets/main/mainlogo.png" alt="" class="img-fluid nomargin"></b-nav-item>
          <b-nav-item class="nomargin" @click="$router.push('/finlife')"><img  src="@/assets/main/productlogo.png" alt="" class="img-fluid nomargin"></b-nav-item>
          <b-nav-item class="nomargin" @click="$router.push('/ratecalcul')"><img  src="@/assets/main/exchangelogo.png" alt="" class="img-fluid nomargin"></b-nav-item>
          <b-nav-item class="nomargin" @click="$router.push('/searchmap')"><img  src="@/assets/main/searchmaplogo.png" alt="" class="img-fluid nomargin"></b-nav-item>
          <b-nav-item class="nomargin" @click="$router.push('/community/userboard')"><img  src="@/assets/main/communitylogo.png" alt="" class="img-fluid nomargin"></b-nav-item>
          <b-nav-item class="nomargin ml-auto" @click="$router.push('/login')"><img  src="@/assets/main/signinlogo.png" alt="" class="img-fluid nomargin"></b-nav-item>
          <b-nav-item class="nomargin" @click="$router.push('/signup')"><img  src="@/assets/main/signuplogo.png" alt="" class="img-fluid nomargin"></b-nav-item>



        </b-nav>
      </div>
    </div>

    <router-view/>
    <!--footer-->
    <div class="block-header py-3 border-top text-center">
      <div class="container">
        <div class="row">
          <div class="col">
            <div style="white-space: nowrap;">
              <footer>
                <nav>
                  <a href="https://www.ssafy.com/ksp/jsp/swp/swpMain.jsp">SSAFY</a> |
                  <a @click="showCreators" style="cursor:pointer;">Creators</a> |
                  <a @click="showRules" style="cursor:pointer;">이용약관</a>
                </nav>
                <p v-if="CreatorsIsActive">싸피 9기 정도현 & 김주현</p>
                <p v-if="rulesIsActive">현재 이용약관이 없습니다.</p>
                <p>
                  <span>본 사이트의 콘텐츠는 저작권법의 보호를 받는 바 무단 전재, 복사, 배포 등을 금합니다.</span><br/>
                  <span>Copyright &copy; HAPPYHOUSE All Rights Reserved.</span>
                </p>
              </footer>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>


</template>

<script>
import { mapGetters } from "vuex"

export default {
  name: 'App',
  data() {
    return {
      userData: this.getUserInfo,
      CreatorsIsActive: false,
      rulesIsActive: false

    }
  },
  computed: {
    ...mapGetters(['isLogin']),
    ...mapGetters(['getUserInfo'])
  },
  created(){

  },
  mounted() {

  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
    },

    showCreators(){
      this.CreatorsIsActive = !this.CreatorsIsActive
    },
    showRules(){
      this.rulesIsActive = !this.rulesIsActive
    }

  }
}
</script>

<style scoped>
#app {

  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;

}

.bi {
  font-size: 1.7rem;
}
.bi:hover {
  color: dodgerblue;
}
.container {
  font-size: 0.9rem;
  color: #808080;
}

footer {
  width: 100%;
  height: 90px;
}
footer a {
  display: inline-block;
  margin: 0 20px 10px 20px;
  color: #808080;
}
footer a:visited {
  color: #808080;
}
footer p {
  margin-top: 0; margin-bottom: 0;
}
footer p span {
  display: inline-block;
  margin-left: 20px;
}

.nomargin {
  padding: 0;
  margin-top: 0;
  margin-bottom: 0;
  margin-right: 5px;

}

#hellouser {
  margin-top: 40px;
  font-size: 24px;
  font-weight: bold;
  color: #333;

}
</style>