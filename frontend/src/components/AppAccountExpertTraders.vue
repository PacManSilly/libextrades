<script setup>
/* eslint-disable */
import { ref, computed } from 'vue';
import { RouterLink } from 'vue-router';
import { useUserTrader } from '../stores/trader';
import { useUserStore } from '../stores/user';
import btclogo from '../assets/images/btc.png';
import AppButton from './AppButton.vue';
import AppTraderCard from './AppTraderCard.vue'
import IconCloseBig from './icons/IconCloseBig.vue';
import IconLongLeft from './icons/IconLongLeft.vue'
import IconSetting from './icons/IconSetting.vue'

// store
const store = useUserTrader()
const userStore = useUserStore()

// data
const modal = ref(false)
const traderId = ref(null)
const userId = userStore.userData.data.id

// computed
const activeTrader = computed(() => {
    return store.traders.data.find((trader) => trader.id == traderId.value)
})

const isEmpty = computed(() => {
    return store.traders.data.length == 0;
})

// methods
const viewTrader = (id) => {
    traderId.value = id
    modal.value = true
}

const addTrader = () => {
    const data = {
        traderId: activeTrader.value.id,
        investors: [userStore.userData.data.id]
    }

    store.createTrader(data)
}

// created
store.getTraders()
</script>

<template>
    <div class="w-full h-full min-h-full">

        <div class="w-full h-full flex flex-col">

            <div>
                <RouterLink :to="{name: 'mytraders'}" class="group inline-flex items-center gap-2">
                    <IconLongLeft class="w-7 h-7 fill-slate-600 group-hover:animate-bounce-h" />
                    <span class="text-blue-600 text-sm md:text-base">Back</span>
                </RouterLink>
            </div>

            <div class="w-full flex flex-col gap-20 mt-10 items-center justify-between pb-10 md:justify-center">

                <div>
                    <span class="text-slate-200 text-2xl font-medium md:text-4xl">Available Traders</span>
                </div>

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
                        <p class="text-center text-slate-600 font-medium text-sm md:text-base">No Expert traders yet</p>
                    </div>
                </div>

                <div v-else class="w-full grid gap-5 grid-cols-1 md:grid-cols-3 lg:grid-cols-4">
                    <AppTraderCard
                        @trader-clicked="viewTrader"
                        v-for="trader in store.traders.data"
                        :key="trader.id"
                        v-bind="trader"
                        :name="trader.full_name"
                        :rate="trader.win_rate"
                        :share="trader.profit_share"
                        :active="trader.investors.includes(userId)" />
                </div>

            </div>
        
        </div>

        <!-- trader modal -->
        <teleport to="body">
            <transition
                enter-from-class="scale-0 opacity-0"
                enter-active-class="transition-all duration-150"
                leave-to-class="scale-0 opacity-0"
                leave-active-class="transition-all duration-150">
                <div v-if="modal" class="w-full absolute top-0 z-30 h-screen min-h-[40rem] bg-slate-900/90 backdrop-blur-lg">

                    <div class="w-full h-full relative flex items-center justify-center">
                        
                        <!-- close button -->
                        <button @click.prevent="modal = false" type="button" class="absolute group top-5 left-5 p-2 rounded transition-all duration-150 hover:bg-slate-800">
                            <IconCloseBig class="w-10 h-10 fill-slate-400 group-hover:fill-slate-200" />
                        </button>
                        
                        
                        <div class="w-10/12 flex flex-col gap-10 items-center lg:w-1/2">
                            
                             <div>
                                <img :src="btclogo" class="h-32 w-32">
                            </div>

                            <div class="w-full flex flex-col gap-3 bg-slate-800 p-4 rounded-md md:w-1/2">
                                <div class="flex gap-5">
                                    <span class="text-slate-500 text-lg font-normal">Name:</span>
                                    <span class="text-slate-400 font-medium text-lg">{{activeTrader.full_name}}</span>
                                </div>
                                <div class="flex gap-5">
                                    <span class="text-slate-500 text-lg font-normal">Email:</span>
                                    <span class="text-slate-400 font-medium text-lg">{{activeTrader.email}}</span>
                                </div>
                                <div class="flex gap-5">
                                    <span class="text-slate-500 text-lg font-normal">Win Rate:</span>
                                    <span class="text-slate-400 font-medium text-lg">{{activeTrader.win_rate}}</span>
                                </div>
                                <div class="flex gap-5">
                                    <span class="text-slate-500 text-lg font-normal">Profit Share:</span>
                                    <span class="text-slate-400 font-medium text-lg">{{activeTrader.profit_share}}</span>
                                </div>
                                <div class="mt-5">
                                    <AppButton v-if="activeTrader.investors.includes(userId)" @click.prevent="modal = false" name="Already Your Trader" :loading="store.addTrader.loading" />
                                    <AppButton v-else @click.prevent="addTrader" name="Add Trader" />
                                </div>
                            </div>

                        </div>

                    </div>
                </div>
            </transition>
        </teleport>

    </div>
</template>