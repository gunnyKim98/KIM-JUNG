<template>
  <div>
    <b-modal v-model="modalshow" title="환율 정보 서비스 이용 안내">
      <p>평일 오전 10시~18시에 이용가능합니다.</p>
      <p>주말에는 서비스되지 않습니다.</p>
      <template #modal-footer>
        <b-button variant="primary" @click="modalClose">확인</b-button>
      </template>
    </b-modal>

    <div>

      <RateCalculator :ratelist="ratelist" :selectBoxText="selectBoxText"/>
      <hr>
      <RateList :ratelist="ratelist"/>
    </div>
  </div>
</template>

<script>
import RateCalculator from '@/components/RateCalcul/RateCalculator.vue'
import RateList from '@/components/RateCalcul/RateList.vue'

export default {
  name:'RateCalculView',
  components:{
    RateCalculator,
    RateList
  },
  data(){
    return{
      ratelist: null,
      selectBoxText: [],
      modalshow: true
    }
  },
  created(){
    this.loadlist()
        .then(() => this.makeselectbox())
        .catch(error => {
          console.error(error);
        });
  },
  computed:{

  },
  methods:{
    loadlist() {

      return this.$store.dispatch('exchangeMoney')
          .then(() => {
            this.ratelist = this.$store.state.exchangemoney.exchangeMoney;
          })
    },
    makeselectbox(){
      for(let i = 0; i< this.ratelist.length; i++){
        this.selectBoxText.push(this.ratelist[i].country + ' / ' + this.ratelist[i].currency)
      }
    },
    modalClose(){
      this.loadlist()
          .then(() => this.makeselectbox())
      this.modalshow = false

    }
  }
}
</script>

<style>
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
</style>