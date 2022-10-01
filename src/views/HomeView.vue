<template>
  <!-- <div style="column-count: 2;"> -->
    <router-link :to="{ name: 'BackendView' }">Admin View</router-link>
    <MassageList/>
    <div style="min-height:600px">
      <MasseurList/>
    </div>.
  <!-- </div> -->
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
.massages {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
</style>
  