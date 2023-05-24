<template>
  <div>
    <div class="container">
      <h2>예금&적금 상품 정보</h2>
      <p>이자율 정보는 "저축금리(최고우대금리)"로 표시됩니다.</p>
      <p>상품명을 클릭하면 자세한 정보를 볼 수 있습니다. </p>
      <p>은행명을 클릭하면 지도 정보를 볼 수 있습니다.</p>
      <p></p>
    </div>

    <div class="container">
      <button class="btn btn-outline-dark" @click="databaseDepositInfo">예금 정보</button> |
      <button class="btn btn-outline-dark" @click="databaseSavingInfo">적금 정보</button>
    </div>
    <hr>
    <div v-if="depositIsActive">
      <FinlifeDeposit v-if="info_depo && option_deposit" :info_depo="info_depo" :option_deposit="option_deposit" :depositlist="depositlist"/>
    </div>

    <div v-if="saveIsActive">
      <FinlifeSavings v-if="info_save && option_save" :info_save="info_save" :option_save="option_save" :savingslist="savingslist"/>
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
      info_save: null,
      option_save: null,
      info_depo: null,
      option_deposit: null,
      depositIsActive: false,
      saveIsActive: false,
      depositlist: [],
      savingslist: []
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
  methods: {
    databaseSavingInfo() {
      this.saveIsActive = true
      this.depositIsActive = false
      this.info_save = this.$store.state.savings.databaseSavingInfo
      this.option_save = this.$store.state.savings.databaseSavingOption
      this.$store.dispatch('makeSavingsList')
          .then(() => this.savingslist = this.$store.state.savings.savingsList)
    },
    databaseDepositInfo() {
      this.saveIsActive = false
      this.depositIsActive = true
      this.info_depo = this.$store.state.deposit.databaseDepositInfo
      this.option_deposit = this.$store.state.deposit.databaseDepositOption
      this.$store.dispatch('makeDepositList')
          .then(() => this.depositlist = this.$store.state.deposit.depositList)
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