import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap'
import axios from 'axios'
import VueCookies from 'vue-cookies';
import Carousel3d from 'vue3-carousel-3d';
import "vue3-carousel-3d/dist/index.css"
import { library } from "@fortawesome/fontawesome-svg-core";
import { faPhone } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faFacebook } from '@fortawesome/free-brands-svg-icons'
import { faInstagram } from '@fortawesome/free-brands-svg-icons'
import { faEnvelope} from '@fortawesome/free-solid-svg-icons';
import { faCalendar} from '@fortawesome/free-solid-svg-icons';

library.add(faPhone, faFacebook, faInstagram, faEnvelope, faCalendar);

createApp(App)
.use(store)
.use(router, axios)
.use(VueCookies)
.use(Carousel3d)
.component("font-awesome-icon", FontAwesomeIcon)
.mount('#app')
window._ = require('lodash');
