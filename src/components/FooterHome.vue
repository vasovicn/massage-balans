<template>
    <div class="container-fluid pb-0 mb-0 justify-content-center text-light" style="box-shadow:5px">
        <footer>
            <div class="row my-3 justify-content-center">
                <div class="col-11">
                    <div class="row ">
                        <div class="col-xl-6 col-md-4 col-sm-4 col-12   my-auto mx-auto a">

                            <img src="http://localhost:8000/media/logo_lotus.jpg"
                                style="height: 200px;margin:-35px 0 -40px 0" />
                        </div>
                        <div class="col-xl-2 col-md-4 col-sm-4 col-12">
                            <h6 class="mb-3 mb-lg-4 bold-text "><b>RADNO VREME</b></h6>
                            <ul class="list-unstyled">
                                <li style="color:white">Svakim danom:<br />08-22h</li>
                            </ul>
                        </div>
                        <div class="col-xl-2 col-md-4 col-sm-4 col-12">
                            <h6 class="mb-3 mb-lg-4 text-muted bold-text mt-sm-0 mt-5">
                                <b>
                                    ADRESA
                                </b>
                            </h6>
                            <a style="color:white" target="_blank" href="https://goo.gl/maps/VRgUFSdoeBrHQ8Vx6">Laze
                                Jovanovica Porcija 7a Beograd, Zemun </a>
                        </div>
                        <div class="col-xl-2 col-md-4 col-sm-4 col-12" >
                            <font-awesome-icon style="height: 40px;margin: 5px;"
                            :icon="{ prefix: 'fas', iconName: 'phone' }" class="phone" @click="callNumber()" />
                        <font-awesome-icon style="height: 40px;margin: 5px;"
                            :icon="{ prefix: 'fab', iconName: 'facebook' }" class="facebook" @click="goFacebook" />
                        <font-awesome-icon style="height: 40px;margin: 5px;"
                            :icon="{ prefix: 'fab', iconName: 'instagram' }" class="instagram" @click="goInstagram" />
                        <font-awesome-icon style="height: 40px;margin: 5px;"
                            :icon="{ prefix: 'fas', iconName: 'envelope' }" class="email" @click="sendEmail" />
                        </div>
                    </div>
                </div>
            </div>
        </footer>
    </div>
</template>

<script>

export default {
    name: 'FooterHome',
    components: {
    },
    data() {
        return {
        }
    },
    methods: {
        back() {
            this.$router.back()
        },
        goFacebook() {
            window.open("https://www.facebook.com/")
        },
        goInstagram() {
            window.open("https://www.instagram.com/")
        },
        callNumber() {
            window.location ='tel:'+ +381652812333;
        },
        sendEmail() {
            window.location ='mailto:'+ 'nikolazemun97@gmail.com';
        }
    },
    computed: {
    },
}

</script>
  
<style scoped>
@import url('https://fonts.googleapis.com/css?family=Rubik&display=swap');

body {
    background: linear-gradient(0deg, #fff, 50%, #DEEEFE);
    font-family: 'Rubik', sans-serif;
    background: #828789;
    /* height: 100 !important; */
}


.container-fluid {
    overflow: hidden;
    /* margin-top: 250px ; */
    background: #81bfaa;
    color: #828789 !important;
    margin-bottom: 0;
    padding-bottom: 0;
    box-shadow: 0px -5px 5px rgb(223, 218, 218);
    min-height: 150px;
}

small {
    font-size: calc(12px + (15 - 12) * ((100vw - 360px) / (1600 - 360))) !important;
}

.bold-text {
    color: #828789 !important;
}


.mt-55 {
    margin-top: calc(50px + (60 - 50) * ((100vw - 360px) / (1600 - 360))) !important;
}


h3 {
    font-size: calc(34px + (40 - 34) * ((100vw - 360px) / (1600 - 360))) !important;
}

.social {
    font-size: 21px !important;
}

.rights {
    font-size: calc(10px + (12 - 10) * ((100vw - 360px) / (1600 - 360))) !important;
}
.instagram:hover {
    cursor: pointer;
    transform: scale(1.1);
    color: #E1306C;
}
.facebook:hover {
    cursor: pointer;
    transform: scale(1.1);
    color: #4267B2;
}
.email:hover {
    cursor: pointer;
    transform: scale(1.1);
    color: #EA4335;
}
.phone:hover {
    cursor: pointer;
    transform: scale(1.1);
    color: #5FAE93;
}
</style>
  