<script setup>
/* eslint-disable */
import { ref, computed } from 'vue';
import { RouterLink } from 'vue-router';
import { useUserInvestment } from '../stores/investment';
import btclogo from '../assets/images/btc.png';
import qrcode from '../assets/images/qrcode.jpeg';
import AppCopyText from './AppCopyText.vue';
import IconCreditCard from './icons/IconCreditCard.vue';
import IconCloseBig from './icons/IconCloseBig.vue';
import IconLongRight from './icons/IconLongRight.vue';
import IconSetting from './icons/IconSetting.vue';
import AppInvestmentCard from './AppInvestmentCard.vue';

// store
const store = useUserInvestment()

// data
const modal = ref(false)
const investmentId = ref(null)

// computed
const activeInvestment = computed(() => {
    return store.investments.data.find((plan) => plan.id == investmentId.value)
})

const isEmpty = computed(() => {
    return store.investments.data.length == 0
})

// methods
const deposit = (id) => {
    investmentId.value = id
    modal.value = true
}

const toDate = (value) => {
    return new Date(value).toDateString()
}

// created
store.getInvestments()
</script>

<template>
    <div class="w-full h-full min-h-full">

        <div class="w-full h-full flex flex-col">

            <!-- loading -->
            <div v-if="store.investments.loading" class="w-full h-full flex items-center justify-center">
                <IconSetting class="w-10 h-10 fill-slate-600 md:w-20 md:h-20" />
            </div>

            <!-- error -->
            <div v-else-if="store.investments.error" class="w-full h-full flex items-center justify-center">
                <span class="text-red-600 text-sm md:text-lg">{{store.investments.error}}</span>
            </div>

            <!-- empty state -->
            <div v-if="isEmpty" class="w-full h-full flex items-center justify-center">
                <div class="w-full h-60 p-4 flex flex-col gap-5 items-center justify-center border-2 border-dashed border-slate-700 rounded-lg bg-slate-800 md:h-72 md:w-7/12 lg:p-6 lg:w-1/2">
                    <IconCreditCard class="w-20 h-20 fill-slate-700" />
                    <p class="text-center text-slate-600 font-medium text-sm md:text-base">You have not made any deposit. Please click the link below to select an investment plan</p>
                    <div class="">
                        <RouterLink :to="{name: 'investmentplan'}" class="text-blue-500 text-sm hover:text-blue-600 md:text-base">Select Plan</RouterLink>
                    </div>
                </div>
            </div>

            <!-- success -->
            <div v-else class="w-full h-full flex items-start justify-center">
                <div class="w-full flex flex-col gap-5 p-8 bg-slate-800 rounded-lg">
                    <div class="flex flex-col justify-between md:flex-row">
                        <div class="flex flex-col gap-2">
                            <p class="text-slate-300 font-medium text-2xl md:text-3xl">My Investments</p>
                            <span class="text-sm font-normal text-slate-600">A list of all your current investments, both active and pending. please click on the pay now button on investments marked as pending.</span>
                        </div>
                        <div class="">
                            <RouterLink :to="{name: 'investmentplan'}" class="group inline-flex items-center gap-2">
                                <span class="text-blue-600 text-sm md:text-base">Investment</span>
                                <IconLongRight class="w-7 h-7 fill-slate-500 group-hover:animate-bounce-h" />
                            </RouterLink>
                        </div>
                    </div>

                    <div class="mt-5 flex flex-col gap-4 md:gap-2">
                        <AppInvestmentCard @pay-now="deposit(investment.id)" v-for="investment in store.investments.data" :key="investment.id" v-bind="investment" />
                    </div>

                </div>
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
                                    Transfer between <code class="text-blue-600 font-normal">{{activeInvestment.amount}}</code> worth of Bitcoin to the address below
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