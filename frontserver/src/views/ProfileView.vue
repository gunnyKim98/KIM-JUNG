<template>
  <div class="container">
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
        
        <p style="margin-left: 30px;">나이 : {{ getUserInfo.age }}</p>
        <p style="margin-left: 30px;">성별 : {{ getUserInfo.sex == 'male' ? '남자' : '여자' }}</p>
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
                <div v-if="getUserInfo.my_deposit.length">
                  <b-card title="가입상품 - 예금" class="mb-3" style="height:254px;" >
                    <div style="font-size:15px;" v-for="(item,idx) in getUserInfo.my_deposit" :key="idx">
                      <p style="margin-bottom:3px"> {{idx+1}}. <a @click="showProductDetail(item.title)" style="cursor:pointer;">{{ item.title }}</a> ({{item.cost}}만원)</p> 
                      <p> -> <a @click="showProductChart(item.title)" style="cursor:pointer;">금리확인</a></p>
                    </div>
                  </b-card>
                </div>
                <div v-else>
                  <b-card title="가입상품 - 예금" class="mb-3" style="height:254px;" >
                    <h5 class="text-center" style="margin-top: 100px"> 가입한 상품이 없습니다.</h5>
                  </b-card>
                </div>
              
              </div>
              <div class="col-md-6">
                <div v-if="getUserInfo.my_saving.length">
                  <b-card title="가입상품 - 적금" class="mb-3" style="height:254px">
                    <div style="font-size:15px;" v-for="(item,idx) in getUserInfo.my_saving" :key="idx">
                      <p style="margin-bottom: 3px;">{{idx+1}}. <a @click="showProductDetail(item.title)" style="cursor:pointer;">{{ item.title }}</a> ({{item.cost}}만원)</p>
                      <p> -> <a @click="showProductChart(item.title)" style="cursor:pointer;">금리확인</a></p>
                    </div>
                  </b-card>
                </div>
                <div v-else>
                  <b-card title="가입상품 - 적금" class="mb-3" style="height:254px;" >
                    <h5 class="text-center" style="margin-top: 100px"> 가입한 상품이 없습니다.</h5>
                  </b-card>
                </div>
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
                <b-card title="추천 예금 상품(나이)" class="mb-3" style="height:254px">
                  <p v-for="(item, idx) in joinDepositAge" :key="idx">
                    {{idx+1}}. <a @click="showProductDetail(item.상품명)" style="cursor:pointer;">{{ item.상품명 }}</a>
                  </p>
                </b-card>
              </div>
              <div class="col-md-6">
                <b-card title="추천 예금 상품(소득)" class="mb-3" style="height:254px">
                  <p v-for="(item, idx) in joinDepositEarn" :key="idx">
                    {{idx+1}}. <a @click="showProductDetail(item.상품명)" style="cursor:pointer;">{{ item.상품명 }}</a>
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
                <b-card title="추천 적금 상품(나이)" class="mb-3" style="height:254px">
                  <p v-for="(item, idx) in joinSavingAge" :key="idx">
                    {{idx+1}}. <a @click="showProductDetail(item.상품명)" style="cursor:pointer;">{{ item.상품명 }}</a>
                  </p>
                </b-card>
              </div>
              <div class="col-md-6">
                <b-card title="추천 적금 상품(소득)" class="mb-3" style="height:254px">
                  <p v-for="(item, idx) in joinSavingEarn" :key="idx">
                    {{idx+1}}. <a @click="showProductDetail(item.상품명)" style="cursor:pointer;">{{ item.상품명 }}</a>
                  </p>
                </b-card>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>

      <div>
      <b-modal v-model="showChart" title="금리정보" >
        <template v-if="selectedProduct">
          <RateChart :selectedProduct="selectedProduct"/>
        </template>
        <template #modal-footer>
          <b-button variant="primary" @click="modalClose">확인</b-button>
        </template>
      </b-modal>
      </div>

        <div>
          <b-modal v-model="showModal" title="상품 정보" >
          <template v-if="selectedProduct">
          <p style="font-weight: bold;">*상품명*</p>
          <p>{{ selectedProduct.상품정보.fin_prdt_nm }}</p>
          <br>
          <p style="font-weight: bold;">*은행명*</p>
          <p>
            <a href="http://localhost:8080/searchmap" @click="searchBank(selectedProduct.상품정보.kor_co_nm)">
              {{ selectedProduct.상품정보.kor_co_nm }}
            </a>
          </p>
          <br>
          <div>
            <p style="font-weight: bold;">*기타 정보*</p>
            <div v-for="item in selectedProductEtcnote" :key="item.id">
              <p>{{ item }}</p>
            </div>
          </div>
          <br>
          <p style="font-weight: bold;">*이자정보*</p>
          <div v-if="selectedProduct['6개월']==='상품정보없음'">
            <p>6개월 : 해당 상품은 6개월 금리 상품이 없습니다.</p>
          </div>
          <div v-else>
            <p>6개월 : 저축 금리 - {{ selectedProduct['6개월'].intr_rate }}({{ selectedProduct['6개월'].intr_rate_type_nm }})</p>
            <p>6개월 : 최고 우대 금리 - {{ selectedProduct['6개월'].intr_rate2 }}({{ selectedProduct['6개월'].intr_rate_type_nm }})</p>
          </div>

          <div v-if="selectedProduct['12개월']==='상품정보없음'">
            <p>12개월 : 해당 상품은 12개월 금리 상품이 없습니다.</p>
          </div>
          <div v-else>
            <p>12개월 : 저축 금리 - {{ selectedProduct['12개월'].intr_rate }}({{ selectedProduct['12개월'].intr_rate_type_nm }})</p>
            <p>12개월 : 최고 우대 금리 - {{ selectedProduct['12개월'].intr_rate2 }}({{ selectedProduct['12개월'].intr_rate_type_nm }})</p>
          </div>

          <div v-if="selectedProduct['24개월']==='상품정보없음'">
            <p>24개월 : 해당 상품은 24개월 금리 상품이 없습니다.</p>
          </div>
          <div v-else>
            <p>24개월 : 저축 금리 - {{ selectedProduct['24개월'].intr_rate }}({{ selectedProduct['24개월'].intr_rate_type_nm }})</p>
            <p>24개월 : 최고 우대 금리 - {{ selectedProduct['24개월'].intr_rate2 }}({{ selectedProduct['24개월'].intr_rate_type_nm }})</p>
          </div>

          <div v-if="selectedProduct['36개월']==='상품정보없음'">
            <p>36개월 : 해당 상품은 36개월 금리 상품이 없습니다.</p>
          </div>
          <div v-else>
            <p>36개월 : 저축 금리 - {{ selectedProduct['36개월'].intr_rate }}({{ selectedProduct['36개월'].intr_rate_type_nm }})</p>
            <p>36개월 : 최고 우대 금리 - {{ selectedProduct['36개월'].intr_rate2 }}({{ selectedProduct['36개월'].intr_rate_type_nm }})</p>
          </div>
        </template>
        <template #modal-footer>
          <b-button variant="primary" @click="modalClose">확인</b-button>
        </template>

      </b-modal>
    </div>


  </div>

