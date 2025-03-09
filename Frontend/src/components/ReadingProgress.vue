<!-- components/ReadingProgress.vue -->

<template>
  <div class="reading-progress">
    <div>
      <donut-chart />
    </div>

    <div class="progress-info">
      <div class="stats">
        <span>{{ booksRead }} / {{ totalBooks }}</span>
        <p>Прочитал</p>
      </div>
      <div class="stats">
        <span>{{ readingGoal }}</span>
        <p>План чтения</p>
      </div>
      <div class="stats">
        <span>{{ toRead }}</span>
        <p>Хочу прочитать</p>
      </div>
    </div>
    <div class="interest">
      Твоя <strong>заинтересованность</strong> в среднем составляет:
      <span>{{ interestLevel }}%</span>
    </div>
    <div class="reading-time">
      Твое среднее <strong>время чтения</strong> в среднем составляет:
      <span>{{ avgReadingTime }} час</span>
    </div>
  </div>
</template>

<script>
import DonutChart from './DonutChart.vue'
import DonutChartVue from './DonutChart.vue'
export default {
  components: { DonutChart },
  props: {
    totalBooks: Number,
    booksRead: Number,
    readingGoal: Number,
    toRead: Number,
    interestLevel: Number,
    avgReadingTime: Number,
  },
}
</script>

<style scoped>
.reading-progress {
  text-align: center;
  color: #fff;
}
.progress-circle {
  font-size: 2rem;
  background-color: #f2b04a;
  color: #000;
  border-radius: 50%;
  padding: 20px;
  display: inline-block;
}
.progress-info {
  display: flex;
  justify-content: space-around;
  margin: 20px 0;
}
.stats {
  color: #fff;
}
.interest,
.reading-time {
  background-color: #333;
  margin: 10px;
  padding: 10px;
  border-radius: 5px;
}
</style>
