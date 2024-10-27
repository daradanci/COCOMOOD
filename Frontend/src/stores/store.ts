import { defineStore } from 'pinia'
import router from '@/router'
const bookInfo = {
  id: 0,
  title: '',
  score: '',
  volumes: 0,
  chapters: 0,
  image: '',
  link: '',
  type: '',
  status: '',
  theme: [],
  ta: [],
  author: [],
  genre: [],
}
const periodInfo = {
  start: 0,
  end: 0,
}
export const useMainStore = defineStore({
  id: 'main',
  state: () => ({
    user: {
      id: 0,
      login: '',
      name: '',
      registration_date: '',
      book_plan: '',
      read_amount: 0,
      average_interest: 0,
      average_readtime: 0,
      password: '',
    },
    isAuthenticated: false,
    booksRead: [],
    books1: [
      {
        image: 'path/to/image1.jpg', // Замените на реальный путь к изображению
        title: 'Том 1',
        author: 'Мосян Тунсю',
        rating: 8,
      },
      {
        image: 'path/to/image2.jpg', // Замените на реальный путь к изображению
        title: 'Том 4',
        author: 'Мосян Тунсю',
        rating: 9,
      },
    ],

    periods: [],
  }),
  getters: {
    getBooksRead: state => state.booksRead,
    getBooks1: state => state.books1,
  },
  actions: {
    register(userData: { name: string; login: string; password: string }) {
      // как-то зарегаться что ли
    },
    login(userData: { login: string; password: string }) {
      // this.user = userData
      const rightUserData = {
        login: 'dante13',
        password: '123456',
      }
      console.log(userData)
      if (
        userData.login === rightUserData.login &&
        userData.password === rightUserData.password
      ) {
        console.log('АВТОРИЗОВАН УРАААА')
        this.isAuthenticated = true
        alert(`ВХод завершен для ${this.login}!`)

        router.push('tracker1')
      } else {
        console.log('НЕАВТОРИЗОВАН')
        this.isAuthenticated = false
      }
    },
    logout() {
      this.user = {
        id: 0,
        login: '',
        name: '',
        registration_date: '',
        book_plan: '',
        read_amount: 0,
        average_interest: 0,
        average_readtime: 0,
        password: '',
      }
      this.isAuthenticated = false
    },
    readBook(bookData: { book_name: string; author: string; rate: number }) {
      this.booksRead.push(bookData)
    },
  },
})
