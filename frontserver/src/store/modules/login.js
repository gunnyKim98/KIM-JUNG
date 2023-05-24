import axios from 'axios'
import router from "@/router"


const baseURL = 'http://127.0.0.1:8000'

const login = {

  state:{
    token: null,
    errorMessage: [],
    userInfo: [],
  },
  getters:{
    isLogin(state) {
      return !!state.token
    },
    getUserInfo(state) {
      return state.userInfo
    },
  },
  mutations:{
    CHANGE_ERROR_MESSAGE(state, message) {
      state.errorMessage = message
    },
    SAVE_TOKEN(state, token) {
      state.token = token
    },
    RESET_TOKEN(state) {
      state.token = null
      state.userInfo = []
      localStorage.removeItem('token')
      localStorage.removeItem('userInfo')
      router.replace({ name: 'LogInView' })
    },
    PROFILE_DETAIL(state, data) {
      state.userInfo = data
    },
  },
  actions:{
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      // const email = payload.email
      const nickname = payload.nickname
      const age = payload.age
      const sex = payload.sex
      const earn = payload.earn

      axios({
        method: 'post',
        url: `${baseURL}/accounts/signup/`,
        data: {
          username, password1, password2, nickname, age, sex, earn, //email
        }
      })
          .then((res) => {
            console.log(res)
            const password = password1
            const payload = {
              username, password
            }
            context.dispatch('login', payload)
          })
          .catch(err => {
            // console.log(err)
            const errMSG = []
            Object.entries(err.response.data).forEach(([key, value]) => {
              // console.log(`${key}: ${value}`)
              let MSG = `${key}: ${value} \n`
              errMSG.push(MSG)
              errMSG.push('\n')
            })
            alert(errMSG)
          })
    },

    login(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${baseURL}/accounts/login/`,
        data: {
          username, password
        }
      })
          .then((res) => {
            context.commit('SAVE_TOKEN', res.data.key)
            console.log(res.data.key)
            context.dispatch('profileDetail', res.data.key)
            router.push('/')
          })
          .catch((err) =>
          {
            console.log(err)
            context.commit('CHANGE_ERROR_MESSAGE', '잘못된 로그인 정보입니다. 다시 입력하세요')
            alert(this.state.errorMessage)
          })
    },
    profileDetail(context) {
      const token = context.state.token
      console.log(token)
      axios({
        method: 'get',
        url: `${baseURL}/users/`,
        data: {
        },
        headers: {
          Authorization: `Token ${ token }`
        }
      })
          .then((res) => {
            console.log(res)
            context.commit('PROFILE_DETAIL', res.data)
          })
          .catch((err) => console.log(err))
    },
    logout(context) {
      axios({
        method: 'post',
        url: `${baseURL}/accounts/logout/`,
        data: {
        }
      })
          .then((res) => {
            console.log(res)
            context.commit('RESET_TOKEN')
          })
          .catch((err) => console.log(err))
    },

  },
}

export default login