import axios from 'axios'
const baseURL = 'http://127.0.0.1:8000'

const depositURL = 'finlife/deposit-products'

const deposit = {
  state:{
    databaseDepositInfo: [],
    databaseDepositOption: [],
    depositList: []
  },
  getters:{
    getDepositList(state){
      return state.depositList
    }
  },
  mutations:{
    DEPOSIT_PRODUCTS(state, data) {
      state.databaseDepositInfo = data
    },
    DEPOSIT_OPTIONS(state, data) {
      state.databaseDepositOption = data
    },
    MAKE_DEPOSIT_LIST(state){
      state.depositList = []
      for (let i=0; i<state.databaseDepositInfo.length; i++){
        let tempObject = {'상품정보': state.databaseDepositInfo[i], '6개월': '상품정보없음','12개월': '상품정보없음','24개월': '상품정보없음','36개월': '상품정보없음'}
        for (let j=0; j<state.databaseDepositOption.length; j++){
          if (state.databaseDepositOption[j]['fin_prdt_cd'] == tempObject['상품정보']['id']){
            if(state.databaseDepositOption[j]['save_trm'] == 6){
              tempObject['6개월'] = state.databaseDepositOption[j]
            } else if (state.databaseDepositOption[j]['save_trm'] == 12){
              tempObject['12개월'] = state.databaseDepositOption[j]
            } else if (state.databaseDepositOption[j]['save_trm'] == 24){
              tempObject['24개월'] = state.databaseDepositOption[j]
            } else if (state.databaseDepositOption[j]['save_trm'] == 36){
              tempObject['36개월'] = state.databaseDepositOption[j]
            }
          }
        }
        state.depositList.push(tempObject)
      }

    }
  },
  actions:{
    depositData(context) {
      axios({
        method: 'get',
        url: `${baseURL}/${depositURL}/`,
      })
          .then((res) => {
            context.commit('DEPOSIT_PRODUCTS', res.data)
          })
          .catch((err) => {
            console.log(err)
          })
    },
    depositOption(context) {
      axios({
        method: 'get',
        url: `${baseURL}/finlife/deposit-product-options/`,
      })
          .then((res) => {
            context.commit('DEPOSIT_OPTIONS', res.data)
            context.dispatch('makeDepositList')
          })
          .catch((err) => {
            console.log(err)
          })
    },
    makeDepositList(context){
      context.commit('MAKE_DEPOSIT_LIST')
    }
  },
}

export default deposit