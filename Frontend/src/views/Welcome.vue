<template>
  <div class="container">
    <header>
      <img
        src="@/assets/COCOMOOD_logo_white.png"
        alt="Cocomood logo"
        class="logo"
      />
    </header>
    <div class="registration-box">
      <h2>Добро пожаловать!</h2>
      <!-- <form @submit.prevent="register"> -->
      <button type="submit" class="register-btn">
        <router-link to="/reg" class="register-btn">Регистрация</router-link>
      </button>

      <br />
      <br />
      <button type="submit" class="register-btn">
        <router-link to="/auth" class="register-btn">Войти</router-link>
      </button>
      <!-- </form> -->
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      username: '',
      password: '',
      showPassword: false,
    }
  },
  methods: {
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword
    },
    register() {
      // Реализуйте регистрацию
      alert(`Регистрация завершена для ${this.name}!`)
      router.push('/auth')
    },
  },
}
</script>

<style scoped>
.container {
  font-family: Arial, sans-serif;
  text-align: center;
  padding: 20px;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
}

.logo {
  height: 40px;
  align-items: center;
}

.login-btn {
  padding: 8px 16px;
  background: white;
  border: 1px solid #333;
  cursor: pointer;
}

.registration-box {
  color: #333;
  background: white;
  padding: 30px;
  margin: 50px auto;
  max-width: 300px;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

h2 {
  font-size: 24px;
  margin-bottom: 20px;
}

.input-group {
  margin-bottom: 15px;
  text-align: left;
}

input[type='text'],
input[type='password'] {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.register-btn {
  width: 100%;
  padding: 10px;
  background-color: #333;
  color: white;
  border: none;
  cursor: pointer;
  font-size: 16px;
}

span {
  cursor: pointer;
  position: absolute;
  right: 15px;
  top: 38px;
  font-size: 18px;
}

.eye {
  float: right;
}
</style>
