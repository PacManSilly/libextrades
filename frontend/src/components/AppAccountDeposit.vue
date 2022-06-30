<script setup>
/* eslint-disable */
import AppAccountPlan from './AppAccountPlan.vue';

// data
const plans = [
    {plan: 'Starter plan', roi: '2.5%', days: '7days', price: '$500 - $3,999'},
    {plan: 'Advance plan', roi: '5%', days: '10days', price: '$4,000 - $9,999'},
    {plan: 'Premium plan', roi: '8.5%', days: '7days', price: '$10,000 - $14,999'},
    {plan: 'Sublime plan', roi: '10%', days: '10days', price: '$15,000 - $29,999'},
    {plan: 'Starter plan', roi: '15%', days: '14days', price: '$30,000 - $500,000'}
]
</script>

<template>
    <div class="w-full h-full min-h-[55rem]">

        <div class="w-full h-full flex flex-col">

            <div class="flex flex-col gap-2 pb-5 mt-10 mb-10 border-b border-slate-700 md:mt-0">
                <h1 class="text-white text-4xl font-black">Deposit</h1>
                <span class="text-slate-600 font-normal tracking-wide">Select an investment plan that best suits you.</span>
            </div>

            <div class="pb-5 grid grid-cols-1 gap-5 md:grid-cols-2 lg:grid-cols-3">
                <AppAccountPlan v-for="plan in plans" v-bind="plan" />
            </div>
        
        </div>

    </div>
</template>