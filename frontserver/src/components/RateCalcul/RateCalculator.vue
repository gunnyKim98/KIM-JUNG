<template>
  <div class="container">
    
  <b-card style="width: 600px">
    <b-form-group>
      <b-form-select class="selectbox" v-model="selectedText1" @change="makeSelectedCurrency1">
        <option v-for="(item, idx) in selectBoxText" :key="idx" :value="item">{{ item }}</option>
      </b-form-select>
    </b-form-group>
    <div class="table-container">
      <div class="table">
        <table style="width:100%">
          <thead>
            <tr>
              <th style="width: 30%">국가</th>
              <th style="width: 20%">화폐</th>
              <th style="width: 50%">액수 입력</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{{ selectedCountry1 }}</td>
              <td>{{ selectedCurrency1 }}</td>
              <td><b-form-input v-model="inputNumber" type="number"></b-form-input></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </b-card>

  <img class="arrowimage" src="@/assets/rightarrow.png">

  <b-card style="width: 600px">
    <b-form-group>
      <b-form-select class="selectbox" v-model="selectedText2" @change="makeSelectedCurrency2">
        <option v-for="(item, idx) in selectBoxText" :key="idx" :value="item">{{ item }}</option>
      </b-form-select>
    </b-form-group>
    <div class="table-container">
      <div class="table">
        <table style="width:100%">
          <thead>
            <tr>
              <th style="width: 30%">국가</th>
              <th style="width: 20%">화폐</th>
              <th style="width: 50%">{{ inputNumber }} {{ selectedCurrency1 }} 당 </th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{{ selectedCountry2 }}</td>
              <td>{{ selectedCurrency2 }}</td>
              <td>{{ calculResult }} {{ selectedCurrency2 }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </b-card>
</div>
</template>


<script>

// import axios from 'axios'


export default {
  name:'RateCalculator',
  props:{
    ratelist : Array,
    selectBoxText: Array
  },
  data(){
    return{
      selectedText1: '한국 / 원',
      selectedText2: '한국 / 원',
      selectedCountry1: '한국',
      selectedCountry2: '한국',
      selectedCurrency1: '원',
      selectedCurrency2: '원',
      selectedRate1: 1,
      selectedRate2: 1,
      inputNumber: 0
    }
  },
  computed:{
    calculResult(){
      const result = this.inputNumber * (this.selectedRate1 / this.selectedRate2)
      return result.toFixed(3)
    },
  },
  methods:{
    makeSelectedCurrency1(){
      const selectedcountry = this.selectedText1.split(' ')[0]
      
      for (let i of this.ratelist){
        if (i['country'] === selectedcountry){
          this.selectedCountry1 = selectedcountry
          this.selectedCurrency1 = i['currency']
          this.selectedRate1 = i['rate']
        }
      }
    },
    makeSelectedCurrency2(){
      const selectedcountry = this.selectedText2.split(' ')[0]
      
      for (let i of this.ratelist){
        if (i['country'] === selectedcountry){
          this.selectedCountry2 = selectedcountry
          this.selectedCurrency2 = i['currency']
          this.selectedRate2 = i['rate']
        }
      }
    }
  }
}
</script>

<style scoped>
.custom-select {
  width: 150px; /* 원하는 크기로 조정 */
  height: 30px; /* 원하는 크기로 조정 */
  font-size: 16px; /* 원하는 글꼴 크기로 조정 */
}

.container {
  display: flex;
  text-align: center;
  justify-content: center;
  text-align: center;
  flex-wrap: nowrap;
  padding: 10px;
}

.table-container {
    display: flex;
    justify-content: center;
  }

.table {
  width: 100%;
}

.arrowimage{
 width: 100px; 
 height: 100px;
 margin-top: auto;
 margin-bottom: auto;
}

.selectbox{
  width: 200px;
  height: 40px;
}
</style>