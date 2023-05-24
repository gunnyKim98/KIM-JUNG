import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from "@/views/SignUpView.vue";
import LogInView from "@/views/LogInView.vue";
import FinLife from "@/views/FinLife.vue";
import RateCalculView from "@/views/RateCalculView.vue";
import SearchMapView from "@/views/SearchMapView.vue";
import ProfileView from "@/views/ProfileView.vue";
import CommunityView from "@/views/CommunityView.vue";
import EditProfileView from "@/views/EditProfileView.vue";
import AnnouncementBoard from "@/components/ArticleArea/AnnouncementBoard.vue";
import NewsBoard from "@/components/ArticleArea/NewsBoard.vue";
import UserBoard from "@/components/ArticleArea/UserBoard.vue";
import DetailUserBoard from "@/views/DetailUserBoard.vue";
import CreateUserBoard from "@/views/CreateUserBoard.vue";
import CreateNewsBoard from "@/views/CreateNewsBoard.vue";
import DetailNewsBoard from "@/views/DetailNewsBoard.vue";
import CreateAnnounceBoard from "@/views/CreateAnnounceBoard.vue";
import DetailAnnounceBoard from "@/views/DetailAnnounceBoard.vue";
import AddDepositProduct from "@/views/AddDepositProduct.vue";
import AddSavingProduct from "@/views/AddSavingProduct.vue";
import EditUserArticle from "@/views/EditUserArticle.vue";
import EditNewsArticle from "@/views/EditNewsArticle.vue";
import EditAnnounceArticle from "@/views/EditAnnounceArticle.vue";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/finlife',
    name: 'finlife',
    component: FinLife
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/editprofile',
    name: 'editprofile',
    component: EditProfileView
  },
  {
    path: '/addProduct_deposit/:title/:bank',
    name: 'addProduct_deposit',
    component: AddDepositProduct
  },
  {
    path: '/addProduct_saving/:title/:bank',
    name: 'addProduct_saving',
    component: AddSavingProduct
  },
  {
    path: '/ratecalcul',
    name: 'ratecalcul',
    component: RateCalculView
  },
  {
    path: '/searchmap',
    name: 'searchmap',
    component: SearchMapView

  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },

  {
    path: '/community/announce',
    name: 'announce',
    component: AnnouncementBoard
  },
  {
    path: '/community/announce/create',
    name: 'creatannounce',
    component: CreateAnnounceBoard
  },
  {
    path: '/community/announce/:id',
    name: 'detailannounce',
    component: DetailAnnounceBoard
  },
  {
    path: '/community/announce/edit/:id',
    name: 'editAnnounceArticle',
    component: EditAnnounceArticle
  },
  {
    path: '/community/newsboard',
    name: 'newsboard',
    component: NewsBoard
  },
  {
    path: '/community/newsboard/create',
    name: 'createnewsboard',
    component: CreateNewsBoard
  },
  {
    path: '/community/newsboard/:id',
    name: 'detailnewsboard',
    component: DetailNewsBoard
  },
  {
    path: '/community/newsboard/edit/:id',
    name: 'editNewsArticle',
    component: EditNewsArticle
  },
  {
    path: '/community/userboard',
    name: 'userboard',
    component: UserBoard
  },
  {
    path: '/community/userboard/create',
    name: 'createuserboard',
    component: CreateUserBoard
  },
  {
    path: '/community/userboard/:id',
    name: 'detailuserboard',
    component: DetailUserBoard
  },
  {
    path: '/community/userboard/edit/:id',
    name: 'editUSerArticle',
    component: EditUserArticle
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
