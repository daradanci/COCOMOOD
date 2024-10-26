<template>
  <div class="register">
    <h2>Авторизация</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="username">Имя пользователя</label>
        <input
          type="text"
          id="username"
          v-model="form.username"
          :class="{ 'is-invalid': errors.username }"
        />
        <span v-if="errors.username" class="error">{{ errors.username }}</span>
      </div>

      <div class="form-group">
        <label for="password">Пароль</label>
        <input
          type="password"
          id="password"
          v-model="form.password"
          :class="{ 'is-invalid': errors.password }"
        />
        <span v-if="errors.password" class="error">{{ errors.password }}</span>
      </div>
      <button type="submit">Войти</button>
    </form>
  </div>
</template>

<script>
import { useMainStore } from '../stores/store'

// store.login({ username: 'exampleUser', email: 'example@example.com' })

export default {
  data() {
    return {
      form: {
        username: '',
        email: '',
        password: '',
      },
      errors: {},
    }
  },
  methods: {
    validateForm() {
      this.errors = {}
      if (!this.form.username)
        this.errors.username = 'Имя пользователя обязательно'
      if (!this.form.email) this.errors.email = 'Электронная почта обязательна'
      else if (!/\S+@\S+\.\S+/.test(this.form.email))
        this.errors.email = 'Некорректный формат email'
      if (!this.form.password) this.errors.password = 'Пароль обязателен'
      else if (this.form.password.length < 6)
        this.errors.password = 'Пароль должен быть не менее 6 символов'
      return Object.keys(this.errors).length === 0
    },
    submitForm() {
      if (this.validateForm()) {
        const store = useMainStore()

        // Логика отправки данных на сервер
        console.log('Форма отправлена:', this.form)
        // Очистка формы после успешной регистрации
        this.form = { username: '', password: '' }
      }
    },
  },
}
</script>

<style scoped>
.register {
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
