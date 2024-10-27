import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterForm from '@/components/RegisterForm.vue'
import AuthForm from '@/components/AuthForm.vue'
import UserPage from '@/views/UserPage.vue'
import ReadingProgress from '@/components/ReadingProgress.vue'
import MainPage from '@/views/MainPage.vue'
import Reg from '@/views/Reg.vue'
import Auth from '@/views/Auth.vue'
import Welcome from '@/views/Welcome.vue'
import BookList from '@/components/BookList.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'welcome',
      component: Welcome,
    },

    {
      path: '/tracker',
      name: 'tracker',
      component: ReadingProgress,
    },
    {
      path: '/tracker1',
      name: 'tracker1',
      component: MainPage,
    },
    {
      path: '/auth',
      name: 'auth',
      component: Auth,
    },

    {
      path: '/reg',
      name: 'reg',
      component: Reg,
    },

    {
      path: '/me',
      name: 'me',
      component: UserPage,
    },
    {
      path: '/test',
      name: 'test',
      component: BookList,
    },
  ],
})

export default router
