import axios from "axios";

const baseURL = 'http://127.0.0.1:8000'

const finlife = {
  state:{
    recommend_deposit_age: [],
    recommend_deposit_earn: [],
    recommend_saving_age: [],
    recommend_saving_earn: []
  },
  getters:{
    joinDepositAge(state) {
      const result = state.recommend_deposit_age.sort((item1, item2) => item1['나이차'] - item2['나이차']).slice(0,5)
           
      return result
    },
    joinDepositEarn(state) {
      const result = state.recommend_deposit_earn.sort((item1, item2) => item1['소득차'] - item2['소득차']).slice(0,5)
      return result
    },
    joinSavingAge(state) {
      const result = state.recommend_saving_age.sort((item1, item2) => item1['나이차'] - item2['나이차']).slice(0,5)
      return result
    },
    joinSavingEarn(state) {
      const result = state.recommend_saving_earn.sort((item1, item2) => item1['소득차'] - item2['소득차']).slice(0,5)
      return result
    },

  },
  mutations:{
    GET_DEPOSIT_AGE(state, data) {
      state.recommend_deposit_age = data
    },
    GET_DEPOSIT_EARN(state, data) {
      state.recommend_deposit_earn = data
    },
    GET_SAVING_AGE(state, data) {
      state.recommend_saving_age = data
    },
    GET_SAVING_EARN(state, data) {
      state.recommend_saving_earn = data
    },
  },
  actions:{
    getJoinDepositAge(context) {
      const token = context.rootState.login.token
      axios({
        method: 'GET',
        url: `${baseURL}/users/search/deposit/${context.rootState.login.userInfo.id}/age/`,
        data: {

        },
        headers: {
          Authorization: `Token ${ token }`
        }
      })
          .then((res) => {
            console.log(res)
            context.commit('GET_DEPOSIT_AGE', res.data)
          })
          .catch((err) => {
            console.log(err)
          })
    },
    getJoinDepositEarn(context) {
      const token = context.rootState.login.token
      axios({
        method: 'GET',
        url: `${baseURL}/users/search/deposit/${context.rootState.login.userInfo.id}/earn/`,
        data: {

        },
        headers: {
          Authorization: `Token ${ token }`
        }
      })
          .then((res) => {
            console.log(res)
            context.commit('GET_DEPOSIT_EARN', res.data)
          })
          .catch((err) => {
            console.log(err)
          })
    },
    getJoinSavingAge(context) {
      const token = context.rootState.login.token
      axios({
        method: 'GET',
        url: `${baseURL}/users/search/saving/${context.rootState.login.userInfo.id}/age/`,
        data: {

        },
        headers: {
          Authorization: `Token ${ token }`
        }
      })
          .then((res) => {
            console.log(res)
            context.commit('GET_SAVING_AGE', res.data)
          })
          .catch((err) => {
            console.log(err)
          })
    },
    getJoinSavingEarn(context) {
      const token = context.rootState.login.token
      axios({
        method: 'GET',
        url: `${baseURL}/users/search/saving/${context.rootState.login.userInfo.id}/earn/`,
        data: {

        },
        headers: {
          Authorization: `Token ${ token }`
        }
      })
          .then((res) => {
            console.log(res)
            context.commit('GET_SAVING_EARN', res.data)
          })
          .catch((err) => {
            console.log(err)
          })
    }
  },
}

export default finlife