import { createStore } from 'vuex'
import MassageService from '@/services/MassageService'

export default createStore({
  state: {
    user: 'Adam Jahr',
    massages: [],
    reservedTime: [],
    massage: null,
    masseuers: [],
    masseur: null,
    reservation: [],
    reservations: [],
    allTermins: ['08:00', '08:15', '08:30', '08:45',
                 '09:00', '09:15', '09:30', '09:45',
                 '10:00', '10:15', '10:30', '10:45',
                 '11:00', '11:15', '11:30', '11:45',
                 '12:00', '12:15', '12:30', '12:45',
                 '13:00', '13:15', '13:30', '13:45',
                 '14:00', '14:15', '14:30', '14:45',
                 '15:00', '15:15', '15:30', '15:45',
                 '16:00', '16:15', '16:30', '16:45',
                 '17:00', '17:15', '17:30', '17:45',
                 '18:00', '18:15', '18:30', '18:45',
                 '19:00', '19:15', '19:30', '19:45',
                 '20:00', '20:15', '20:30', '20:45',
                 '21:00', '21:15', '21:30', '21:45',
                 '22:00' ]
  },
  mutations: {
    SET_MASSAGES(state, massages) {
      state.massages = massages
    },
    SET_MASSAGE(state, massage) {
        state.massage = massage
    },
    SET_RESERVE_TIME(state, reservedTime) {
      state.reservedTime = reservedTime
    },
    SET_MASSEUERS(state, masseuers) {
      state.masseuers = masseuers
    },
    SET_MASSEUR(state, masseur) {
      state.masseur = masseur
    },
    POST_RESERVE_TIME(state, reservation) {
      state.reservation = reservation
    },
    SET_RESERVATIONS(state, reservations) {
      console.log('SASASASA:', reservations)
      state.reservations = reservations
    }
  },
  actions: {
    fetchMassages({ commit }) {
      return MassageService.getMassages()
        .then(response => {
          commit('SET_MASSAGES', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    fetchMassage({ commit, state }, id) {
    const massage = state.massages.find(massage => massage.id === id)
      if (massage) {
        commit('SET_MASSAGE', massage)
      } else {
        return MassageService.getMassage(id)
          .then(response => {
            commit('SET_MASSAGE', response.data)
          })
          .catch(error => {
            console.log(error)
          })
    }
    },
    fetchMasseur({ commit }) {
      return MassageService.getMasseur()
        .then(response => {
          commit('SET_MASSEUR', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    fetchMasseuers({ commit }) {
      return MassageService.getMasseuers()
        .then(response => {
          commit('SET_MASSEUERS', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    fetchReservedTime({ commit }, date) {
        return MassageService.getReservedTime(date)
          .then(response => {
            commit('SET_RESERVE_TIME', response.data)
          })
          .catch(error => {
            console.log(error)
          })
    
    },
    postReservedTime({ commit }, reservation) {
      return MassageService.postReservation(reservation)
          .then(response => {
            commit('POST_RESERVE_TIME', response.data)
          })
          .catch(error => {
            console.log(error)
          })
    },
    fetchAllReservations({ commit }) {
      return MassageService.getAllReservations()
        .then(response => {
          console.log(response.data)
          commit('SET_RESERVATIONS', response.data)
        })
        .catch(error => {
          console.log(error)
        })
  },
  }
})