</template>

<script>
import {mapGetters} from "vuex";
import RateChart from '@/components/Profile/RateChart.vue'

export default {
  name: "ProfileView",
  data() {
    return {
      showModal: false,
      selectedProduct: null,
      selectedProductEtcnote: null,
      showChart: false,
      chartList: null
    }
  },
  components:{
    RateChart
  },
  computed: {
    ...mapGetters(['getUserInfo']),
    ...mapGetters(['getDepositList']),
    ...mapGetters(['getSavingList']),
    ...mapGetters(['joinDepositAge']),
    ...mapGetters(['joinDepositEarn']),
    ...mapGetters(['joinSavingAge']),
    ...mapGetters(['joinSavingEarn']),
  },
  created() {
    this.$store.dispatch('savingData')
        .then(() => this.$store.dispatch('savingOption'))
        .then(() => this.databaseSavingInfo())
    this.$store.dispatch('depositData')
        .then(() => this.$store.dispatch('depositOption'))
        .then(() => this.databaseDepositInfo())
    this.$store.dispatch('getJoinDepositAge')
    this.$store.dispatch('getJoinDepositEarn')
    this.$store.dispatch('getJoinSavingAge')
    this.$store.dispatch('getJoinSavingEarn')
  },
  methods: {
    databaseSavingInfo() {
      this.info_save = this.$store.state.savings.databaseSavingInfo
      this.option_save = this.$store.state.savings.databaseSavingOption
      this.$store.dispatch('makeSavingsList')
          .then(() => this.savingslist = this.$store.state.savings.savingsList)
    },
    databaseDepositInfo() {
      this.info_depo = this.$store.state.deposit.databaseDepositInfo
      this.option_deposit = this.$store.state.deposit.databaseDepositOption
      this.$store.dispatch('makeDepositList')
          .then(() => this.depositlist = this.$store.state.deposit.depositList)
    },
    moveEditProfile() {
      this.$router.push('/editprofile')
    },
    showProductDetail(title) {
 
      let product = []
      for (let i of this.getDepositList){
        if (i.상품정보.fin_prdt_nm == title){
          product = i
        }
      }
      for (let i of this.getSavingList){
        if (i.상품정보.fin_prdt_nm == title){
          product = i
        }
      }
      this.selectedProduct = product;
      this.showModal = true;
      this.selectedProductEtcnote = product.상품정보.etc_note.split('\n')
    },
    showProductChart(title){
      console.log('title')
      let product = []
      for (let i of this.getDepositList){
        if (i.상품정보.fin_prdt_nm == title){
          product = i
        }
      }
      for (let i of this.getSavingList){
        if (i.상품정보.fin_prdt_nm == title){
          product = i
        }
      }
      this.selectedProduct = product;
      this.showChart = true;

    },
    modalClose(){
      this.showModal = false
      this.showChart = false
    },
  }
}
</script>

<style scoped>
.container {
  width: 800px;
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