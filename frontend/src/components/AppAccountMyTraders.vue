<script setup>
/* eslint-disable */
import { computed } from 'vue';
import { RouterLink } from 'vue-router';
import { useUserTrader } from '../stores/trader';
import { useUserStore } from '../stores/user';
import IconLongRight from './icons/IconLongRight.vue';
import IconRefresh from './icons/IconRefresh.vue';
import AppTraderCard from './AppTraderCard.vue';

// store
const store = useUserTrader()
const userStore = useUserStore()

// data
const userId = userStore.userData.data.id

// computed
const isEmpty = computed(() => {
    return store.traders.data.filter((trader) => trader.investors.includes(userId)).length == 0;
})

const toDate = (value) => {
    return new Date(value).toDateString()
}

const myTraders = computed(() => {
    return store.traders.data.filter((trader) => trader.investors.includes(userId))
})

// created
store.getTraders()
</script>

<template>
    <div class="w-full h-full min-h-full">

        <div class="w-full h-full flex flex-col">

            <!-- loading -->
            <div v-if="store.traders.loading" class="w-full h-full flex items-center justify-center">
                <IconSetting class="w-10 h-10 fill-slate-600 md:w-20 md:h-20" />
            </div>

            <!-- error -->
            <div v-else-if="store.traders.error" class="w-full h-full flex items-center justify-center">
                <span class="text-red-600 text-sm md:text-lg">{{store.traders.error}}</span>
            </div>

            <!-- empty state -->
            <div v-if="isEmpty" class="w-full h-full flex items-center justify-center">
                <div class="w-full h-60 p-4 flex flex-col gap-5 items-center justify-center border-2 border-dashed border-slate-700 rounded-lg bg-slate-800 md:h-72 md:w-7/12 lg:p-6 lg:w-1/2">
                    <IconRefresh class="w-20 h-20 fill-slate-700" />
                    <p class="text-center text-slate-600 font-medium text-sm md:text-base">You don't have any expert trader. Please click the link below to select an expert trader</p>
                    <div class="">
                        <RouterLink :to="{name: 'experttraders'}" class="text-blue-500 text-sm hover:text-blue-600 md:text-base">Select Expert Trader</RouterLink>
                    </div>
                </div>
            </div>

            <!-- success -->
            <div v-else class="w-full h-full flex items-start justify-center">
                <div class="w-full flex flex-col gap-5 p-8 bg-slate-800 rounded-lg">
                    <div class="flex flex-col justify-between md:flex-row">
                        <div class="flex flex-col gap-2">
                            <p class="text-slate-300 font-medium text-2xl md:text-3xl">My Expert Traders</p>
                            <span class="text-sm font-normal text-slate-600">A list of all your expert traders.</span>
                        </div>
                        <div class="">
                            <RouterLink :to="{name: 'experttraders'}" class="group inline-flex items-center gap-2">
                                <span class="text-blue-600 text-sm md:text-base">Select Expert</span>
                                <IconLongRight class="w-7 h-7 fill-slate-500 group-hover:animate-bounce-h" />
                            </RouterLink>
                        </div>
                    </div>

                    <div class="w-full mt-5 grid gap-5 grid-cols-1 bg-slate-900 p-4 md:grid-cols-3 lg:grid-cols-4">
                        <AppTraderCard v-for="trader in myTraders" :key="trader.id" v-bind="trader" :name="trader.full_name" :rate="trader.win_rate" :share="trader.profit_share" :active="true" />
                    </div>

                </div>
            </div>


        </div>
    </div>
</template>