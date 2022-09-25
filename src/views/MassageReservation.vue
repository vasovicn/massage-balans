<template>
    <div v-if="massage" class="massage">
        <h1>{{massage.name}}</h1>
        <p>Trajanje masaze: {{massage.length}} min</p>
        <p> Cena masaze: {{massage.price}} RSD</p>
        <p>{{massage.info}}</p>
        <input type="date" v-model="date" @change="changedDate"/>
        <TimeComponent v-if="date && clicked" :date="date" :massage="massage" @clicked-time="clickedTime"/>
        <div class="time" v-if="date && !clicked" @click="this.clicked = !this.clicked">
            Vreme:{{time}}
        </div>
        <button v-if="date && time" style="margin-top: 5px;" @click="sendReservation()">Posalji rezervaciju</button>
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
            time: ""
        }
    },
    components: {
    TimeComponent
},
    props: ['id'],
    created() {
        this.$store.dispatch('fetchMassage', this.id)
    },
    computed: {
        massage() {
        return this.$store.state.massage
        },
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
                                "length": this.massage.length}
            this.$store.dispatch('postReservedTime', reservation)
            this.$router.push({ name: 'MassageConfirmation', params: {id: reservation.id}})

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
    border:1px solid;
    margin-top: 10px;
    padding:3px
  }
  .time:hover {
    background-color: rgb(218, 218, 218);
    cursor: pointer;
  }
</style>
  
    