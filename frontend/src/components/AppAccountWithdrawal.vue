<script setup>
/* eslint-disable */
import IconCloseBig from './icons/IconCloseBig.vue';
import { ref, computed } from 'vue';
import IconCreditCard from './icons/IconCreditCard.vue';
import AppInputField from './AppInputField.vue';
import AppButton from './AppButton.vue';
import IconBitcoin from './icons/IconBitcoin.vue'
import IconEthereum from './icons/IconEthereum.vue'
import IconPayPal from './icons/IconPayPal.vue'

// data
const modal = ref(false)
const tabId = ref(null)
const tabs = [
    {id: 1, type: "Bitcoin", fields: [
        {id: 1, name: "Bitcoin Wallet Address"},
        {id: 2, name: "Amount in USD"},
    ]},
    {id: 2, type: "Ethereum", fields: [
        {id: 1, name: "Ethereum Wallet Address"},
        {id: 2, name: "Amount in USD"},
    ]},
    {id: 3, type: "PayPal", fields: [
        {id: 1, name: "PayPal Email Address"},
        {id: 2, name: "Amount in USD"},
    ]},
    {id: 4, type: "Bank", fields: [
        {id: 1, name: "Bank Name"},
        {id: 2, name: "Account Number"},
        {id: 3, name: "SWIFT Code"},
        {id: 4, name: "Amount in USD"},
    ]}
]

// computed
const activeTab = computed(() => {
    return tabs.find((tab) => tab.id == tabId.value)
})

// methods
const withdrawal = (id) => {
    tabId.value = id
    modal.value = true
}

</script>

<template>
    <div class="w-full h-full min-h-full">

        <div class="w-full h-full flex flex-col">

            <div class="flex flex-col gap-2 pb-5 mt-10 mb-10 border-b border-slate-700 lg:mt-0">
                <h1 class="text-white text-4xl font-black">Withdrawal</h1>
                <span class="text-slate-600 font-normal tracking-wide">Select a withdrawal method</span>
            </div>

            <div class="w-full flex flex-col gap-20 mt-10 items-center justify-between md:justify-center">
                <div class="flex gap-5">
                    <button v-for="tab in tabs" :key="tab.id" @click.prevent="withdrawal(tab.id)" class="px-4 py-2 border border-slate-500 rounded text-slate-500 font-medium text-lg transition-all duration-150 hover:bg-slate-800 hover:text-white">
                        {{tab.type}}
                    </button>
                </div>

                <div class="w-full h-full flex items-center justify-center">
                    <div class="w-full h-60 p-4 flex flex-col items-center justify-center border-2 border-dashed border-slate-700 rounded-lg bg-slate-800 md:h-72 md:w-7/12 lg:p-0 lg:w-1/2">
                        <IconCreditCard class="w-20 h-20 fill-slate-700" />
                        <p class="text-center text-slate-700 font-medium text-sm md:text-base">Please select your preferred method from the options above</p>
                    </div>
                </div>
            </div>
        
        </div>

        <!-- withdrawal modal -->
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
                                <IconBitcoin v-if="activeTab.type == 'Bitcoin'" class="w-40 h-40 fill-slate-700" />
                                <IconEthereum v-if="activeTab.type == 'Ethereum'" class="w-40 h-40 fill-slate-700" />
                                <IconPayPal v-if="activeTab.type == 'PayPal'" class="w-40 h-40 fill-slate-700" />
                                <IconCreditCard v-if="activeTab.type == 'Bank'" class="w-40 h-40 fill-slate-700" />
                            </div>
                            
                            <div>
                                <span class="font-medium text-sm text-slate-500">Please make sure you provide the correct {{activeTab.type}} address</span>
                            </div>

                            <form @submit.prevent class="w-full flex flex-col gap-5 md:w-2/3">
                                <AppInputField v-for="field in activeTab.fields" :key="field.id" :label="field.name" />
                                <AppButton name="Withdraw" />                             
                            </form>

                        </div>
                        
                    </div>
                </div>
            </transition>
        </teleport>

    </div>
</template>