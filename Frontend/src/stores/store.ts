import { defineStore } from 'pinia'

export const useMainStore = defineStore({
  id: 'main',
  state: () => ({
    user: {
      username: '',
      email: '',
    },
    isAuthenticated: false,
  }),
  actions: {
    login(userData: { username: string; email: string }) {
      this.user = userData
      this.isAuthenticated = true
    },
    logout() {
      this.user = { username: '', email: '' }
      this.isAuthenticated = false
    },
  },
})
