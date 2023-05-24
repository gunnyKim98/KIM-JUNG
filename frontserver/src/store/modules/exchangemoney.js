import axios from 'axios'
// const baseURL = 'http://127.0.0.1:8000'

const exchangemoney = {
  state:{
    exchangeMoney: [],
  },
  getters:{

  },
  mutations:{

    EXCHANGE_MONEY(state, data) {
      state.exchangeMoney = data
    },

  },
  actions:{
    exchangeMoney(context) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/finlife/exchange/`,
      })
        .then((res) => {
          context.commit('EXCHANGE_MONEY', res.data)
          console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}

export default exchangemoney