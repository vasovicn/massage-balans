<template>
    <router-link :to="{ name: 'HomeView' }">Home</router-link>
    <div v-if="massage" class="massage">
        <h1>{{massage.name}}</h1>
        <p>Trajanje masaze: {{massage.length}} min</p>
        <p> Cena masaze: {{massage.price}} RSD</p>
        <p>{{massage.info}}</p>
        <button @click="goToReservation(massage.id)">Rezervisi</button>
    </div>
</template>
    
<script>

export default {
    name: 'MassageDetails',
    props: ['id'],
    created() {
        this.$store.dispatch('fetchMassageDjango', this.id)
    },
    computed: {
        massage() {
        return this.$store.state.massage
        }
    },
    methods: {
        goToReservation(massageID) {
          this.$router.push({ name: 'MassageReservation', params: {id: massageID}})
        }
    }
}
</script>
<style scoped>
  .massage {
    display: flex;
    flex-direction: column;
    align-items: center;
    border:1px solid;
    min-width: 200px;
    max-width: 700px;
    max-height: 500px;
    margin:auto;
    padding:10px
  }
  .time {
    margin-top: 10px;
    padding:3px
  }
  /* .time:hover {
    background-color: rgb(218, 218, 218);
    cursor: pointer;
    border-radius: 10px;
  } */
  .button {
  background-color: #c2fbd7;
  border-radius: 100px;
  box-shadow: rgba(44, 187, 99, .2) 0 -25px 18px -14px inset,rgba(44, 187, 99, .15) 0 1px 2px,rgba(44, 187, 99, .15) 0 2px 4px,rgba(44, 187, 99, .15) 0 4px 8px,rgba(44, 187, 99, .15) 0 8px 16px,rgba(44, 187, 99, .15) 0 16px 32px;
  color: green;
  cursor: pointer;
  display: inline-block;
  font-family: CerebriSans-Regular,-apple-system,system-ui,Roboto,sans-serif;
  padding: 7px 20px;
  text-align: center;
  text-decoration: none;
  transition: all 250ms;
  border: 0;
  font-size: 16px;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

/* .button:hover {
  box-shadow: rgba(44,187,99,.35) 0 -25px 18px -14px inset,rgba(44,187,99,.25) 0 1px 2px,rgba(44,187,99,.25) 0 2px 4px,rgba(44,187,99,.25) 0 4px 8px,rgba(44,187,99,.25) 0 8px 16px,rgba(44,187,99,.25) 0 16px 32px;
  transform: scale(1.05);
} */
</style>
  
    