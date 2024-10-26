<!-- components/BookList.vue -->
<template>
  <div class="book-list">
    <h2>Прочитанные книги — {{ booksRead }} из {{ totalBooks }}</h2>
    <div class="books">
      <div class="book" v-for="book in books" :key="book.id">
        <img :src="book.cover" alt="Обложка книги" />
        <p>{{ book.title }}</p>
        <span>{{ book.rating }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    books: Array,
    booksRead: Number,
    totalBooks: Number,
  },
}
</script>

<style scoped>
.book-list {
  margin-top: 20px;
}
.books {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
.book {
  width: 150px;
  text-align: center;
  background-color: #fff;
  border-radius: 5px;
  padding: 10px;
}
img {
  width: 100%;
  height: auto;
  border-radius: 5px;
}
</style>
