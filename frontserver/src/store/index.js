import Vue from 'vue'
import Vuex from 'vuex'
// import axios from 'axios'


Vue.use(Vuex)
// const baseURL = 'http://127.0.0.1:8000'


import finlife from './modules/finlife'
import login from './modules/login'
import searchmap from './modules/searchmap'
import exchangemoney from './modules/exchangemoney'
import deposit from './modules/deposit'
import savings from './modules/savings'
import createPersistedState from "vuex-persistedstate";
import newsboard from "@/store/modules/newsboard";
import userboard from "@/store/modules/userboard";
import announcementboard from "@/store/modules/announcementboard";

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      reducer: (state) => ({
        login: state.login,
        // 현재 login 모듈만 로컬 스토리지에 저장
      }),
    }),
  ],
  state: {
  },
  getters: {

  },
  mutations: {

  },
  actions: {
    
  },
  modules: {
    finlife,
    login,
    searchmap,
    exchangemoney,
    deposit,
    savings,
    userboard,
    announcementboard,
    newsboard,
  }
})
