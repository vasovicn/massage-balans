<template>
  <router-link :to="{ name: 'BackendView' }">Admin View</router-link>
  <div class="row" style="margin:50px">
    <div class="col-8">
      <MassageList />
    </div>
    <div class="col-1"/>
    <div class="col-3">
      <MasseurList />
    </div>
  </div>
</template>
  
<script>
import MassageList from '@/components/MassageList.vue'
import MasseurList from '@/components/MasseurList.vue'

export default {
  name: 'HomeView',
  components: {
    MassageList,
    MasseurList
  }
}
</script>
  
<style scoped>
@import'~bootstrap/dist/css/bootstrap.css'
</style>
  