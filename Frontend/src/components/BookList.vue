<template>
  <div class="container mt-4">
    <div class="row flex-nowrap overflow-auto">
      <div
        v-for="(book, index) in books1"
        :key="index"
        class="col-6 col-md-4 col-lg-3 mb-4 d-inline-block"
      >
        <div class="card h-100 text-center">
          <img :src="book.image" class="card-img-top" alt="Book Cover" />
          <div class="card-body">
            <h5 class="card-title">{{ book.title }}</h5>
            <p class="card-text">{{ book.author }}</p>
            <p class="card-text">{{ book.rating }}/10</p>
            <a href="https://myanimelist.net/manga/2/Berserk" target="_blank">
              <button class="btn btn-success">Подробнее</button>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useMainStore } from '@/stores/store'
import { storeToRefs } from 'pinia'
export default {
  data() {
    return {}
  },
  setup() {
    const mainStore = useMainStore()
    mainStore.readBook({
      image: new URL('@/assets/157897l.jpg', import.meta.url).href,
      title: 'Берсерк Том 1',
      author: 'Кэнтаро Миура',
      rating: 8,
    })

    mainStore.readBook({
      image: new URL('@/assets/157931l.jpg', import.meta.url).href,
      title: 'Бересерк Том 6',
      author: 'Кэнтаро Миура',
      rating: 8.6,
    })

    // Доступ к состоянию и методам
    // const booksRead = mainStore.getBooksRead // для геттера
    const books1 = mainStore.getBooksRead // для геттера
    // mainStore.login({ username: 'user', email: 'user@example.com' }) // для действия

    return {
      books1,
      mainStore,
    }
  },
}
</script>

<style>
.container {
  max-width: 1200px;
}

.row.flex-nowrap {
  overflow-x: auto;
  flex-wrap: nowrap;
  padding-bottom: 1rem;
}

.card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card-title {
  font-size: 1.2rem;
  font-weight: bold;
}

.card-text {
  color: #6c757d;
}
</style>
