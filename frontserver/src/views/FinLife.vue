<template>
  <div>
    <div class="container">
      <div v-if="depositIsActive">
        <h2>예금 상품 정보</h2>
      </div>
      <div v-else>
        <h2>적금 상품 정보</h2>
      </div>
      <p>이자율 정보는 "저축금리(최고우대금리)"로 표시됩니다.</p>
      <p>상품명을 클릭하면 자세한 정보를 볼 수 있습니다. </p>
      <p>은행명을 클릭하면 지도 정보를 볼 수 있습니다.</p>
      <p></p>
    </div>

    <div v-if="depositIsActive" class="container">
      <button disabled class="btn btn-outline-dark" @click="databaseDepositInfo">예금 정보</button> |
      <button class="btn btn-outline-dark" @click="databaseSavingInfo">적금 정보</button>
    </div>
     <div v-else class="container">
      <button class="btn btn-outline-dark" @click="databaseDepositInfo">예금 정보</button> |
      <button disabled class="btn btn-outline-dark" @click="databaseSavingInfo">적금 정보</button>
    </div>

    <hr>
    <div v-if="depositIsActive">
      <FinlifeDeposit :info_depo="this.$store.state.deposit.databaseDepositInfo" :option_deposit="this.$store.state.deposit.databaseDepositOption" :depositlist="this.$store.state.deposit.depositList"/>
    </div>

    <div v-if="saveIsActive">
      <FinlifeSavings :info_save="this.$store.state.savings.databaseSavingInfo" :option_save="this.$store.state.savings.databaseSavingOption" :savingslist="this.$store.state.savings.savingsList"/>
    </div>
  </div>
</template>

<script>
import FinlifeDeposit from '@/components/Finlife/FinlifeDeposit.vue'
import FinlifeSavings from '@/components/Finlife/FinlifeSavings.vue'

export default {
  name: "FinLife",
  data() {
    return {
    
      depositIsActive: true,
      saveIsActive: false,

    }
  },
  components: {
    FinlifeDeposit,
    FinlifeSavings
  },
  created() {
    this.$store.dispatch('savingData')
        .then(() => this.$store.dispatch('savingOption'))
    this.$store.dispatch('depositData')
        .then(() => this.$store.dispatch('depositOption'))  
  },
  mounted(){
    this.info_depo = this.$store.state.savings.databaseSavingInfo
  },
  methods: {
    databaseSavingInfo() {
      this.saveIsActive = true
      this.depositIsActive = false
    
    },
    databaseDepositInfo() {
      this.saveIsActive = false
      this.depositIsActive = true
      
    }
  }

}
</script>

<style scoped>
.productmain{
  max-width: 80%;
}

.container {
  flex-wrap: wrap;
  max-width: 1500px;
  overflow: hidden;

  text-align: center;
}

.container p {
  white-space: pre-line;
}
</style>