import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
// import Vue from 'vue'
import App from './App.vue'
import router from './router'

import CanvasJSChart from '@canvasjs/vue-charts'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

// import VueSimpleAlert from 'vue-simple-alert'

// Import Bootstrap and BootstrapVue CSS files (order is important)
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'
const app = createApp(App)
const pinia = createPinia()
app.use(createPinia())
app.use(pinia)

app.use(CanvasJSChart)
// Vue.use(VueSimpleAlert)

// import { useMainStore } from '@/stores/store'
// const mainStore = useMainStore()
// router.beforeEach((to, from, next) => {
//   if (to.name === 'tracker1' && !mainStore.isAuthenticated)
//     next({ name: 'welcome' })
//   else next()
// })

app.use(router)
app.mount('#app')
