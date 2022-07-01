<script setup>
/* eslint-disable */
import { ref, computed } from 'vue';
import btclogo from '../assets/images/btc.png';
import AppButton from './AppButton.vue';
import IconCloseBig from './icons/IconCloseBig.vue';

// data
const modal = ref(false)
const traderId = ref(null)
const traders = [
    {id: 1, name: 'Full Name 1', email: 'email@email.com', rate: '90%', share: '20%'},
    {id: 2, name: 'Full Name 2', email: 'email@email.com', rate: '80%', share: '20%'},
    {id: 3, name: 'Full Name 3', email: 'email@email.com', rate: '70%', share: '20%'},
    {id: 4, name: 'Full Name 4', email: 'email@email.com', rate: '60%', share: '20%'},
    {id: 5, name: 'Full Name 5', email: 'email@email.com', rate: '50%', share: '20%'},
    {id: 6, name: 'Full Name 6', email: 'email@email.com', rate: '40%', share: '20%'},
    {id: 7, name: 'Full Name 7', email: 'email@email.com', rate: '30%', share: '20%'},
    {id: 8, name: 'Full Name 8', email: 'email@email.com', rate: '20%', share: '20%'},
    {id: 9, name: 'Full Name 9', email: 'email@email.com', rate: '10%', share: '20%'},
    {id: 10, name: 'Full Name 10', email: 'email@email.com', rate: '12%', share: '20%'},
    {id: 11, name: 'Full Name 11', email: 'email@email.com', rate: '44%', share: '20%'},
    {id: 12, name: 'Full Name 12', email: 'email@email.com', rate: '22%', share: '20%'},
]

// computed
const activeTrader = computed(() => {
    return traders.find((trader) => trader.id == traderId.value)
})

// methods
const viewTrader = (id) => {
    traderId.value = id
    modal.value = true
}
</script>

<template>
    <div class="w-full h-full min-h-full">

        <div class="w-full h-full flex flex-col">

            <div class="flex flex-col gap-2 pb-5 mt-10 mb-10 border-b border-slate-700 lg:mt-0">
                <h1 class="text-white text-4xl font-black">Copy Expert Traders</h1>
                <span class="text-slate-600 font-normal tracking-wide">Select one expert trader to become your manager</span>
            </div>

            <div class="w-full flex flex-col gap-20 mt-10 items-center justify-between pb-10 md:justify-center">

                <div>
                    <span class="text-slate-200 text-2xl font-medium md:text-4xl">Available Traders</span>
                </div>

                <div class="w-full grid gap-5 grid-cols-1 md:grid-cols-3 lg:grid-cols-4">
                    <div v-for="trader in traders" :key="trader.id" class="w-full flex gap-3 bg-slate-800 p-3 rounded-md">
                        <img :src="btclogo" class="w-10 h-10 rounded-full overflow-hidden">
                        <div class="flex flex-col items-start">
                            <button type="button" @click.prevent="viewTrader(trader.id)" class="text-blue-600 text-base font-medium">{{trader.name}}</button>
                            <span class="text-sm font-normal text-slate-500">Win Rate: {{trader.rate}}</span>
                            <span class="text-sm font-normal text-slate-500">Profit Share: {{trader.share}}</span>
                        </div>
                    </div>
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
                                    <span class="text-slate-400 font-medium text-lg">{{activeTrader.name}}</span>
                                </div>
                                <div class="flex gap-5">
                                    <span class="text-slate-500 text-lg font-normal">Email:</span>
                                    <span class="text-slate-400 font-medium text-lg">{{activeTrader.email}}</span>
                                </div>
                                <div class="flex gap-5">
                                    <span class="text-slate-500 text-lg font-normal">Win Rate:</span>
                                    <span class="text-slate-400 font-medium text-lg">{{activeTrader.rate}}</span>
                                </div>
                                <div class="flex gap-5">
                                    <span class="text-slate-500 text-lg font-normal">Profit Share:</span>
                                    <span class="text-slate-400 font-medium text-lg">{{activeTrader.share}}</span>
                                </div>
                                <div class="mt-5">
                                    <AppButton name="Add Trader" />
                                </div>
                            </div>

                        </div>

                    </div>
                </div>
            </transition>
        </teleport>

    </div>
</template>