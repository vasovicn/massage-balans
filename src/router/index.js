import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MassageConfirmation from '../views/MassageConfirmation.vue'
import BackendView from '../views/backend/BackendView.vue'
import CreateNewMassage from '../views/backend/CreateNewMassage'
import MassageDetails from '../views/MassageDetails'
import UserPortal from '../views/UserPortal'

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
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
  {
    path: '/create-new-masasge',
    name: 'CreateNewMassage',
    component: CreateNewMassage
  },
  {
    path: '/massage-details/:id',
    name: 'MassageDetails',
    props: true,
    component: MassageDetails
  },
  {
    path: '/user-portal',
    name: 'UserPortal',
    props: true,
    component: UserPortal
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
