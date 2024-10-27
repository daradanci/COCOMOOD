import { defineStore } from 'pinia'
import router from '@/router'
import axios from 'axios'
import Cookies from 'js-cookie'

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
    async register(userData: {
      name: string
      login: string
      password: string
    }) {
      const req_result = await axios.post(
        `http://192.168.250.244:8080/user/create`,
        userData,
      )
      console.log(req_result)
    },

    async login(userData: { login: string; password: string }) {
      try {
        const req_result = await axios.post(
          `http://192.168.250.244:8080/user/login`,
          userData,
        )
        this.isAuthenticated = true
        localStorage.setItem(
          'isAuthenticated',
          JSON.stringify(this.isAuthenticated),
        )
        router.push('tracker1')

        console.log(userData)
        console.log(req_result)

        // Предположим, что токен возвращается в `req_result.data.token`
        if (req_result.data && req_result.data.token) {
          Cookies.set('authToken', req_result.data.token, { expires: 1 }) // Сохраняем куки на 1 день
          console.log('Куки сохранены')
        }
      } catch (error) {
        console.error('Ошибка при выполнении запроса:', error)
        this.isAuthenticated = false
        localStorage.setItem(
          'isAuthenticated',
          JSON.stringify(this.isAuthenticated),
        )
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
      localStorage.setItem(
        'isAuthenticated',
        JSON.stringify(this.isAuthenticated),
      )
    },
    readBook(bookData: { book_name: string; author: string; rate: number }) {
      this.booksRead.push(bookData)
    },
    async getUserData(userData: {}) {
      try {
        const req_result = await axios.post(
          `http://192.168.250.244:8080/user/read_amount`,
          userData,
          { withCredentials: true },
        )

        console.log(userData)
        console.log(req_result)

        // Предположим, что токен возвращается в `req_result.data.token`
        if (req_result.data && req_result.data.token) {
          Cookies.set('authToken', req_result.data.token, { expires: 1 }) // Сохраняем куки на 1 день
          console.log('Куки сохранены')
        }
      } catch (error) {
        console.error('Ошибка при выполнении запроса:', error)
        this.isAuthenticated = false
      }
    },
  },
})
