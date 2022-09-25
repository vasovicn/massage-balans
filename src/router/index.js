import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MassageReservation from '../views/MassageReservation.vue'
import MassageConfirmation from '../views/MassageConfirmation.vue'
import BackendView from '../views/backend/BackendView.vue'

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/massage/:id',
    name: 'MassageReservation',
    props: true,
    component: MassageReservation
  },
  {
    path: '/massage-confirmation/:id',
    name: 'MassageConfirmation',
    props: true,
    component: MassageConfirmation
  },
  {
    path: '/massage-reservations/',
    name: 'BackendView',
    props: true,
    component: BackendView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
