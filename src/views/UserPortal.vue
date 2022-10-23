<template>
  <div></div>
</template>
    
<script>
import axios from 'axios'

export default {
  name: 'UserPortal',
  data() {
    return {
      reservations: '',
      phone: '',
      email: '',
      firstname: '',
      lastname: '',
      dateOfBirth: '',

    }
  },
  components: {
  },
  created() {
    this.$store.dispatch('userPortal')

  },
  beforeCreate() {
    this.$store.dispatch('initialToken')
    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token' + token
    }
    else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  }
}
</script>
    
<style scoped>
@import'~bootstrap/dist/css/bootstrap.css'
</style>
    