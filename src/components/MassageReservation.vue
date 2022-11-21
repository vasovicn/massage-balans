<template>
    <div v-if="massageID">
        <p>Trajanje masaze: {{ massage.length }} min</p>
        <p> Cena masaze: {{ massage.price }} RSD</p>
        <carousel-3d :display="3" style="width:200px !important">
            <slide class="customize-carousel" v-for="(masseur, i) in masseuers" :index="i" :key="i"
                @click="this.selectedMasseur = masseur">
                <img :data-index="i" :src="masseur.photo_url" style="height: inherit;">
            </slide>
        </carousel-3d>
        <div>{{ this.selectedMasseur.user.first_name }}</div>
        <br />
        <div style="margin-bottom:10px">
            <input id="date_picker" :min="dateMin" type="date" v-model="date" @change="changedDate" />
        </div>
        <div class="btns-background" v-if="date && clicked">
            <button @click="this.timePeriod = [7, 12]" class="btn-abc btn-left"
                :style="{ backgroundColor: this.timePeriod[0] === 7 ? 'white' : '#f1f1f1' }">Morning</button>
            <button @click="this.timePeriod = [11, 17]" class="btn-abc"
                :style="{ backgroundColor: this.timePeriod[0] === 11 ? 'white' : '#f1f1f1' }">Afternoon</button>
            <button @click="this.timePeriod = [16, 22]" class="btn-abc btn-right"
                :style="{ backgroundColor: this.timePeriod[0] === 16 ? 'white' : '#f1f1f1' }">Evening</button>
        </div>
        <TimeComponent v-if="date && clicked" :date="date" :massage="massage" :currentTime="currentTime"
            :masseur_id="selectedMasseur.id" :currentDate="dateMin" @clicked-time="clickedTime"
            :timePeriod="this.timePeriod" />
        <div class="choosen-time" v-if="date && !clicked" @click="this.clicked = !this.clicked">
            Vreme:{{ time }}
        </div>
        <button v-if="!this.$store.state.isAuthenticated && date && !clicked" class="button" data-toggle="modal"
            data-target="#myModal" @click="setCurrentMasseur">Posalji
            rezervaciju</button>
        <button v-if="this.$store.state.isAuthenticated && date && !clicked" class="button"
            @click="sendReservation">Posalji
            rezervaciju</button>
    </div>
</template>
    
<script>
import TimeComponent from '@/components/TimeComponent.vue'
import { uuid } from 'vue-uuid';
import { Carousel3d, Slide } from 'vue3-carousel-3d';


export default {
    name: 'MassageReservation',
    data() {
        return {
            date: "",
            clicked: false,
            time: "",
            currentTime: "",
            masseur_id: 1,
            timePeriod: [7, 12],
            selectedMasseur: this.$store.state.masseuers[0],
            client_token: ""
        }
    },
    emits: ["reserved", "fold"],
    components: {
        TimeComponent,
        Carousel3d,
        Slide
    },
    props: ['massageID'],
    created() {
        this.$store.dispatch('fetchMassageDjango', this.massageID.id)
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
        },
        masseuers() {
            return this.$store.state.masseuers
        }
    },
    methods: {
        setCurrentMasseur() {
            this.$store.commit('SET_CURRENT_MASSEUR', this.selectedMasseur)
            this.$store.commit('SET_CURRENT_MASSAGE_DATE', this.date)
        },
        clickedTime(time) {
            this.clicked = !this.clicked
            this.time = time
            this.$store.commit('SET_MASSAGE_TIME', time)
        },
        changedDate() {
            if (!this.clicked) {
                this.clicked = !this.clicked
            }
        },
        sendReservation() {
            const reservedTermin = {
                "id": uuid.v4(),
                "date": this.date,
                "time": this.time,
                "length": this.massage.length,
                "type": this.massage.name,
                "token": this.$store.state.token,
                "masseur_id": parseInt(this.selectedMasseur.id)
            }
            this.$store.dispatch('postReservationDjango', reservedTermin)
            this.$store.dispatch('setSelectedMassageButton', true)
            this.$store.commit('SET_SELECTED_MASSAGE', false)
            window.scrollTo(0, 0);
        },
        timeMin() {
            var today = new Date();
            var hours = String(today.getHours()).padStart(2, '0');
            var minutes = String(today.getMinutes()).padStart(2, '0');

            var time = hours + ':' + minutes
            this.currentTime = time
        },
        closeModal() {
            this.toggleModal = false
        },
    }
}
</script>
<style scoped>
@import url("https://fonts.googleapis.com/css?family=DM+Sans:400,500,700&display=swap");


input[type=radio] {
    display: none;
}

/* .customize-carousel {
    height:100px !important;
    width:50px !important;
} */
.carousel-3d-container {
    min-width: 650px;
    /* max-height: 150px; */
    /* display: flex !important; */
}

/* .carousel-3d-slide {
    height: 50px;
    width: 50px;
} */

