import axios from 'axios'
const baseURL = 'http://127.0.0.1:8000'

const newsboard = {
  state:{
    news_articles: [],
    news_fetched: [],
    news_comments: [],
  },
  getters:{
    news_sendArticles(state) {
      return state.news_articles
    },
    news_sendComments(state) {
      return state.news_comments
    },
  },
  mutations:{
    NEWS_GET_ARTICLES(state, articles) {
      state.news_articles = articles
    },
    NEWS_SET_FETCHED(state, data) {
      state.news_fetched = data
    },
    GET_NEWS_COMMENTS(state, data) {
      state.news_comments = data
    }
  },
  actions:{
    news_getGet(context) {
      const token = context.rootState.login.token
      console.log(token)
      axios({
        method: 'get',
        url: `${baseURL}/articles/news/`,
        headers: {
          Authorization: `Token ${ token }`
        }
      })
          .then((res) => {
            console.log(res.data)
            context.commit('NEWS_GET_ARTICLES', res.data)
          })
          .catch((err) => {
            console.log(err)
          })
    },
    news_getComments(context) {
      const token = context.rootState.login.token
      axios({
        method: 'get',
        url: `${baseURL}/articles/news/comments/`,
        headers: {
          Authorization: `Token ${ token }`
        }
      })
          .then((res) => {
            console.log(res.data)
            context.commit('GET_NEWS_COMMENTS', res.data)
          })
          .catch((err) => {
            console.log(err)
          })
    },
  },

}

export default newsboard