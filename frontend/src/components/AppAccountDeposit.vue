<script setup>
/* eslint-disable */
import { ref, computed } from 'vue';
import AppAccountPlan from './AppAccountPlan.vue';
import btclogo from '../assets/images/btc.png';
import qrcode from '../assets/images/qrcode.jpeg';
import AppCopyText from './AppCopyText.vue';
import IconCloseBig from './icons/IconCloseBig.vue';


// data
const modal = ref(false)
const planId = ref(null)
const plans = [
    {id: 1, plan: 'Starter plan', roi: '2.5%', days: '7days', price: '$500 - $3,999'},
    {id: 2, plan: 'Advance plan', roi: '5%', days: '10days', price: '$4,000 - $9,999'},
    {id: 3, plan: 'Premium plan', roi: '8.5%', days: '7days', price: '$10,000 - $14,999'},
    {id: 4, plan: 'Sublime plan', roi: '10%', days: '10days', price: '$15,000 - $29,999'},
    {id: 5, plan: 'Starter plan', roi: '15%', days: '14days', price: '$30,000 - $500,000'}
]

// computed
const activePlan = computed(() => {
    return plans.find((plan) => plan.id == planId.value)
})

const deposite = (id) => {
    planId.value = id
    modal.value = true
}
</script>

<template>
    <div class="w-full h-full min-h-full">

        <div class="w-full h-full flex flex-col">

            <div class="flex flex-col gap-2 pb-5 mt-10 mb-10 border-b border-slate-700 lg:mt-0">
                <h1 class="text-white text-4xl font-black">Deposit</h1>
                <span class="text-slate-600 font-normal tracking-wide">Select an investment plan that best suits you.</span>
            </div>

            <div class="pb-5 grid grid-cols-1 gap-5 md:grid-cols-2 lg:grid-cols-3">
                <AppAccountPlan @deposit="deposite" v-for="plan in plans" :key="plan.id" v-bind="plan" />
            </div>
        
        </div>

        <!-- payment modal -->
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
                            
                            <!-- start of btc logo -->
                            <div>
                                <img :src="btclogo" class="h-32 w-32">
                            </div>

                            <div class="w-full flex flex-col gap-10 text-center md:w-10/12">
                                <span class="text-slate-400 text-sm md:text-base">
                                    Transfer between <code class="text-blue-600 font-normal">{{activePlan.price}}</code> worth of Bitcoin to the address below
                                    or scan the QRCode with your Crypto wallet app
                                </span>

                                <div class="flex flex-col items-center justify-center gap-10">
                                    
                                    <!-- start of coin address and copy button -->
                                    <AppCopyText>
                                        <template #copy>
                                            Copy address
                                        </template>

                                        <template #text>
                                            bc1q0agxmcdkp9r4h57dpm583wnqg0cq4r7uc5lzmx
                                        </template>
                                    </AppCopyText>
                                    <!-- end of coin address and copy button -->

                                    <!-- start of coin qrcode -->
                                    <div>
                                        <img :src="qrcode" class="w-40 h-40 md:h-60 md:w-60">
                                    </div>
                                    <!-- end of coin qrcode -->

                                    <div>
                                        <span class="text-slate-400 text-sm md:text-base">
                                            Your Investment will automatically begin when
                                            the system recieves at most two blockchain confirmations.
                                        </span>
                                    </div>

                                </div>
                            </div>

                        </div>

                    </div>
                </div>
            </transition>
        </teleport>

    </div>
</template>