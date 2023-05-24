import axios from 'axios'
const baseURL = 'http://127.0.0.1:8000'

const savingURL = 'finlife/saving-products'


const savings = {
  state:{
    databaseSavingInfo: [],
    databaseSavingOption: [],
    savingsList: []
  },
  getters:{

  },
  mutations:{
    SAVING_PRODUCTS(state, data) {
      state.databaseSavingInfo = data
    },
    
    SAVING_OPTIONS(state, data) {
      for (let i=0; i<data.length; i++){
        if (data[i].intr_rate === 0){
          data[i].intr_rate = ' - '
        }
        if (data[i].intr_rate2 === 0){
          data[i].intr_rate2 = ' - '
        }
      }
      state.databaseSavingOption = data
    },

    MAKE_SAVINGS_LIST(state){
      state.savingsList = []
      for (let i=0; i<state.databaseSavingInfo.length; i++){
        let tempObject = {'상품정보': state.databaseSavingInfo[i], '6개월': '상품정보없음','12개월': '상품정보없음','24개월': '상품정보없음','36개월': '상품정보없음'}
        for (let j=0; j<state.databaseSavingOption.length; j++){
          if (state.databaseSavingOption[j]['fin_prdt_cd'] == tempObject['상품정보']['id']){
            if(state.databaseSavingOption[j]['save_trm'] == 6){
              tempObject['6개월'] = state.databaseSavingOption[j]
            } else if (state.databaseSavingOption[j]['save_trm'] == 12){
                tempObject['12개월'] = state.databaseSavingOption[j]
            } else if (state.databaseSavingOption[j]['save_trm'] == 24){
                tempObject['24개월'] = state.databaseSavingOption[j]
            } else if (state.databaseSavingOption[j]['save_trm'] == 36){
              tempObject['36개월'] = state.databaseSavingOption[j]
            }
          }
        }
        state.savingsList.push(tempObject)
      }
    }
  },
  actions:{
    savingData(context) {
      axios({
        method: 'get',
        url: `${baseURL}/${savingURL}/`,
      })
          .then((res) => {
            context.commit('SAVING_PRODUCTS', res.data)

          })
          .catch((err) => {
            console.log(err)
          })
    },
    savingOption(context) {
      axios({
        method: 'get',
        url: `${baseURL}/finlife/saving-product-options/`,
      })
          .then((res) => {
            context.commit('SAVING_OPTIONS', res.data)
          })
          .catch((err) => {
            console.log(err)
          })
    },
    makeSavingsList(context){
      context.commit('MAKE_SAVINGS_LIST')
    }
  },
}

export default savings