/* eslint-disable */
import { defineStore } from "pinia";
import { useUserStore } from "./user";
import axios from "axios";


export const useUserWithdrawal = defineStore({
    id: 'withdrawal',
    state: () => ({
        withdrawals: {loading: false, data: JSON.parse(localStorage.getItem('libex_withdrawals')), error: null},
        newWithdrawal: {loading: false, error: null}
    }),
    actions: {
        async getWithdrawals() {
            // user store
            const userStore = useUserStore()
            this.withdrawals.loading = true
            await axios.get('withdrawals/', {headers: {'Authorization': `Bearer ${JSON.parse(localStorage.getItem('libex_token'))}`}})
              .then((resp) => {
                this.withdrawals.loading = false
                this.withdrawals.error = null,
                localStorage.setItem('libex_withdrawals', JSON.stringify(resp.data))
                this.withdrawals.data = JSON.parse(localStorage.getItem('libex_withdrawals'))
              })
              .catch((err) => {
                this.withdrawals.loading = false
                if (err.response.status == 401) userStore.signOut()
                else this.withdrawals.error = "An error occured"
              })
        },
        async createWithdrawal(data) {
            // user store
            const userStore = useUserStore()
            this.newWithdrawal.loading = true
            await axios.post('withdrawals/new/', {...data}, {headers: {'Authorization': `Bearer ${JSON.parse(localStorage.getItem('libex_token'))}`}})
                .then((resp) => {
                    this.newWithdrawal.loading = false
                    this.newWithdrawal.error = null
                    
                    // redirect to deposite history
                    this.$router.push({name: 'withrawalhistory'})
                })
                .catch((err) => {
                    this.newWithdrawal.loading = false
                    if (err.response.status == 401) userStore.signOut()
                    else this.newWithdrawal.error = "error"
                })
        },
    }
})