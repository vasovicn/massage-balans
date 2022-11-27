import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MassageConfirmation from '../views/MassageConfirmation.vue'
import BackendView from '../views/backend/BackendView.vue'
// import CreateNewMassage from '../views/backend/CreateNewMassage'
import MassageDetails from '../views/MassageDetails'
// import UserPortal from '../views/portal/UserPortal'
import LayoutPortal from '../views/portal/LayoutPortal'
import FeautureReservations from '../views/portal/FeautureReservations'
import PastReservations from '../views/portal/PastReservations'
import ResetPassword from '../views/ResetPassword'
import PageNotFound from '../views/PageNotFound'
import PriceList from '../views/PriceList'

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
  // {
  //   path: '/create-new-masasge',
  //   name: 'CreateNewMassage',
  //   component: CreateNewMassage
  // },
  {
    path: '/massage-details/:id',
    name: 'MassageDetails',
    props: true,
    component: MassageDetails
  },
  {
    path: '/user-portal',
    name: 'LayoutPortal',
    props: true,
    component: LayoutPortal,
    children: [
      {
        path: '',
        name: 'FeautureReservations',
        component: FeautureReservations
      },
      {
        path: 'past',
        name: 'PastReservations',
        component: PastReservations
      }
    ]
  },
  {
    path: '/massage-reservations/:uidb64/:token',
    name: 'ResetPassword',
    props: true,
    component: ResetPassword
  },
  { path: '/:pathMatch(.*)*',
    component: PageNotFound
  },
  {
    path: '/price-list',
    name: 'PriceList',
    component: PriceList
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
