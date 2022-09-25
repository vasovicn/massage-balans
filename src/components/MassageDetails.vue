<template>
    <div v-if="massage">
        <p>Trajanj masaze: {{massage.length}} min</p>
        <p> Cena masaze: {{massage.price}} RSD</p>
        <p>{{massage.info}}</p>
        <button @click="reservationPage">Rezervisi</button>
    </div>
</template>
    
<script>

export default {
    name: 'MassageDetails',
    props: ['massageID'],
    created() {
        this.$store.dispatch('fetchMassage', this.massageID)
    },
    computed: {
        massage() {
        return this.$store.state.massage
        }
    },
    methods: {
        reservationPage() {
            this.$router.push({ name: 'MassageReservation', params: {id: this.massageID}})
        }
    }
}
</script>
<style>
  .massage {
    display: flex;
    flex-direction: column;
    align-items: center;
    border:1px solid;
    min-width: 200px;
    max-width: 400px;
    max-height: 300px;
    padding: 10px;
  }
</style>
  
    