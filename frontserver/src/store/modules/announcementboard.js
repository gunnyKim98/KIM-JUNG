import axios from 'axios'
const baseURL = 'http://127.0.0.1:8000'

const announcementboard = {
  state:{
    anno_articles: [],
    anno_fetched: [],
  },
  getters:{
    anno_sendArticles(state) {
      return state.anno_articles
    }
  },
  mutations:{
    ANNO_GET_ARTICLES(state, articles) {
      state.anno_articles = articles
    },
    ANNO_SET_FETCHED(state, data) {
      state.anno_fetched = data
    }
  },
  actions:{
    anno_getGet(context) {
      const token = context.rootState.login.token
      console.log(token)
      axios({
        method: 'get',
        url: `${baseURL}/articles/announce/`,
        headers: {
          Authorization: `Token ${ token }`
        }
      })
          .then((res) => {
            console.log(res.data)
            context.commit('ANNO_GET_ARTICLES', res.data)
          })
          .catch((err) => {
            console.log(err)
          })
    },
  },

}

export default announcementboard