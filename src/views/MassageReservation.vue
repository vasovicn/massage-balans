<template>
    <router-link :to="{ name: 'HomeView' }">Home</router-link>
    <div v-if="massage" class="massage">
        <h1>{{massage.name}}</h1>
        <p>Trajanje masaze: {{massage.length}} min</p>
        <p> Cena masaze: {{massage.price}} RSD</p>
        <p>{{massage.info}}</p>
        <input id="date_picker" :min="dateMin" type="date" v-model="date" @change="changedDate"/>
        <TimeComponent v-if="date && clicked" 
                       :date="date" 
                       :massage="massage"
                       :currentTime="currentTime"
                       :currentDate="dateMin" 
                       @clicked-time="clickedTime"/>
        <div class="time" v-if="date && !clicked" @click="this.clicked = !this.clicked">
            Vreme:{{time}}
        </div>
        <button v-if="date && !clicked" style="margin: 20px;" class="button" @click="sendReservation()">Posalji rezervaciju</button>
    </div>
</template>
    
<script>
import TimeComponent from '@/components/TimeComponent.vue'
import { uuid } from 'vue-uuid';

export default {
    name: 'MassageReservation',
    data() {
        return {
            date: "",
            clicked: false,
            time: "",
            currentTime: ""
        }
    },
    components: {
    TimeComponent
},
    props: ['id'],
    created() {
        this.$store.dispatch('fetchMassage', this.id)
        this.timeMin()
        
    },
    computed: {
        massage() {
        return this.$store.state.massage
        },
        dateMin() {
            var today = new Date();
            var dd = String(today.getDate()).padStart(2, '0');
            var mm = String(today.getMonth() + 1).padStart(2, '0');
            var yyyy = today.getFullYear();
            today = yyyy + '-' + mm + '-' + dd;
            return today
        }
    },
    methods: {
        clickedTime(time) {
            this.clicked = !this.clicked
            this.time = time
        },
        changedDate() {
            if (!this.clicked) {
                this.clicked = !this.clicked
            }
        },
        sendReservation() {
            const reservation = {"id": uuid.v4(),
                                 "date":this.date,
                                 "time": this.time,
                                 "length": this.massage.length,
                                 "type": this.massage.name
                                }
            this.$store.dispatch('postReservedTime', reservation)
            this.$router.push({ name: 'MassageConfirmation', params: {id: reservation.id}})

        },
        timeMin() {
            var today = new Date();
            var hours = String(today.getHours()).padStart(2, '0');
            var minutes = String(today.getMinutes()).padStart(2, '0');
            
            var time = hours + ':' + minutes
            this.currentTime = time
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
  .time:hover {
    background-color: rgb(218, 218, 218);
    cursor: pointer;
    border-radius: 10px;
  }
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

.button:hover {
  box-shadow: rgba(44,187,99,.35) 0 -25px 18px -14px inset,rgba(44,187,99,.25) 0 1px 2px,rgba(44,187,99,.25) 0 2px 4px,rgba(44,187,99,.25) 0 4px 8px,rgba(44,187,99,.25) 0 8px 16px,rgba(44,187,99,.25) 0 16px 32px;
  transform: scale(1.05);
}
</style>
  
    