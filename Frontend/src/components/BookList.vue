<template>
  <div class="container mt-4">
    <div class="row flex-nowrap overflow-auto">
      <div
        v-for="(book, index) in books"
        :key="index"
        class="col-6 col-md-4 col-lg-3 mb-4 d-inline-block"
      >
        <div class="card h-100 text-center">
          <img :src="book.image" class="card-img-top" alt="Book Cover" />
          <div class="card-body">
            <h5 class="card-title">{{ book.title }}</h5>
            <p class="card-text">{{ book.author }}</p>
            <p class="card-text">{{ book.rating }}/10</p>
            <button class="btn btn-success">Подробнее</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      books: [
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
        // Добавьте другие книги, если нужно
      ],
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
