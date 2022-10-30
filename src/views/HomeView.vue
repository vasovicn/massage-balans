<template>
  <div class="row" style="margin:50px">
    <div class="col-8">
      <MassageList />
    </div>
    <div class="col-1" @click="focusOUT"/>
    <div class="col-3">
      <MasseurList />
    </div>
  </div>
</template>
  
<script>
import MassageList from '@/components/MassageList.vue'
import MasseurList from '@/components/MasseurList.vue'
import axios from 'axios'

export default {
  name: 'HomeView',
  components: {
    MassageList,
    MasseurList,
  },
  beforeCreate() {
    this.$store.dispatch('initialToken')
    const token = this.$store.state.token

    if ( token ) {
      axios.defaults.headers.common['Authorization'] = 'Token' + token
    }
    else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  methods: {
    focusOUT() {
      this.$store.dispatch('setSelectedMassage', null)
    }
  }
  
}
</script>
  
<style scoped>
@import'~bootstrap/dist/css/bootstrap.css'
</style>
  