<script setup lang="ts">
import UserBookList from './UserBookList.vue'
</script>

<template>
  <div class="book_list">
    <h2>Я. Звучит гордо.</h2>
    <UserBookList />
  </div>
</template>

<style scoped>
.book_list {
  max-width: 400px;
  margin: auto;
}
.form-group {
  margin-bottom: 15px;
}
label {
  display: block;
  margin-bottom: 5px;
}
input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}
.is-invalid {
  border-color: red;
}
.error {
  color: red;
  font-size: 0.9em;
}
button {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}
</style>
