<script setup>
/* eslint-disable */
import { computed } from 'vue';
import { RouterLink } from 'vue-router';
import { useUserWithdrawal } from '../stores/withdrawal';
import IconLongRight from './icons/IconLongRight.vue';
import IconCreditCard from './icons/IconCreditCard.vue'
import AppWithdrawalCard from './AppWithdrawalCard.vue'

// store
const store = useUserWithdrawal()

const isEmpty = computed(() => {
    return store.withdrawals.data.length == 0
})

const toDate = (value) => {
    return new Date(value).toDateString()
}

// created
store.getWithdrawals()
</script>

<template>
    <div class="w-full h-full min-h-full">

        <div class="w-full h-full flex flex-col">

            <!-- loading -->
            <div v-if="store.withdrawals.loading" class="w-full h-full flex items-center justify-center">
                <IconSetting class="w-10 h-10 fill-slate-600 md:w-20 md:h-20" />
            </div>

            <!-- error -->
            <div v-else-if="store.withdrawals.error" class="w-full h-full flex items-center justify-center">
                <span class="text-red-600 text-sm md:text-lg">{{store.withdrawals.error}}</span>
            </div>

            <!-- empty state -->
            <div v-if="isEmpty" class="w-full h-full flex items-center justify-center">
                <div class="w-full h-60 p-4 flex flex-col gap-5 items-center justify-center border-2 border-dashed border-slate-700 rounded-lg bg-slate-800 md:h-72 md:w-7/12 lg:p-6 lg:w-1/2">
                    <IconCreditCard class="w-20 h-20 fill-slate-700" />
                    <p class="text-center text-slate-600 font-medium text-sm md:text-base">You have not requested for any withdrawals. Please click the link below to select an withdrawal method</p>
                    <div class="">
                        <RouterLink :to="{name: 'withrawalmethods'}" class="text-blue-500 text-sm hover:text-blue-600 md:text-base">Select Withdrawal Method</RouterLink>
                    </div>
                </div>
            </div>

            <!-- success -->
            <div v-else class="w-full h-full flex items-start justify-center">
                <div class="w-full flex flex-col gap-5 p-8 bg-slate-800 rounded-lg">
                    <div class="flex flex-col justify-between md:flex-row">
                        <div class="flex flex-col gap-2">
                            <p class="text-slate-300 font-medium text-2xl md:text-3xl">My withdrawals</p>
                            <span class="text-sm font-normal text-slate-600">A list of all your current withdrawals, both Paid and pending.</span>
                        </div>
                        <div class="">
                            <RouterLink :to="{name: 'withrawalmethods'}" class="group inline-flex items-center gap-2">
                                <span class="text-blue-600 text-sm md:text-base">Request Withdrawal</span>
                                <IconLongRight class="w-7 h-7 fill-slate-500 group-hover:animate-bounce-h" />
                            </RouterLink>
                        </div>
                    </div>

                    <div class="mt-5 flex flex-col gap-2">
                        <AppWithdrawalCard v-for="withdrawal in store.withdrawals.data" :key="withdrawal.id" v-bind="withdrawal" />
                    </div>

                </div>
            </div>


        </div>
    </div>
</template>