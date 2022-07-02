<script setup>
/* eslint-disable */
import { ref, computed } from 'vue';
import { RouterLink } from 'vue-router';
import { useUserInvestment } from '../stores/investment';
import AppInvestmentPlanCard from './AppInvestmentPlanCard.vue';
import IconCloseBig from './icons/IconCloseBig.vue';
import IconLongLeft from './icons/IconLongLeft.vue';

// store
const store = useUserInvestment()

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

// methods
const selectPlan = (id) => {
    planId.value = id
    modal.value = true
}

const deposit = () => {
    const data = {
        plan: activePlan.value.plan,
        amount: activePlan.value.price,
        days: activePlan.value.days,
    }

    store.createInvestment(data)
}
</script>

<template>
    <div class="w-full h-full min-h-full">

        <div class="w-full h-full flex flex-col gap-5">

            <div>
                <RouterLink :to="{name: 'deposithistory'}" class="group inline-flex items-center gap-2">
                    <IconLongLeft class="w-7 h-7 fill-slate-600 group-hover:animate-bounce-h" />
                    <span class="text-blue-600 text-sm md:text-base">Back</span>
                </RouterLink>
            </div>

            <div class="pb-5 grid grid-cols-1 gap-5 md:grid-cols-2 lg:grid-cols-3">
                <AppInvestmentPlanCard @deposit="selectPlan" v-for="plan in plans" :key="plan.id" v-bind="plan" />
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
                            <!-- error -->
                            <div v-if="store.newInvestment.error" class="w-full h-full flex items-center justify-center">
                                <span class="text-red-600 text-sm md:text-lg">{{store.newInvestment.error}}</span>
                            </div>

                            <div>
                                <span class="text-base font-bold text-slate-100">You have selected this plan. Click deposit to proceed</span>
                            </div>
                            
                            <AppInvestmentPlanCard @deposit="deposit" v-bind="activePlan" :loading="store.newInvestment.loading" />
                        </div>

                    </div>
                </div>
            </transition>
        </teleport>

    </div>
</template>