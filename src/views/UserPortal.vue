<template>
   <div></div>
</template>
    
  <script>
  
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
        // this.$store.dispatch('userPortal')
        
    }  
  }
  </script>
    
  <style scoped>
  @import'~bootstrap/dist/css/bootstrap.css'
  </style>
    