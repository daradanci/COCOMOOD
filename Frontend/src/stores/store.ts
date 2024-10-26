import { defineStore } from 'pinia'

const bookInfo = {
  book_name: '',
  author: '',
  rate: 0,
}

export const useMainStore = defineStore({
  id: 'main',
  state: () => ({
    user: {
      username: '',
      email: '',
    },
    isAuthenticated: false,
    booksRead: [bookInfo],
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
    readBook(bookData: { book_name: string; author: string; rate: number }) {
      this.booksRead.push(bookData)
    },
  },
})
