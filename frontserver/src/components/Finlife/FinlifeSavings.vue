<template>
  <div>
    <div >
      <div class="checkbox-group container">
        저축 기간 :
        <div class="checkbox-item" v-for="(item, idx) in saveterm" :key="idx">
          <input type="checkbox" :value="item" v-model="selectedsaveterm">
          <label>{{ item }}</label>
        </div>

        <div class="checkbox-item">
          <input type="checkbox" @change="allSaveTerm">
          <label>모두 선택</label>
        </div>

      </div>
      <div class="checkbox-group container">
        가입 방법 :
        <div class="checkbox-item" v-for="(item, idx) in joinway" :key="idx">
          <input type="checkbox" :value="item" v-model="selectedjoinway">
          <label>{{ item }}</label>
        </div>
        <div class="checkbox-item">
          <input type="checkbox" @change="allJoinWay">
          <label>모두 선택</label>
        </div>
      </div>

      <div class="checkbox-group container">
        <h6 style="margin: 0;">은행 : </h6>
        <select style="margin-left: 10px; margin-right: 10px;" v-model="selectedbankname">
          <option v-for="(item, idx) in bankname" :value="item" :key="idx">{{ item }}</option>
        </select>

        <button class="btn btn-outline-dark" @click="makeSearchList">검색</button>
      </div>


    </div>
    <hr>
    <div v-if="!searchstate" class="table-container">
      <table class="table" style="white-space: nowrap; width:1350px;">
        <thead>
        <tr>
          <th style="width: 5%">번호</th>
          <th style="width: 20%">상품명</th>
          <th style="width: 15%">은행명</th>
          <th style="width: 20%">가입 방법</th>
          <th style="width: 10%">6개월</th>
          <th style="width: 10%">12개월</th>
          <th style="width: 10%">24개월</th>
          <th style="width: 10%">36개월</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(item, idx) in savingslist" :key="item.id">
          <td>{{ idx + 1 }}</td>
          <td @click="showProductDetail(item)" style="cursor:pointer;">{{ item.상품정보.fin_prdt_nm }}</td>
          <td><a style="color:black;" href="http://localhost:8080/searchmap" @click="searchBank(item.상품정보.kor_co_nm)"> {{item.상품정보.kor_co_nm}}</a></td>
          <td>{{ item.상품정보.join_way }}</td>
          <td v-if="item['6개월']==='상품정보없음'">{{ item['6개월'] }}</td>
          <td v-else>{{ item['6개월'].intr_rate }}({{ item['6개월'].intr_rate2 }})</td>
          <td v-if="item['12개월']==='상품정보없음'">{{ item['12개월'] }}</td>
          <td v-else>{{ item['12개월'].intr_rate }}({{ item['12개월'].intr_rate2 }})</td>
          <td v-if="item['24개월']==='상품정보없음'">{{ item['24개월'] }}</td>
          <td v-else>{{ item['24개월'].intr_rate }}({{ item['24개월'].intr_rate2 }})</td>
          <td v-if="item['36개월']==='상품정보없음'">{{ item['36개월'] }}</td>
          <td v-else>{{ item['36개월'].intr_rate }}({{ item['36개월'].intr_rate2 }})</td>
        </tr>
        </tbody>
      </table>
    </div>
    <div v-if="searchstate" class="table-container">
      <div v-if="searchlist.length===0">
        <h1>검색 결과가 없습니다.</h1>
      </div>
      <div v-else>
        <table class="table" style="white-space: nowrap; width:1350px;">
          <thead>
          <tr>
            <th style="width: 5%">번호</th>
            <th style="width: 20%">상품명</th>
            <th style="width: 15%">은행명</th>
            <th style="width: 20%">가입 방법</th>
            <th style="width: 10%">6개월</th>
            <th style="width: 10%">12개월</th>
            <th style="width: 10%">24개월</th>
            <th style="width: 10%">36개월</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(item, idx) in searchlist" :key="item.id">
            <td>{{ idx + 1 }}</td>
            <td @click="showProductDetail(item)" style="cursor:pointer;">{{ item.상품정보.fin_prdt_nm }}</td>
            <td><a style="color:black;" href="http://localhost:8080/searchmap" @click="searchBank(item.상품정보.kor_co_nm)"> {{item.상품정보.kor_co_nm}}</a></td>
            <td>{{ item.상품정보.join_way }}</td>
            <td v-if="item['6개월']==='상품정보없음'">{{ item['6개월'] }}</td>
            <td v-else>{{ item['6개월'].intr_rate }}({{ item['6개월'].intr_rate2 }})</td>
            <td v-if="item['12개월']==='상품정보없음'">{{ item['12개월'] }}</td>
            <td v-else>{{ item['12개월'].intr_rate }}({{ item['12개월'].intr_rate2 }})</td>
            <td v-if="item['24개월']==='상품정보없음'">{{ item['24개월'] }}</td>
            <td v-else>{{ item['24개월'].intr_rate }}({{ item['24개월'].intr_rate2 }})</td>
            <td v-if="item['36개월']==='상품정보없음'">{{ item['36개월'] }}</td>
            <td v-else>{{ item['36개월'].intr_rate }}({{ item['36개월'].intr_rate2 }})</td>
          </tr>
          </tbody>
        </table>
      </div>
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
          <b-button variant="danger" @click="addProductSaving(selectedProduct.상품정보.fin_prdt_nm, selectedProduct.상품정보.kor_co_nm)">등록</b-button>
          <b-button variant="primary" @click="modalClose">확인</b-button>
        </template>

      </b-modal>
    </div>

  </div>
