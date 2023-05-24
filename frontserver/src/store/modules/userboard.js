// import axios from 'axios'
import axios from "axios";

const baseURL = 'http://127.0.0.1:8000'

const userboard = {
  state:{
    articles: [],
    fetched: [],
    comments: [],
  },
  getters:{
    sendArticles(state) {
      return state.articles
    },
    sendComments(state) {
      return state.comments
    }
  },
  mutations:{
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    SET_FETCHED(state, data) {
      state.fetched = data
    },
    GET_COMMENTS(state, data) {
      state.comments = data
    }
  },
  actions:{
    getGet(context) {
      const token = context.rootState.login.token
      console.log(token)
      axios({
        method: 'get',
        url: `${baseURL}/articles/community/`,
        headers: {
          Authorization: `Token ${ token }`
        }
      })
        .then((res) => {
          console.log(res.data)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getComments(context) {
      const token = context.rootState.login.token
      axios({
        method: 'get',
        url: `${baseURL}/articles/community/comments/`,
        headers: {
          Authorization: `Token ${ token }`
        }
      })
          .then((res) => {
            console.log(res.data)
            context.commit('GET_COMMENTS', res.data)
          })
          .catch((err) => {
            console.log(err)
          })
    },
  },
}

export default userboard