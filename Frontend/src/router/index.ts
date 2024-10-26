import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterForm from '@/components/RegisterForm.vue'
import AuthForm from '@/components/AuthForm.vue'
import UserPage from '@/views/UserPage.vue'
import ReadingProgress from '@/components/ReadingProgress.vue'
import MainPage from '@/views/MainPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
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
      component: AuthForm,
    },

    {
      path: '/reg',
      name: 'reg',
      component: RegisterForm,
    },

    {
      path: '/me',
      name: 'me',
      component: UserPage,
    },
  ],
})

export default router
