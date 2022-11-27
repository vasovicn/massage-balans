<template>
  <div class="row" style="margin: 150px 10px">
    <div class="col-6">
      <SingleMassage :massageID="massage" :masseurs="masseurs" v-if="massage && masseurs"/>
    </div>
      <div class="col-6">
        <div class="row" style="margin-left: 80px;">
          <MassageList/>
        </div>
    </div>
  </div>
</template>
    
<script>
import MassageList from '@/components/MassageList.vue'
import SingleMassage from '@/components/SingleMassage.vue'
export default {
  name: 'MassageDetails',
  props: ['id'],
  components: {
    MassageList,
    SingleMassage
  },
  data() {
    return {
      masseurs: null
    }
  },
  created() {
    this.$store.dispatch('getMassagesDjango').then(response => {
      console.log(response);
      this.$store.dispatch('fetchMassageDjango', this.id);
    })
    this.$store.dispatch('fetchmasseurs')
        .catch(error => {
          console.log(error)
        })
  },
  computed: {
    massage() {
      return this.$store.state.massages.find(massage => massage.id === parseInt(this.id))
    },
    masseurs() {
      return this.$store.state.masseurs
    }
  },
  methods: {
  }
}
</script>
<style scoped>
.massage {
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 1px solid;
  min-width: 200px;
  max-width: 700px;
  max-height: 500px;
  margin: auto;
  padding: 10px
}

.time {
  margin-top: 10px;
  padding: 3px
}

/* .time:hover {
    background-color: rgb(218, 218, 218);
    cursor: pointer;
    border-radius: 10px;
  } */
.button {
  background-color: #c2fbd7;
  border-radius: 100px;
  box-shadow: rgba(44, 187, 99, .2) 0 -25px 18px -14px inset, rgba(44, 187, 99, .15) 0 1px 2px, rgba(44, 187, 99, .15) 0 2px 4px, rgba(44, 187, 99, .15) 0 4px 8px, rgba(44, 187, 99, .15) 0 8px 16px, rgba(44, 187, 99, .15) 0 16px 32px;
  color: green;
  cursor: pointer;
  display: inline-block;
  font-family: CerebriSans-Regular, -apple-system, system-ui, Roboto, sans-serif;
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
  
    