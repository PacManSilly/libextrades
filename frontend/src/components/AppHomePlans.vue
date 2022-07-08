<script setup>
/* eslint-disable */
import { useRouter } from 'vue-router';
import AppInvestmentPlanCard from './AppInvestmentPlanCard.vue';
import {gsap} from "gsap";
import {ScrollTrigger} from "gsap/ScrollTrigger";
import { onMounted, ref } from 'vue';
gsap.registerPlugin(ScrollTrigger);

// router
const router = useRouter()

// refs
const plan = ref("")
const planHead = ref("")

// data
const plans = [
    {id: 1, plan: 'Starter plan', roi: '2.5%', days: '7days', price: '$500 - $3,999'},
    {id: 2, plan: 'Advance plan', roi: '5%', days: '10days', price: '$4,000 - $9,999'},
    {id: 3, plan: 'Premium plan', roi: '8.5%', days: '7days', price: '$10,000 - $14,999'},
    {id: 4, plan: 'Sublime plan', roi: '10%', days: '10days', price: '$15,000 - $29,999'},
    {id: 5, plan: 'Luxury plan', roi: '15%', days: '14days', price: '$30,000 - $500,000'}
]

const planCards = document.getElementsByClassName("planCards")

// methods
const navigateToSignUp = () => {
    router.push({name: 'signup'})
}

const animPlans = () => {
   gsap.from(planHead.value, {scrollTrigger: {trigger: plan.value, start: "200px bottom", markers: false, id: "plan"}, duration: 1, y: 100, opacity: 0})
   gsap.from(planCards, {scrollTrigger: {trigger: plan.value, start: "400px bottom", markers: false, id: "plan"}, duration: 1, y: 100, opacity: 0, stagger: 0.2})
}

onMounted(() => {
    animPlans()
})
</script>

<template>
    <div id="plans" ref="plan" class="w-full h-full min-h-full py-20 bg-slate-900">

        <div class="w-11/12 mx-auto flex flex-col gap-y-20 lg:w-10/12">

            <div ref="planHead" class="flex flex-col items-center gap-2">
                <h2 class="text-white text-xl font-black md:text-3xl">Investment Plans</h2>
                <p class="w-11/12 mx-auto text-center text-xs text-slate-500 md:text-sm lg:w-1/2">
                    Start investing with as low as $500 for the starter plan. You can select your preferred option from the plans below.
                </p>
            </div>

            <div class="pb-5 grid grid-cols-1 gap-5 md:grid-cols-2 lg:grid-cols-3">
                <AppInvestmentPlanCard @click.prevent="navigateToSignUp" v-for="plan in plans" :key="plan.id" v-bind="plan" class="planCards" />
            </div>
        
        </div>

    </div>
</template>