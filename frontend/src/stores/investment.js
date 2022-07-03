/* eslint-disable */
import { defineStore } from "pinia";
import { useUserStore } from "./user";
import axios from "axios";


export const useUserInvestment = defineStore({
    id: 'investment',
    state: () => ({
        investments: {loading: false, data: JSON.parse(localStorage.getItem('libex_investments')), error: null},
        newInvestment: {loading: false, error: null}
    }),
    actions: {
        async getInvestments() {
            // user store
            const userStore = useUserStore()
            this.investments.loading = true
            await axios.get('investments/', {headers: {'Authorization': `Bearer ${JSON.parse(localStorage.getItem('libex_token'))}`}})
              .then((resp) => {
                this.investments.loading = false
                this.investments.error = null,
                localStorage.setItem('libex_investments', JSON.stringify(resp.data))
                this.investments.data = JSON.parse(localStorage.getItem('libex_investments'))
              })
              .catch((err) => {
                this.investments.loading = false
                if (err.response.status == 401) userStore.signOut()
                else this.investments.error = "An error occured"
              })
        },
        async createInvestment(data) {
            // user store
            const userStore = useUserStore()
            this.newInvestment.loading = true
            await axios.post('investments/new/', {...data}, {headers: {'Authorization': `Bearer ${JSON.parse(localStorage.getItem('libex_token'))}`}})
                .then((resp) => {
                    this.newInvestment.loading = false
                    this.newInvestment.error = null
                    
                    // redirect to deposite history
                    this.$router.push({name: 'deposithistory'})
                })
                .catch((err) => {
                    this.newInvestment.loading = false
                    if (err.response.status == 401) userStore.signOut()
                    else this.newInvestment.error = "error"
                })
        },
    }
})