<script setup>
/* eslint-disable */
import IconCheckBold from './icons/IconCheckBold.vue';
import AppButton from './AppButton.vue';

// props
const props = defineProps({
    plan: {type: String, default: "Plan"},
    price: {type: String, default: "Price"},
    days: {type: String, default: "days"},
    roi: {type: String, default: '%'},
    id: {type: String}
})

// emits
defineEmits(['deposit'])
</script>

<template>
    <div class="w-full h-full min-h-full">

        <div class="bg-white rounded-md flex flex-col overflow-hidden">

            <div class="w-full bg-slate-100 flex flex-col items-center gap-2 p-8 shadow-lg">
                <span class="text-slate-900 text-sm font-medium md:text-base">{{plan}}</span>
                <span class="text-slate-900 text-xl font-black md:text-2xl lg:text-3xl">{{price}}</span>
                <span class="text-slate-500 text-xs font-normal md:text-sm">({{days}})</span>
            </div>

            <div class="flex flex-col gap-3 p-8">
                <span class="flex gap-3">
                    <IconCheckBold class="w-5 h-5 fill-blue-600" />
                    <span class="text-slate-500 text-sm font-normal">{{props.roi}} Return on investment (ROI)</span>
                </span>

                <span class="flex gap-3">
                    <IconCheckBold class="w-5 h- fill-blue-600" />
                    <span class="text-slate-500 text-sm font-normal">10% Referral bonus</span>
                </span>

                <span class="flex gap-3">
                    <IconCheckBold class="w-5 h-5 fill-blue-600" />
                    <span class="text-slate-500 text-sm font-normal">24/7 Tech support</span>
                </span>
            </div>

            <div class="w-full p-8">
                <AppButton @click.prevent="$emit('deposit', props.id)" name="Deposit" />
            </div>

        </div>

    </div>
</template>