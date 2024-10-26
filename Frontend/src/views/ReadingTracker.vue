<!-- views/ReadingTracker.vue -->
<template>
  <div class="reading-tracker">
    <ReadingProgress
      :totalBooks="10"
      :booksRead="4"
      :readingGoal="9"
      :toRead="1"
      :interestLevel="50"
      :avgReadingTime="1"
    />
    <BookList :books="readBooks" :booksRead="4" :totalBooks="10" />
  </div>
</template>

<script>
import ReadingProgress from '@/components/ReadingProgress.vue'
import BookList from '@/components/BookList.vue'

export default {
  components: {
    ReadingProgress,
    BookList,
  },
  data() {
    return {
      readBooks: [
        {
          id: 1,
          title: 'Магистр дьявольского культа',
          cover: 'cover1.jpg',
          rating: 4.8,
        },
        {
          id: 2,
          title: 'Магистр дьявольского культа 2',
          cover: 'cover2.jpg',
          rating: 4.7,
        },
        // Добавьте другие книги по необходимости
      ],
    }
  },
}
</script>

<style scoped>
.reading-tracker {
  background-color: #000;
  color: #fff;
  padding: 20px;
}
</style>
