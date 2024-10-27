import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import CanvasJSChart from '@canvasjs/vue-charts'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

// Import Bootstrap and BootstrapVue CSS files (order is important)
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'
const pinia = createPinia()
const app = createApp(App)
app.use(CanvasJSChart)
app.use(createPinia())

app.use(pinia)

import { useMainStore } from '@/stores/store'
const mainStore = useMainStore()
router.beforeEach((to, from, next) => {
  if (to.name === 'tracker1' && !mainStore.isAuthenticated)
    next({ name: 'welcome' })
  else next()
})

app.use(router)
app.mount('#app')
