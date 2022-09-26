<template>
    <div class="massage">
        <router-link :to="{ name: 'HomeView' }">Home</router-link>
        <h2>Vasa rezervacija je uspesno poslata</h2>
        <p>Vidimo se {{reservation.date}} u {{reservation.time}} </p>
    </div>
</template>
    
<script>

export default {
    name: 'MassageConfirmation',
    data() {
        return {

        }
    },
    props: ['id'],
    created() {

    },
    computed: {
        reservation() {
            return this.$store.state.reservation
        }
       
    },
    methods: {
        
    }
}
</script>
<style scoped>
.massage {
  display: flex;
  align-items: center;
  border:1px solid;
  min-width: 300px;
  max-width: 300px;
  max-height: 300px;
}
</style>
  
    