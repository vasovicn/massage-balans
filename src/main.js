import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap'
import axios from 'axios'
import VueCookies from 'vue-cookies';


createApp(App)
.use(store)
.use(router, axios)
.use(VueCookies)
.mount('#app')
window._ = require('lodash');