</template>


<script>
import {mapGetters} from "vuex";

export default {
  name: 'FinlifeSavings',
  props:{
    info_save : Array,
    option_save: Array,
    savingslist: Array
  },
  data(){
    return{
      saveterm: ['6개월','12개월','24개월','36개월'],
      selectedsaveterm:  [],
      joinway: ['인터넷', '스마트폰', '전화(텔레뱅킹)', '영업점', '기타'],
      selectedjoinway:  [],
      bankname: ['전체','우리은행','한국스탠다드차타드은행','부산은행','광주은행','제주은행','전북은행','경남은행','중소기업은행','한국산업은행','국민은행','신한은행','농협은행주식회사','하나은행','주식회사 케이뱅크','수협은행','주식회사 카카오뱅크','토스뱅크 주식회사'],
      selectedbankname: '전체',
      searchstate : false,
      searchlist: [],
      allsavetermIsactive: false,
      alljoinwayIsactive: false,
      showModal: false, // 모달 창 표시 여부
      selectedProduct: null, // 선택된 상품 정보
      selectedProductEtcnote: null
    }
  },
  computed: {
    ...mapGetters(['isLogin'])
  },
  methods:{
    makeSearchList(){
      this.searchlist = []
      for (let i=0; i<this.savingslist.length; i++){
        const product_joinway = this.savingslist[i].상품정보.join_way.split(',')
        const product_saveterm = Object.keys(this.savingslist[i]).filter(key => this.savingslist[i][key] !== '상품정보없음');
        const product_bank = this.savingslist[i].상품정보.kor_co_nm

        let joinway_bool = true
        let saveterm_bool = true
        let bank_bool = true

        if (this.selectedjoinway.length != 0){
          joinway_bool = this.selectedjoinway.every(item => product_joinway.includes(item));
        }
        if (this.selectedsaveterm != 0){
          saveterm_bool = this.selectedsaveterm.every(item => product_saveterm.includes(item));
        }
        if (this.selectedbankname != '전체' && product_bank != this.selectedbankname){
          bank_bool = false
        }

        if (joinway_bool && saveterm_bool && bank_bool){
          this.searchlist.push(this.savingslist[i])
        }

        this.searchstate = true

      }
    },
    allSaveTerm(){
      if (this.allsavetermIsactive){
        this.allsavetermIsactive = !this.allsavetermIsactive
        this.selectedsaveterm = []
      } else{
        this.allsavetermIsactive = !this.allsavetermIsactive
        this.selectedsaveterm = this.saveterm
      }
    },
    allJoinWay(){
      if (this.alljoinwayIsactive){
        this.alljoinwayIsactive = !this.alljoinwayIsactive
        this.selectedjoinway = []
      } else{
        this.alljoinwayIsactive = !this.alljoinwayIsactive
        this.selectedjoinway = this.joinway
      }
    },
    showProductDetail(product) {
      this.selectedProduct = product;
      this.showModal = true;
      this.selectedProductEtcnote = product.상품정보.etc_note.split('\n')
    },
    modalClose(){
      this.showModal = false
    },
    searchBank(bank){

      this.$store.dispatch('searchBank', bank)
    },
    addProductSaving(title, bank) {
      if (!this.isLogin){
        alert('로그인이 필요한 서비스입니다.')
        this.$router.push('/login')
        return
      }
      console.log(title)
      console.log(bank)
      this.$router.push(`/addProduct_saving/${title}/${bank}/`)
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;}

.checkbox-group {
  display: flex;
}

.checkbox-item {
  margin: 10px;

}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background-color: white;
  padding: 20px;
}

.table-container {
  display: flex;
  justify-content: center;
  text-align: center;
}
</style>