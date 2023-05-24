<template>
  <div class="container">
    {{ getUserInfo }}
    <hr>
    <div>
      <div style="margin-bottom:10px;">
         <a  href="#" @click="$router.push('/')" style="color:green;">홈으로 >></a>
      </div>

      <h3 style="padding: 10px;">닉네임 : {{ getUserInfo.nickname}}</h3>
      <h6 class="text-right">등급: {{
          getUserInfo.is_superuser ? '관리자' :
          getUserInfo.is_staff ? '운영자' :
          '일반유저'
        }}</h6>

      <hr>
      <div class="contentbox">
          <p style="margin-left: 30px;">아이디 : {{ getUserInfo.username }}</p>
          <p style="margin-left: 30px;">이름 : {{ getUserInfo.first_name }} {{ getUserInfo.last_name }}</p>
          <p style="margin-left: 30px;">나이 : {{ getUserInfo.age }}</p>
          <p style="margin-left: 30px;">성별 : {{ getUserInfo.sex == 'male' ? '남자' : '여자' }}</p>
          <p style="margin-left: 30px;">email : {{ getUserInfo.email.length == 0 ? '등록되지 않았습니다.' : getUserInfo.email }}</p>
          <p style="margin-left: 30px;">소득 : {{ getUserInfo.earn }} (만원)</p>
          
        </div>
        <button class="btn btn-outline-dark" style="margin-left: 30px;" @click="moveEditProfile">회원 정보 수정</button>
      <hr>
      <div class="text-right" style="padding:0px;"> 
        <p style="padding:0px;">가입날짜 : {{ getUserInfo?.date_joined.slice(0,4) }}년 {{ getUserInfo?.date_joined.slice(5,7) }}월 {{ getUserInfo?.date_joined.slice(8,10) }}일 </p>
        <p style="padding:0px;">최근 로그인 : {{ getUserInfo?.last_login.slice(0,4) }}년 {{ getUserInfo?.last_login.slice(5,7) }}월 {{ getUserInfo?.last_login.slice(8,10) }}일 {{ getUserInfo?.last_login.slice(11,13) }}시 {{ getUserInfo?.last_login.slice(14,16) }}분</p>
      </div>
      <hr>
      <div>
        <div class="row">
          <div class="col">
            <div class="row">
              <div class="col-md-6">
                <b-card title="가입상품 - 예금" class="mb-3" style="height:254px">
                    <p v-for="(item,idx) in getUserInfo.my_deposit" :key="idx">
                      {{idx+1}}. {{ item.title }}
                    </p>
                </b-card>
              </div>
              <div class="col-md-6">
                <b-card title="가입상품 - 적금" class="mb-3" style="height:254px">
                  <p v-for="(item,idx) in getUserInfo.my_saving" :key="idx">
                      {{idx+1}}. {{ item.title }}
                    </p>
                </b-card>
              </div>
              </div>
            </div>
        </div>
      </div>

      <div>
        <div class="row">
          <div class="col">
            <div class="row">
              <div class="col-md-6">
                <b-card title="추천상품 - 나이" class="mb-3" style="height:254px">
                    <p v-for="(item,idx) in getUserInfo.my_deposit" :key="idx">
                      {{idx+1}}. {{ item.title }}
                    </p>
                </b-card>
              </div>
              <div class="col-md-6">
                <b-card title="추천상품 - 소득" class="mb-3" style="height:254px">
                  <p v-for="(item,idx) in getUserInfo.my_saving" :key="idx">
                      {{idx+1}}. {{ item.title }}
                    </p>
                </b-card>
              </div>
              </div>
            </div>
        </div>
      </div>


    </div>
  </div>

</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "ProfileView",
  data() {
    return {

    }
  },

  computed: {
    ...mapGetters(['getUserInfo'])

  },
  // created() {
  //   this.getProfile()
  // },
  methods: {
    // getProfile() {
    //   this.$store.dispatch('profileDetail')
    // },
    moveEditProfile() {
      this.$router.push('/editprofile')
    }
  }
}
</script>

<style scoped>
.container {
  width: 800px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
}

.contentbox {
  min-height: 300px;
  font-size: 17px;
}
</style>