.card {
    position: absolute;
    width: 100%;
    height: 150px;
    left: 0;
    right: 0;
    margin: auto;
    transition: transform 0.4s ease;
    cursor: pointer;
}

.carousel-container {
    margin: auto;
    margin-top: -120px;
    margin-bottom: -20px;
    width: 200px;
    height: 300px;
    transform-style: preserve-3d;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
}

.cards {
    position: relative;
    width: 70%;
    height: 15%;
}


.massage {
    display: flex;
    flex-direction: column;
    align-items: center;
    /* border:1px solid; */
    min-width: 200px;
    max-width: 700px;
    max-height: 500px;
    margin: auto;
    padding: 10px
}

.time {
    margin-top: 10px;
    /* padding: 3px; */
    min-height: 20px;
}

.time:hover {
    background-color: rgb(218, 218, 218);
    cursor: pointer;
    border-radius: 10px;
}

.button {
    background-color: #81bfaa;
    border-radius: 18px;
    /* box-shadow: #81bfaa 0 -25px 18px -14px inset, #81bfaa 0 1px 2px, #81bfaa 0 2px 4px, #81bfaa 0 4px 8px, #81bfaa 0 8px 16px, #81bfaa 0 16px 32px; */
    color: white;
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

.button:hover {
    /* box-shadow: rgba(44, 187, 99, .35) 0 -25px 18px -14px inset, rgba(44, 187, 99, .25) 0 1px 2px, rgba(44, 187, 99, .25) 0 2px 4px, rgba(44, 187, 99, .25) 0 4px 8px, rgba(44, 187, 99, .25) 0 8px 16px, rgba(44, 187, 99, .25) 0 16px 32px; */
    transform: scale(1.05);
}

.choosen-time {
    padding: 5px;
    width: fit-content;
    margin: auto;
    margin-bottom: 5px;
}

.choosen-time:hover {
    transform: scale(1.05);
    background-color: rgb(241, 241, 241);
    cursor: pointer;
    border-radius: 5px;
}

.btn-abc {
    margin: 5px 0px 5px 0px;
    width: 20%;
    border: none;
    border-radius: 5px;
    background-color: #f1f1f1;
    width: 100%;
}

.btn-abc-selected {
    background-color: white;
}

.btns-background {
    background-color: #f1f1f1;
    border-radius: 5px;
    width: 310px;
    margin: 0 auto;
    display: inline-flex;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
}

.btn-left {
    margin-left: 5px;
}

.btn-right {
    margin-right: 5px;
}

.carousel-img {
    width: 100%;
    height: 100%;
    border-radius: 10px;
    object-fit: cover;
}

#item-1:checked~.cards #song-3,
#item-2:checked~.cards #song-1,
#item-3:checked~.cards #song-2 {
    transform: translatex(-40%) scale(0.8);
    opacity: 0.4;
    z-index: 0;
}

#item-1:checked~.cards #song-2,
#item-2:checked~.cards #song-3,
#item-3:checked~.cards #song-1 {
    transform: translatex(40%) scale(0.8);
    opacity: 0.4;
    z-index: 0;
}

#item-1:checked~.cards #song-1,
#item-2:checked~.cards #song-2,
#item-3:checked~.cards #song-3 {
    transform: translatex(0) scale(1);
    opacity: 1;
    z-index: 1;
}

#item-1:checked~.cards #song-1 img,
#item-2:checked~.cards #song-2 img,
#item-3:checked~.cards #song-3 img {
    box-shadow: 0px 0px 5px 0px rgba(81, 81, 81, 0.47);
}

.player {
    background-color: #fff;
    border-radius: 8px;
    min-width: 320px;
    padding: 16px 10px;
}

.upper-part {
    position: relative;
    display: flex;
    align-items: center;
    margin-bottom: 12px;
    height: 36px;
    overflow: hidden;
}

.play-icon {
    margin-right: 10px;
}

.song-info {
    width: calc(100% - 32px);
    display: block;
}

.song-info .title {
    color: #403d40;
    font-size: 14px;
    line-height: 24px;
}

.sub-line {
    display: flex;
    justify-content: space-between;
    width: 100%;
}

.subtitle,
.time {
    font-size: 12px;
    line-height: 16px;
    color: #c6c5c6;
}

.time {
    font-size: 12px;
    line-height: 16px;
    color: #a5a5a5;
    font-weight: 500;
    margin-left: auto;
}

.progress-bar {
    height: 3px;
    width: 100%;
    background-color: #e9efff;
    border-radius: 2px;
    overflow: hidden;
}

.progress {
    display: block;
    position: relative;
    width: 60%;
    height: 100%;
    background-color: #2992dc;
    border-radius: 6px;
}

.info-area {
    width: 100%;
    position: absolute;
    top: 0;
    left: 30px;
    transition: transform 0.4s ease-in;
}

#item-2:checked~.player #test {
    transform: translateY(0);
}

#item-2:checked~.player #test {
    transform: translateY(-40px);
}

#item-3:checked~.player #test {
    transform: translateY(-80px);
}
</style>
    